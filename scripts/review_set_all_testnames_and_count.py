"""Update test count and test names in review files.

For each review file, updates two locations:
  1. Header:   Test Count: N
  2. Coverage:  N tests found for `feature` (test1, test2, ...).

Both are set to the actual count from the test XML. The coverage line
also includes the comma-separated list of test names (in XML document order).

Usage:
    python scripts/review_set_all_testnames_and_count.py
"""

import os
import re

from fhirpath_utils import TESTS_DIR, load_test_names_by_testing, get_feature_name_from_review

# Matches: "Test Count: 14" or "Test Count: 0"
HEADER_RE = re.compile(r"^Test Count: \d+$")

# Matches: "14 tests found for `startsWith` (names...)." or "0 tests found for `startsWith`."
COVERAGE_RE = re.compile(r"^\d+ tests? found for `[^`]+`")


def main():
    tests_by_feature = load_test_names_by_testing()

    files = sorted(os.listdir(TESTS_DIR))
    updated = 0
    for f in files:
        if not f.endswith(".md"):
            continue
        fp = os.path.join(TESTS_DIR, f)
        feature = get_feature_name_from_review(fp)
        if not feature:
            continue
        test_names = tests_by_feature.get(feature, [])
        count = len(test_names)

        with open(fp, "r", encoding="utf-8") as fh:
            content = fh.read()

        lines = content.split("\n")
        changed = False
        for i, line in enumerate(lines):
            # Update header Test Count line
            if HEADER_RE.match(line):
                new_line = f"Test Count: {count}"
                if line != new_line:
                    lines[i] = new_line
                    changed = True
                continue

            # Update coverage count + names line
            if COVERAGE_RE.match(line):
                if count == 0:
                    new_line = f"0 tests found for `{feature}`."
                else:
                    names_str = ", ".join(test_names)
                    new_line = f"{count} tests found for `{feature}` ({names_str})."
                if line != new_line:
                    lines[i] = new_line
                    changed = True
                continue

        if changed:
            with open(fp, "w", encoding="utf-8") as fh:
                fh.write("\n".join(lines))
            updated += 1
            print(f"Updated: {f}")

    print(f"\nTotal updated: {updated}")


if __name__ == "__main__":
    main()
