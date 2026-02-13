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
  "summary_text": "Brief overall assessment of test status and any notable failure patterns.",
  "reviewed": false
}

Field details:
- covered: plain text description only (no ✅/❌ prefixes — the script adds these automatically). Each item references relevant test name(s) in parentheses.
- gaps: plain text description only (no ✅/❌ prefixes). Briefly describe what's missing.
- summary_text: descriptive text placed after the **Summary:** statistics line. Focus on engine consistency and failure pattern analysis only — do not repeat coverage gaps (already listed above in the review file). If tests fail, assess whether the pattern suggests engine-specific bugs (fails in one engine only), test issues (fails across most engines), or spec ambiguity (mixed results). Do not name specific engines. Leave empty string if all tests pass and nothing is notable.
- reviewed: set to true ONLY when gaps is empty AND all tests pass on all engines (100% pass rate). Otherwise false.

Save any intermediate JSON files in the `temp` directory.

Python scripts available in the scripts directory:
- check_coverage.py: extracts FHIRPath tests for coverage analysis. Use --feature <name> or --file <review.md> for text output, --list for feature summary, --json for batch JSON (all files or single with --file).
- review_set_covered_and_gaps.py: updates Covered/Gaps sub-sections, summary text, and readme Reviewed column. Preserves count/names line and test results table. Input JSON: {"filename", "covered", "gaps", "summary_text" (optional), "reviewed" (optional)}.
- fhirpath_utils.py: shared utilities module used by the above scripts.
"@

copilot --model claude-opus-4.6-fast -i $prompt --allow-tool "shell(python)"
