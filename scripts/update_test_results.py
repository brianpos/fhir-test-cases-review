"""
Update test results in review files and readme.md.

Reads engine test result JSON files from the fhirpath-lab results directory,
cross-references them with the FHIRPath test XML, and updates:
  - Each reviews/review-*.md file: replaces the test results table and
    ``**Summary:**`` line, preserving any descriptive text below the summary
  - The readme.md summary tables: ``# Checks`` column

Usage: python scripts/update_test_results.py
"""

import json
import os

from fhirpath_utils import (
    TESTS_DIR,
    load_test_names_by_testing,
    get_feature_name_from_review,
    update_summary_table,
)

RESULTS_DIR = r"C:\git\Production\fhirpath-lab\static\results"
README_FILE = "readme.md"


# ---------------------------------------------------------------------------
# Engine loading
# ---------------------------------------------------------------------------

def load_engines(results_dir):
    """Load engine test results from JSON files listed in outputs.txt.

    Returns:
        (engine_names, engines) where *engine_names* is an ordered list of
        display names and *engines* maps each name to
        ``{test_name: {Result: bool, NotImplemented: bool}}``.
    """
    outputs_path = os.path.join(results_dir, "outputs.txt")
    with open(outputs_path, "r", encoding="utf-8") as f:
        engine_files = [line.strip() for line in f if line.strip()]

    engine_names = []
    engines = {}

    for ef in engine_files:
        path = os.path.join(results_dir, ef)
        if not os.path.exists(path):
            print(f"WARNING: {path} not found, skipping")
            continue
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        display_name = ef.replace(".json", "")
        engine_names.append(display_name)
        test_map = {}
        for group in data.get("Groups", []):
            for tc in group.get("TestCases", []):
                test_map[tc["Name"]] = {
                    "Result": tc.get("Result", False),
                    "NotImplemented": tc.get("NotImplemented", False),
                }
        engines[display_name] = test_map

    return engine_names, engines


# ---------------------------------------------------------------------------
# Results table + statistics
# ---------------------------------------------------------------------------

def _is_na(tr):
    """Return True when a test result dict represents N/A (missing or not implemented)."""
    return tr is None or tr.get("NotImplemented", False)


def build_results_table(test_names, engine_names, engines):
    """Build the markdown results table and per-test analysis.

    Tests are listed in the order given (XML document order).

    Returns:
        (table_lines, total_pass, total_cells, test_analysis)

    *test_analysis* is a list of ``(test_name, fail_count, tested_count, na_count)``
    tuples — one per test.
    """
    header = "| Test | " + " | ".join(engine_names) + " |"
    separator = "|------|" + "|".join(["------"] * len(engine_names)) + "|"
    table_lines = [header, separator]

    total_pass = 0
    total_cells = len(test_names) * len(engine_names)
    test_analysis = []

    for tn in test_names:
        row = f"| {tn} |"
        fails = 0
        tested = 0
        na_count = 0
        for en in engine_names:
            tr = engines[en].get(tn)
            if _is_na(tr):
                row += " N/A |"
                na_count += 1
            elif tr.get("Result", False):
                row += " ✅ |"
                total_pass += 1
                tested += 1
            else:
                row += " ❌ |"
                fails += 1
                tested += 1
        table_lines.append(row)
        test_analysis.append((tn, fails, tested, na_count))

    return table_lines, total_pass, total_cells, test_analysis


# ---------------------------------------------------------------------------
# Review-file update
# ---------------------------------------------------------------------------

def update_review_file(filepath, test_names, engine_names, engines):
    """Replace the results table and **Summary:** line in a review file.

    Only the table rows and ``**Summary:**`` line are rewritten; sections
    before ``### Test Results`` and any descriptive text *after* the summary
    line are left untouched.

    Returns:
        pass_pct for downstream readme updates.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    num_tests = len(test_names)
    num_engines = len(engine_names)

    # Build table and stats
    table_lines, total_pass, total_cells, _analysis = build_results_table(
        test_names, engine_names, engines,
    )
    pass_pct = (total_pass / total_cells * 100) if total_cells > 0 else 0

    summary_line = (
        f"**Summary:** {total_pass}/{total_cells} ({pass_pct:.0f}%) "
        f"— {num_tests} tests × {num_engines} engines"
    )

    # Assemble new table + summary line
    new_section = "### Test Results\n\n"
    new_section += "\n".join(table_lines) + "\n"
    new_section += "\n" + summary_line

    if "### Test Results" in content:
        idx = content.index("### Test Results")
        # Content before the section (keep as-is)
        line_start = content.rfind("\n", 0, idx)
        if line_start == -1:
            line_start = 0
        before = content[:line_start + 1]

        # Preserve text after the **Summary:** line
        after = ""
        summary_idx = content.find("**Summary:**", idx)
        if summary_idx != -1:
            end_of_summary = content.find("\n", summary_idx)
            if end_of_summary != -1:
                after = content[end_of_summary:]  # includes leading newline
        content = before + new_section + after
    else:
        content = content.rstrip() + "\n\n" + new_section + "\n"

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    return pass_pct


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    # 1. Load engine results
    engine_names, engines = load_engines(RESULTS_DIR)
    print(f"Loaded {len(engines)} engines: {engine_names}")

    # 2. Load XML testing-attribute → test-name mapping
    testing_map = load_test_names_by_testing()
    print(f"Found {len(testing_map)} testing attributes")

    # 3. Enumerate review files
    review_files = sorted(os.listdir(TESTS_DIR))
    print(f"Found {len(review_files)} review files\n")

    # 4. Read readme once, update in memory, write back at the end
    with open(README_FILE, "r", encoding="utf-8") as f:
        readme_content = f.read()

    for rf in review_files:
        if not rf.endswith(".md"):
            continue

        filepath = os.path.join(TESTS_DIR, rf)
        func_name = get_feature_name_from_review(filepath)
        if not func_name:
            print(f"WARNING: No Name found in {rf}, skipping")
            continue

        test_names = testing_map.get(func_name, [])
        num_tests = len(test_names)

        if num_tests > 0:
            pass_pct = update_review_file(
                filepath, test_names, engine_names, engines,
            )
        else:
            pass_pct = 0

        # Update readme # Checks column
        checks_val = f"{num_tests} ({pass_pct:.0f}%)" if num_tests > 0 else "0"
        readme_content = update_summary_table(readme_content, rf, "# Checks", checks_val)

        status = f"{num_tests} tests, {pass_pct:.0f}% pass" if num_tests > 0 else "0 tests"
        print(f"  {rf}: {func_name} -> {status}")

    # 5. Write updated readme
    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(readme_content)

    print("\nDone!")


if __name__ == "__main__":
    main()
