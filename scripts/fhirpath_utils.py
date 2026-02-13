"""Shared utilities for FHIRPath test review scripts.

Provides common constants, XML parsing, and review-file helpers used
across check_coverage, review_set_all_testnames_and_count,
review_set_covered_and_gaps, and update_test_results.
"""

import os
import xml.etree.ElementTree as ET

# Common paths and constants
TESTS_XML = os.path.join("..", "fhir-test-cases", "r5", "fhirpath", "tests-fhir-r5.xml")
TESTS_DIR = "reviews"
NS = {"t": "http://hl7.org/fhirpath/tests"}


def _iter_tests(xml_path=TESTS_XML):
    """Yield each (testing, test_element) pair from the FHIRPath test XML."""
    tree = ET.parse(xml_path)
    root = tree.getroot()
    for group in root.findall(".//t:group", NS):
        for test in group.findall("t:test", NS):
            yield test.get("testing", ""), test


def load_tests_by_testing(xml_path=TESTS_XML):
    """Parse the FHIRPath test XML and return a dict keyed by `testing` value.

    Returns: {testing_value: [list of test dicts]}
    Each test dict has keys: name, testing, description, expression,
    invalid, outputs, inputfile, mode.
    """
    tests_by_feature = {}

    for testing, test in _iter_tests(xml_path):
        expr_elem = test.find("t:expression", NS)
        expression = (expr_elem.text or "") if expr_elem is not None else ""
        invalid = expr_elem.get("invalid", "") if expr_elem is not None else ""
        outputs = []
        for out in test.findall("t:output", NS):
            outputs.append({"type": out.get("type", ""), "value": out.text or ""})

        entry = {
            "name": test.get("name", ""),
            "testing": testing,
            "description": test.get("description", ""),
            "expression": expression,
            "invalid": invalid,
            "outputs": outputs,
            "inputfile": test.get("inputfile", ""),
            "mode": test.get("mode", ""),
        }
        tests_by_feature.setdefault(testing, []).append(entry)

    return tests_by_feature


def load_test_names_by_testing(xml_path=TESTS_XML):
    """Parse the FHIRPath test XML and return a dict of testing value -> [test names].

    Returns: {testing_value: [list of test name strings]}
    """
    tests_by_feature = {}

    for testing, test in _iter_tests(xml_path):
        name = test.get("name", "")
        if testing and name:
            tests_by_feature.setdefault(testing, []).append(name)

    return tests_by_feature


def get_feature_name_from_review(filepath):
    """Extract the Name: field from a review file.

    Returns the feature name string, or None if not found.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("Name:"):
                return line.split(":", 1)[1].strip()
    return None


def update_summary_table(content, review_filename, column, value):
    """Update a column in a markdown summary table row identified by review filename.

    Locates the table row containing `review_filename`, then updates the
    specified column.  Columns are identified by negative offset from the
    right-hand side of the pipe-delimited row so that escaped pipes in
    earlier columns (e.g. the ``|`` union operator) do not cause mis-alignment.

    Supported *column* values and their offsets (from end of ``split('|')``):

    * ``"# Checks"`` — 4th from end
    * ``"Reviewed"`` — 3rd from end

    Args:
        content: Full markdown file text.
        review_filename: Filename to match in the row (e.g. ``"review-fn-empty.md"``).
        column: Column name to update.
        value: New cell text (spaces are added around it automatically).

    Returns:
        Updated content string, or the original content if the row was not found.
    """
    column_offsets = {
        "# Checks": -4,
        "Reviewed": -3,
    }
    if column not in column_offsets:
        raise ValueError(f"Unknown column: {column!r}")

    offset = column_offsets[column]
    lines = content.split("\n")

    for i, line in enumerate(lines):
        if review_filename in line and line.strip().startswith("|"):
            parts = line.split("|")
            idx = len(parts) + offset
            if 0 < idx < len(parts):
                parts[idx] = f" {value} "
                lines[i] = "|".join(parts)
            break

    return "\n".join(lines)


def format_tests(tests):
    """Format test dicts into a readable text block.

    Returns a string with one test per block, separated by blank lines.
    """
    lines = []
    for i, t in enumerate(tests):
        if i > 0:
            lines.append("")
        lines.append(f"name: {t['name']}")
        if t["description"]:
            lines.append(f"description: {t['description']}")
        lines.append(f"expression: {t['expression']}")
        if t["invalid"]:
            lines.append(f"invalid: {t['invalid']}")
        if t["mode"]:
            lines.append(f"mode: {t['mode']}")
        if t["inputfile"]:
            lines.append(f"inputfile: {t['inputfile']}")
        for j, o in enumerate(t["outputs"]):
            lines.append(f"output[{j}]: {o['type']} = {o['value']}")
        if not t["outputs"]:
            lines.append("output: (empty collection)")
    return "\n".join(lines)
