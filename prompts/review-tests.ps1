# Script to review AI-generated tests for quality, accuracy, and style.
#   Picks a test with the "AI:" prefix in its description, locates the
#   corresponding review file, then evaluates the test against the spec,
#   coverage intent, engine results, and style guidelines. Fixes or flags
#   issues found.
#
# Usage: .\prompts\review-tests.ps1
#
$prompt = @"
Review an AI-generated FHIRPath test for quality, accuracy, and style.

The FHIRPath specification is at: C:\git\hl7\FHIRPath\input\pages\index.md
The test XML file is at: ..\fhir-test-cases\r5\fhirpath\tests-fhir-r5.xml

## Step 1: SELECT an AI-generated test

Search the test XML file for ``<test`` elements whose ``description`` attribute starts with ``AI:``.
Pick ONE test to review. Prefer a random-ish selection — don't always pick the first one.
Record the test's ``name``, ``testing`` attribute, ``description``, ``expression``, expected ``output``(s), and any other attributes (``invalid``, ``inputfile``, ``mode``, etc.).

If no AI-prefixed tests exist, write a ``stop.md`` file and STOP (see Error Handling below).

## Step 2: LOCATE the review file

Use the test's ``testing`` attribute to find the corresponding review file:
1. Run ``python scripts/check_coverage.py --list`` and find the feature matching the ``testing`` value.
2. Open the review file indicated in the output (e.g. ``review-fn-startsWith.md``).
3. Read the review file's **Covered:** section to understand the intended purpose of this test — find the covered item that references this test name.
4. Read the **Test Results** table to see how this test performs across engines.

## Step 3: READ the specification

Read the relevant section from the specification file (C:\git\hl7\FHIRPath\input\pages\index.md) using the review file's ``Header in specification:`` field to locate the exact section.
Also read any parent section preamble and cross-referenced sections (e.g. "Singleton Evaluation of Collections", type conversion rules) that apply to this function/operator.

## Step 4: REVIEW the test

Evaluate the test against these criteria:

### 4a. Accuracy against intended purpose
- Does the test actually verify the coverage item it's listed under in the review file?
- Does the expression test the specific behavior described, or does it test something else?
- Could the test pass even if the targeted behavior were implemented incorrectly (false positive)?
- Does the expected output (or ``invalid`` marker) correctly match what the spec requires?

### 4b. Accuracy against the specification
- Is the expected result correct according to the spec?
- Does the expression exercise the exact spec requirement it claims to test?
- Are there edge cases in the spec that the test mishandles?
- If the test expects an error (``invalid``), is that error type (``semantic``, ``syntax``, ``execution``) correct per the spec?

### 4c. Engine failure analysis
- Check the test results across engines. If multiple engines fail this test, investigate:
  - Is the expected output actually wrong?
  - Is there a spec ambiguity that engines interpret differently?
  - Is the expression valid but testing an edge case engines haven't implemented yet?
- A test failing in only one engine likely indicates an engine bug — note but don't change the test.
- A test failing in most/all engines strongly suggests the test itself is wrong — flag for correction.

### 4d. Style conformance
Check these style rules and fix violations:
- **Empty collections:** Use ``{}`` for empty collections, not patterns like ``.where(false)`` or other workarounds that depend on input resources. For example, ``{}.empty()`` is preferred over ``Patient.name.where(false).empty()``.
- **Literal values over input files:** If the test expression doesn't actually need data from an input resource and can work with literal values alone, it should use literals. For example, ``'hello'.startsWith('he')`` doesn't need ``inputfile="patient-example.xml"``.
- **XML escaping:** Verify proper XML escaping — ``&amp;`` for ``&``, ``&lt;`` for ``<``, ``&gt;`` for ``>``.
- **Test name uniqueness:** Confirm the test name is unique across the entire XML file.
- **Description clarity:** The ``AI:`` prefixed description should clearly state what behavior is being verified.

### 4e. Result value verification
- Does the test explicitly verify the correct result value(s), not just that the expression succeeds or errors?
- A test that only checks ``invalid="semantic"`` without also having a companion test that verifies the correct output for valid input is incomplete — flag if the coverage item needs both.
- For tests with ``<output>`` elements: does the expected value actually prove the function works correctly? For example, a test returning ``true`` is only meaningful if a wrong implementation would return ``false`` or empty — not if ``true`` is the trivial/default result.
- Watch for tests that could pass with a no-op implementation (e.g. returning the input unchanged, returning 0, returning empty). The expected output should be a value that only a correct implementation can produce.
- If the test has no ``<output>`` elements (expects empty collection), confirm that empty is genuinely the correct result per the spec, not a sign that the test is failing silently.

### 4f. Spec ambiguity assessment
- If the test touches an area where the spec is ambiguous, vague, or silent, note this.
- Consider whether divergent engine results point to a spec gap rather than engine bugs.

## Step 5: APPLY fixes

If the review identified issues, fix them:

### For test corrections (Steps 4a, 4b, 4d):
- Edit the test in the XML file to fix the expression, expected output, attributes, or style.
- If the test is fundamentally flawed (wrong spec interpretation), rewrite it to correctly test the intended coverage item.
- If the test cannot be salvaged (e.g. it tests something inherently untestable), remove it from the XML.

### For no issues found:
If the test passes all review criteria, change the ``AI:`` prefix to ``HR:`` in its ``description`` attribute in the XML to mark ready for human review. The description text should remain unchanged otherwise.

## Summary output

At the end, print a brief summary:
- Test reviewed: ``<test name>`` (``<testing>`` attribute)
- Verdict: PASS (no issues, AI: prefix removed) / FIXED (issues corrected) / REMOVED (test was unsalvageable)
- Changes made: list any edits to the XML or review file

## Step 6: LOG findings

Append a markdown formatted summary of the review to ``expression-reviews.md`` using this template:

``````markdown
### <<function name>> - <<test case name>>
```fhirpath
<<fhirpath expression>>
```
Changed to: (where expression is changed, otherwise omit this line)
```fhirpath
<<fhirpath expression>>
```
<<review summary>>
``````

Where:
- ``<<function name>>`` is the ``testing`` attribute value (e.g. ``startsWith``, ``aggregate``)
- ``<<test case name>>`` is the test's ``name`` attribute (e.g. ``testStartsWith15``)
- ``<<fhirpath expression>>`` is the test's ``<expression>`` content (unescaped from XML)
- ``<<review summary>>`` is a brief description of findings: verdict (PASS/FIXED/REMOVED), what was checked, any issues found and how they were resolved, or confirmation that the test is correct

If ``expression-reviews.md`` does not exist yet, create it with a heading ``# Expression Reviews`` before the first entry.

## Error Handling

If ANY of the following occur, write a file called ``stop.md`` in the repository root with the details and then STOP immediately:

1. **No AI tests to review** — if no tests with ``AI:`` prefix descriptions exist in the XML, write stop.md with the message "No AI-generated tests remaining to review."
2. **Review file not found** — if the ``testing`` attribute doesn't match any review file, write stop.md explaining which test and testing value could not be matched.
3. **Unexpected errors** — if you encounter invalid/malformed XML, file-not-found errors, script failures, or any other unexpected error, write stop.md with the error details.

The stop.md format:
``````markdown
# Stop
Date: <timestamp>
Iteration stopped due to: <reason>

## Details
<detailed explanation of what happened, which files were involved, and any error messages>
``````
"@

copilot --model claude-opus-4.6 --prompt $prompt --allow-tool "shell(python)" --add-dir C:\git\hl7\fhir-test-cases\r5 --allow-all
