r"""Extract FHIRPath tests from tests-fhir-r5.xml for coverage analysis.

Data-extraction utility — outputs test data for interactive inspection
or for LLM-based coverage analysis.

Usage:
    python scripts/check_coverage.py --feature <testing-value>
    python scripts/check_coverage.py --file <review-file.md>
    python scripts/check_coverage.py --list
    python scripts/check_coverage.py --json
    python scripts/check_coverage.py --json --file <review-file.md>

--feature <name>  Print all tests whose testing attribute matches <name>.
--file <file>     Target a single review file (reads its Name: field).
                  In text mode: prints review content + tests.
                  In JSON mode: outputs JSON for that file only.
--list            List all distinct testing values and their test counts.
--json            Output JSON (for LLM pipeline / batch processing).
                  Without --file: all review files.
                  With --file: single review file.

Text output format (default):
    One test per block, separated by blank lines:
        name: <test name>
        description: <description>
        expression: <FHIRPath expression>
        invalid: <semantic|syntax|execution>   (only if present)
        mode: <mode>                           (only if present)
        inputfile: <filename>
        output[0]: <type> = <value>
        output[1]: <type> = <value>
        (no output lines means expected result is empty collection)

Reads:
    - ../fhir-test-cases/r5/fhirpath/tests-fhir-r5.xml  (FHIRPath test suite)
"""

import json
import os
import re
import sys

# Ensure Unicode output on Windows
if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
    sys.stdout.reconfigure(encoding="utf-8")

from fhirpath_utils import TESTS_XML, TESTS_DIR, load_tests_by_testing, get_feature_name_from_review, format_tests


def _resolve_file_arg():
    """Read --file argument and resolve to (filepath, feature_name)."""
    idx = sys.argv.index("--file")
    if idx + 1 >= len(sys.argv):
        print("ERROR: --file requires a filename", file=sys.stderr)
        sys.exit(1)
    filepath = sys.argv[idx + 1]
    if not os.path.isabs(filepath):
        filepath = os.path.join(TESTS_DIR, filepath)
    if not os.path.exists(filepath):
        print(f"ERROR: File not found: {filepath}", file=sys.stderr)
        sys.exit(1)
    feature_name = get_feature_name_from_review(filepath)
    if not feature_name:
        print(f"ERROR: No Name: field in {filepath}", file=sys.stderr)
        sys.exit(1)
    return filepath, feature_name


def _parse_existing_analysis(content):
    """Extract existing covered/gaps/summary_text from a review file."""
    result = {"covered": [], "gaps": [], "summary_text": ""}

    cov_idx = content.find("### Coverage")
    if cov_idx < 0:
        return result

    # Limit to between ### Coverage and ### Test Results
    tr_idx = content.find("### Test Results", cov_idx)
    section = content[cov_idx:tr_idx] if tr_idx >= 0 else content[cov_idx:]

    # Extract Covered items (lines starting with "- ✅")
    for m in re.finditer(r'^- ✅\s*(.+)$', section, re.MULTILINE):
        result["covered"].append(m.group(1))

    # Extract Gaps items (lines starting with "- ❌")
    for m in re.finditer(r'^- ❌\s*(.+)$', section, re.MULTILINE):
        result["gaps"].append(m.group(1))

    # Extract summary_text: text after **Summary:** line (skip the stats line itself)
    sm = re.search(r'^\*\*Summary:\*\*.*$', content, re.MULTILINE)
    if sm:
        after = content[sm.end():].lstrip('\n')
        # Take text up to next section or end, stop at ### or end of file
        end = re.search(r'^###|\Z', after, re.MULTILINE)
        summary_text = after[:end.start()].strip() if end else after.strip()
        result["summary_text"] = summary_text

    return result


def _extract_spec_header(content):
    """Extract the 'Header in specification:' value from review file content."""
    m = re.search(r'^Header in specification:\s*(.+)$', content, re.MULTILINE)
    return m.group(1).strip() if m else None


def _build_json_entry(filename, feature, tests, content):
    """Build a JSON-serializable dict for a single review file."""
    # Strip redundant 'testing' key from test dicts
    clean_tests = []
    for t in tests:
        ct = dict(t)
        ct.pop("testing", None)
        clean_tests.append(ct)

    entry = {
        "filename": filename,
        "feature": feature,
        "spec_header": _extract_spec_header(content),
        "tests": clean_tests,
    }

    # Include existing analysis so LLM can review/update rather than regenerate
    existing = _parse_existing_analysis(content)
    if existing["covered"] or existing["gaps"] or existing["summary_text"]:
        entry["existing_analysis"] = existing

    return entry


def main():
    if not os.path.exists(TESTS_XML):
        print(f"ERROR: Test file not found: {TESTS_XML}", file=sys.stderr)
        sys.exit(1)

    use_json = "--json" in sys.argv
    has_file = "--file" in sys.argv

    # --list: summary of all features
    if "--list" in sys.argv:
        tests_by_feature = load_tests_by_testing(TESTS_XML)
        for name in sorted(tests_by_feature.keys()):
            print(f"{name}: {len(tests_by_feature[name])} tests")
        return

    tests_by_feature = load_tests_by_testing(TESTS_XML)

    # --json mode (batch or single file)
    if use_json:
        if has_file:
            filepath, feature = _resolve_file_arg()
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            tests = tests_by_feature.get(feature, [])
            entry = _build_json_entry(os.path.basename(filepath), feature, tests, content)
            json.dump(entry, sys.stdout, ensure_ascii=False, indent=1)
            print()
        else:
            files = sorted(f for f in os.listdir(TESTS_DIR) if f.endswith(".md"))
            all_data = []
            for f in files:
                fp = os.path.join(TESTS_DIR, f)
                feat = get_feature_name_from_review(fp)
                if not feat:
                    continue
                with open(fp, "r", encoding="utf-8") as fh:
                    content = fh.read()
                tests = tests_by_feature.get(feat, [])
                all_data.append(_build_json_entry(f, feat, tests, content))
            json.dump(all_data, sys.stdout, ensure_ascii=False, indent=1)
            print()
        return

    # --file: text dump of single review file + tests
    if has_file:
        filepath, feature = _resolve_file_arg()
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        tests = tests_by_feature.get(feature, [])
        test_names = [t["name"] for t in tests]
        filename = os.path.basename(filepath)

        print(f"=== REVIEW FILE: {filename} ===")
        print(f"Feature: {feature}")
        print(f"Test count: {len(tests)}")
        print(f"Test names: {', '.join(test_names)}")
        print()
        print("--- REVIEW FILE CONTENT ---")
        print(content)
        print("--- END REVIEW FILE CONTENT ---")
        print()
        print("--- TESTS ---")
        if tests:
            print(format_tests(tests))
        else:
            print("(no tests found)")
        print("--- END TESTS ---")
        return

    # --feature: text dump of tests for a feature
    if "--feature" in sys.argv:
        idx = sys.argv.index("--feature")
        if idx + 1 >= len(sys.argv):
            print("ERROR: --feature requires a name", file=sys.stderr)
            sys.exit(1)
        feature_name = sys.argv[idx + 1]
        tests = tests_by_feature.get(feature_name, [])
        print(f"feature: {feature_name}")
        print(f"test_count: {len(tests)}")
        print()
        if tests:
            print(format_tests(tests))
        else:
            print("(no tests found)")
        return

    print("Usage: python scripts/check_coverage.py --feature <name>", file=sys.stderr)
    print("       python scripts/check_coverage.py --file <review-file.md>", file=sys.stderr)
    print("       python scripts/check_coverage.py --list", file=sys.stderr)
    print("       python scripts/check_coverage.py --json", file=sys.stderr)
    print("       python scripts/check_coverage.py --json --file <review-file.md>", file=sys.stderr)
    sys.exit(1)


if __name__ == "__main__":
    main()
