"""Update the Covered/Gaps sub-sections and optional summary text in review files.

Preserves the count/names line (managed by review_set_all_testnames_and_count.py)
and the ### Test Results table and **Summary:** statistics line (managed by
update_test_results.py).

Optionally updates:
  - Descriptive text after the **Summary:** line in the review file
  - The Reviewed column in readme.md

Usage:
    echo '{"filename": "...", "covered": [...], "gaps": [...]}' | python scripts/review_set_covered_and_gaps.py --stdin
    python scripts/review_set_covered_and_gaps.py --json-file <path>

Input JSON format (single item or array):
    {
        "filename": "review-fn-abs.md",
        "covered": [
            "Absolute value of negative Integer returns positive Integer (testAbs1)",
            "Absolute value of negative Decimal returns positive Decimal (testAbs2)"
        ],
        "gaps": [
            "Absolute value of positive input returns same value",
            "Long input type not tested"
        ],
        "untestable": [
            "Diagnostic log output behavior is inherently untestable via expressions"
        ],
        "summary_text": "1 test fails in only one engine, suggesting an engine bug.",
        "reviewed": false
    }

Optional fields:
  - summary_text: replaces descriptive text after the **Summary:** line
                  (the statistics line itself is preserved)
  - reviewed: if true, sets Reviewed column to ✅ in readme.md;
              if false, clears it. Omit to leave unchanged.
"""
import json
import os
import re
import sys

from fhirpath_utils import TESTS_DIR, update_summary_table

# Matches the count/names line: "4 tests found for `abs` (test1, test2)."
COVERAGE_COUNT_RE = re.compile(r"^\d+ tests? found for `[^`]+`")

README_FILE = "readme.md"


def update_covered_and_gaps(filename, covered, gaps, untestable=None, summary_text=None):
    fp = os.path.join(TESTS_DIR, filename)
    with open(fp, "r", encoding="utf-8") as f:
        content = f.read()

    # Find ### Coverage section
    cov_idx = content.find("### Coverage")
    if cov_idx < 0:
        print(f"WARNING: No ### Coverage section in {filename}", file=sys.stderr)
        return

    # Find ### Test Results section (to preserve it)
    tr_idx = content.find("### Test Results", cov_idx + 1)

    # Extract the coverage section content
    if tr_idx >= 0:
        cov_section = content[cov_idx:tr_idx]
        post = content[tr_idx:]
    else:
        cov_section = content[cov_idx:]
        post = ""

    # Find and preserve the count/names line within the coverage section
    cov_lines = cov_section.split("\n")
    count_line = None
    for line in cov_lines:
        if COVERAGE_COUNT_RE.match(line):
            count_line = line
            break

    # Build covered section
    covered_text = "**Covered:**\n"
    if covered:
        for item in covered:
            covered_text += f"- ✅ {item}\n"
    if untestable:
        for item in untestable:
            covered_text += f"- ⚠️ {item}\n"
    if not covered and not untestable:
        covered_text += "- (none)\n"

    # Build gaps section
    gaps_text = "**Gaps:**\n"
    if gaps:
        for item in gaps:
            gaps_text += f"- ❌ {item}\n"
    else:
        gaps_text += "- (none)\n"

    # Assemble the new coverage section
    pre = content[:cov_idx].rstrip()
    new_cov = "### Coverage\n"
    if count_line:
        new_cov += count_line + "\n"
    new_cov += "\n" + covered_text + "\n" + gaps_text

    # Handle summary_text: replace descriptive text after **Summary:** line
    if summary_text is not None and post:
        summary_idx = post.find("**Summary:**")
        if summary_idx >= 0:
            # Find the end of the **Summary:** line
            eol = post.find("\n", summary_idx)
            if eol >= 0:
                summary_line = post[summary_idx:eol]
                # Replace everything after the summary line with our text
                post = post[:summary_idx] + summary_line + "\n"
                if summary_text.strip():
                    post += "\n" + summary_text.strip() + "\n"

    new_content = pre + "\n\n" + new_cov + "\n" + post.lstrip("\n")
    with open(fp, "w", encoding="utf-8") as f:
        f.write(new_content)


def _process_item(item, readme_content):
    """Process a single JSON item, updating review file and readme content.

    Returns updated readme_content.
    """
    filename = item["filename"]
    update_covered_and_gaps(
        filename,
        item.get("covered", []),
        item.get("gaps", []),
        item.get("untestable"),
        item.get("summary_text"),
    )
    print(f"Updated {filename}")

    if "reviewed" in item:
        value = "✅" if item["reviewed"] else ""
        readme_content = update_summary_table(readme_content, filename, "Reviewed", value)
        status = "✅" if item["reviewed"] else "cleared"
        print(f"  Reviewed: {status}")

    return readme_content


def main():
    if "--stdin" in sys.argv:
        data = json.load(sys.stdin)
    elif "--json-file" in sys.argv:
        idx = sys.argv.index("--json-file")
        path = sys.argv[idx + 1]
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        print("Usage: python scripts/review_set_covered_and_gaps.py --stdin", file=sys.stderr)
        print("       python scripts/review_set_covered_and_gaps.py --json-file <path>", file=sys.stderr)
        sys.exit(1)

    items = data if isinstance(data, list) else [data]

    # Check if any item has a "reviewed" field — if so, load readme
    needs_readme = any("reviewed" in item for item in items)
    readme_content = None
    if needs_readme and os.path.exists(README_FILE):
        with open(README_FILE, "r", encoding="utf-8") as f:
            readme_content = f.read()

    for item in items:
        if readme_content is not None:
            readme_content = _process_item(item, readme_content)
        else:
            update_covered_and_gaps(
                item["filename"],
                item.get("covered", []),
                item.get("gaps", []),
                item.get("untestable"),
                item.get("summary_text"),
            )
            print(f"Updated {item['filename']}")

    if needs_readme and readme_content is not None:
        with open(README_FILE, "w", encoding="utf-8") as f:
            f.write(readme_content)
        print("Updated readme.md")


if __name__ == "__main__":
    main()
