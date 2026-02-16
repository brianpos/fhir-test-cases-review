# Analyze test coverage for review files and write back results.
# Usage: .\prompts\review-files-check-coverage.ps1
#   Processes all review files by default.
#   To target specific files, edit the prompt below to add a filter.
#
$prompt = @"
For each review file in the reviews folder, analyze test coverage against the specification:

The FHIRPath specification is at: C:\git\hl7\FHIRPath\input\pages\index.md

1. EXTRACT: Run `python scripts/check_coverage.py --file <review-file.md>` to get the matching tests and existing analysis for a review file. The output includes a `spec_header` field — use this to locate the relevant section in the specification file.
2. READ SPEC: Read the relevant section from the specification file (index.md). Also read the parent section heading and any preamble text that applies to the group of functions/operators this feature belongs to (e.g. the "Boolean logic" preamble applies to all of and/or/xor/implies/not). Follow any cross-references to related sections (e.g. "Singleton Evaluation of Collections").
3. ANALYZE: Compare the specification requirements against the test expressions. If the review file already has Covered/Gaps content from a previous analysis, review it and update as needed (add missing items, remove incorrect ones, refine descriptions) rather than regenerating from scratch. Determine:
   - Which spec requirements are covered by at least one test
   - Which requirements have no test coverage (gaps)
   - Which requirements are inherently untestable via FHIRPath expressions (e.g. logging behavior, UI concerns)
   - If any of the expressions fail on multiple engines (particularly those marked with a description with a prefix "AI:"):
      * Inspect the test expression for accuracy against what it is supposed to be testing
      * If the test is valid but fails across multiple engines, this may indicate a spec ambiguity or an issue with the test itself rather than an engine bug.
      * If it passes on most engines, this may indicate an engine-specific bug, or specification ambiguity.
      * Tag the summary with a note about any notable failure patterns, but do not name specific engines in the summary text.
      * Tag the tests coverage entry with the ⚠️ prefix and summarize this analysis and prefix with SPEC AMBIGUITY/TEST ISSUE if relevant.
   - A brief overall summary of the function's test status (failure patterns, engine-specific issues, etc.)
   - Whether the function should be marked as fully reviewed (no gaps AND 100% pass rate)

   Analysis guidelines:
   - Treat each distinct sentence/clause in the specification as a separate requirement to verify
   - A test only covers a requirement if it specifically exercises that exact behavior (e.g. a test for type errors does NOT cover the "multiple items" error requirement — these are different conditions)
   - Check that each spec requirement has at least one test that would fail if that requirement were implemented incorrectly
   - Tests that verify additional behaviors beyond the spec (e.g. edge cases, type safety) can be listed as covered items too

   Pay close attention to these cross-cutting concerns — check whether each is specified and tested:
   - Collection handling: what happens with multiple items in input? Is an error required?
   - Empty inputs: behavior when input collection or arguments are empty
   - Type handling: implicit and explicit type conversions across expected types (per Singleton Evaluation rules)
   - Error conditions: all error conditions mentioned in the spec must have corresponding tests

4. WRITE BACK: Produce a JSON object with the analysis and write it back using `python scripts/review_set_covered_and_gaps.py --json-file <path>`.

The JSON format for step 4 is:
{
  "filename": "review-fn-example.md",
  "covered": [
    "Brief description of covered spec requirement (testName1, testName2)"
  ],
  "gaps": [
    "Brief description of spec requirement with no test coverage"
  ],
  "untestable": [
    "Brief description of spec requirement that cannot be verified via FHIRPath expressions"
  ],
  "summary_text": "Brief overall assessment of test status and any notable failure patterns.",
  "reviewed": false
}

Field details:
- covered: plain text description only (no ✅/❌/⚠️ prefixes — the script adds these automatically). Each item references relevant test name(s) in parentheses.
- gaps: plain text description only (no prefixes). Briefly describe what's missing.
- untestable: plain text description only (no prefixes). Spec requirements that cannot be verified via FHIRPath test expressions (e.g. logging behavior, UI concerns). These appear under **Covered:** with a ⚠️ marker. Do NOT list these as gaps.
- summary_text: descriptive text placed after the **Summary:** statistics line:
    * Focus on engine consistency and failure pattern analysis only
    * **NEVER name specific engines** — describe patterns generically (e.g. "fails in 3 engines", "one engine reports N/A", "most engines pass")
    * Do not repeat coverage gaps (already listed above in the review file)
    * N/A test results indicate that a feature has not been implemented at all in an engine, which is a different issue than a failed test result that indicates an attempted implementation with a bug or spec misinterpretation.
    * If tests fail, assess whether the pattern suggests engine-specific bugs (fails in one engine only), test issues (fails across most engines), or spec ambiguity (mixed results)
    * Leave empty string if all tests pass and nothing is notable
    * BAD examples (naming engines):
      - "testAggregate5 fails in Firely, Java, Helios. Aidbox reports N/A for all tests."
      - "testPlusOverflow1 fails all 8 engines. fhirpath.js and AtomicEHR fail all date/time arithmetic tests."
      - "from-zulip-1 fails on AtomicEHR-0.0.5 only, likely an engine bug."
    * GOOD examples (generic patterns — use this style):
      - "Two tests using $index and outer-context init fail in 3 engines, suggesting incomplete support for newer aggregate features."
      - "preserveOrder parameter test fails in 5 of 8 engines, likely because the STU parameter is not yet widely implemented. Two other tests each fail in 1 engine only."
      - "Integer underflow detection fails universally. Quantity subtraction with different units fails in 6 of 8 engines, need to investigate test accuracy/specification clarity. Time wrapping past midnight fails in 3 engines."
      - "Extended string representation tests fail consistently on 2 engines. Case-insensitive tests fail on 2-3 engines."
- reviewed: set to true ONLY when gaps is empty AND all tests pass on all engines (100% pass rate). Otherwise false.

Save any intermediate JSON files in the `temp` directory.

Python scripts available in the scripts directory:
- check_coverage.py: extracts FHIRPath tests for coverage analysis. Use --feature <name> or --file <review.md> for text output, --list for feature summary, --json for batch JSON (all files or single with --file).
- review_set_covered_and_gaps.py: updates Covered/Gaps sub-sections, summary text, and readme Reviewed column. Preserves count/names line and test results table. Input JSON: {"filename", "covered", "gaps", "summary_text" (optional), "reviewed" (optional)}.
- fhirpath_utils.py: shared utilities module used by the above scripts.
"@

copilot --model claude-opus-4.6 --prompt $prompt --allow-tool "shell(python)" --allow-all
