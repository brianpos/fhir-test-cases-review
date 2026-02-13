# Copilot Instructions — fhir-test-cases-review

## Project Overview

This repository contains **AI-generated, human-reviewed analyses** of FHIRPath R5 unit tests from [fhir-test-cases](https://github.com/FHIR/fhir-test-cases). Each review file evaluates test coverage for a specific FHIRPath function or operator against its specification, and tracks cross-engine compatibility across the tested implementations.

## Repository Structure

| Path | Purpose |
|---|---|
| `reviews/` | Individual review files (`review-fn-*.md`, `review-op-*.md`, etc.) — one per function/operator |
| `scripts/` | Python scripts for batch processing reviews |
| `prompts/` | PowerShell prompts for running batch operations via Copilot CLI |
| `readme.md` | Summary tables linking all reviews with check counts and pass rates |
| `test-plan.md` | Master test plan with coverage tracking |

## External Dependencies (local paths used by scripts)

- **FHIRPath spec source:** `C:\git\hl7\FHIRPath\input\pages\index.md`
- **Function/operation lists:** `C:\git\hl7\FHIRPath\functions-review.md`, `C:\git\hl7\FHIRPath\operations-review.md`
- **Test XML:** `../fhir-test-cases/r5/fhirpath/tests-fhir-r5.xml` (sibling repo, cloned alongside this project)
- **Engine results:** `C:\git\Production\fhirpath-lab\static\results\` (JSON files listed in `outputs.txt`, others are older versions and should be ignored)

## Review File Format

Every review file follows the template in [scripts/review-template.md](scripts/review-template.md):

```markdown
## Review << Feature Description >>
Name: << feature name as found in test `testing` attribute, and summary table >>
Date: << review date >>
Test Count: << number of tests >>

### Specification Extract
Header in specification: << exact header text from index.md that matches the function/operator/feature being reviewed >>
<< Extract markdown from the specification, and copy here - local copy to reduce context size for processing >>

### Example(s) from Specification
<< Where the specification has examples, copy those here >>

### Coverage
<< `n` tests found (comma seperated list of tests). >>

**Covered:**
- << ✅ Feature tested (testName) >>

**Gaps:**
- << ❌ component of feature not covered by a test >>

### Test Results

<< Test results table >>

**Summary:** n/total (%) — x tests × y engines

<< overall function status summary >>
```

**Naming conventions:**
- Functions: `review-fn-<name>.md` (e.g., `review-fn-startsWith.md`)
- Operators: `review-op-<name>.md` (e.g., `review-op-equals.md`)
- Other features: `review-<feature>.md` (e.g., `review-indexer.md`, `review-polarity.md`)

## Key Scripts

Prompts are run via the Copilot CLI (`copilot` command) with Claude — the `.ps1` files in `prompts/` contain prompts, not traditional scripts. The Python scripts in `scripts/` can also be run directly:

| Script | Purpose |
|---|---|
| `fhirpath_utils.py` | Shared utilities: constants, XML parsing (`_iter_tests`, `load_tests_by_testing`, `load_test_names_by_testing`), review-file helpers (`get_feature_name_from_review`), and readme table helpers (`update_summary_table`) |
| `review_set_all_testnames_and_count.py` | Updates `Test Count:` header and coverage line (count + test names in XML document order) in all review files |
| `check_coverage.py` | Extracts FHIRPath tests for coverage analysis. Use `--feature <name>` or `--file <review.md>` for text output, `--list` for feature summary, `--json` for batch JSON |
| `review_set_covered_and_gaps.py` | Updates Covered/Gaps sub-sections, optional summary text after the Summary line, and optional Reviewed column in `readme.md`. Input via `--stdin` or `--json-file` |
| `update_test_results.py` | Reads engine result JSON files, updates the `### Test Results` table and `**Summary:**` line in each review file, and updates the `# Checks`, `Gaps`, and `Reviewed` columns in `readme.md` |


## Summary Table Conventions (readme.md)

- **# Checks**: `N (P%)` — N tests directly targeting this feature, P% passing across all engines
- **Gaps**: Count of `- ❌` gap lines in the review file's `**Gaps:**` section (empty when 0)
- **Reviewed ✅**: Only set when coverage has no gaps AND all tests pass on all engines; cleared automatically by `update_test_results.py` if gaps exist
- **Filename**: Links to the review file in `reviews/`
- Tables are grouped by FHIRPath spec sections (5.1–5.11, 6.1–6.9, 7, 10.2)
- and can use the Function/operation lists mentioned above for completeness (to review when updating/refreshing the table contents when new functions/operators are added to the spec)


## Workflow for Adding/Updating a Review

1. Ensure the review file exists (create from template if not)
2. Fill spec content from `FHIRPath/input/pages/index.md` — match the `Header in specification:` field to the spec heading
3. Run coverage analysis against `tests-fhir-r5.xml` using the `testing` attribute to match tests to match against the name 
4. Read engine results file(s) to populate the Test Results table
5. Update `readme.md` summary row with check count, pass rate, and reviewed status


## unit Test XML Schema notes
The XML namespace is `http://hl7.org/fhirpath/tests`. Hierarchy: `<tests>` → `<group>` → `<test>`.

```
<tests name? version? versionTo? description? reference?>
  <notes>?                           <!-- string -->
  <group name? version? versionTo? description? reference?>+
    <notes>?                         <!-- string -->
    <test name? testing? inputfile? mode? version? versionTo? description?
          reference? predicate? ordered? skipStaticCheck?>+
      <expression invalid?>          <!-- string; required -->
      <output type>*                 <!-- string; 0..* -->
      <notes>?                       <!-- string -->
    </test>
  </group>
</tests>
```

**Enumerations:**
- `expression/@invalid` (`InvalidType`): `false`, `true`, `syntax`, `semantic`, `execution`
- `output/@type` (`OutputType`, required): `boolean`, `code`, `date`, `dateTime`, `decimal`, `integer`, `id`, `Quantity`, `string`, `time`
- `test/@mode` (`ModeType`): `strict`, `lenient`, `lenient/polymorphics`, `element`, `cda`, `tx`

#### XML test structure
Tests are organized as `<tests>` → `<group>` → `<test>`. Find the appropriate group for the function/operator you're testing, or create a new `<group>` if one doesn't exist:

```xml
<group name="testStartsWith">
  <test name="testStartsWith1" testing="startsWith" inputfile="patient-example.xml">
    <expression>'12345'.startsWith('2')</expression>
    <output type="boolean">false</output>
  </test>
</group>
```

#### Required test attributes
- `name` — unique identifier across the entire file (e.g. `testStartsWith1`, `defineVariable8`)
- `testing` — the function/operator under test (e.g. `startsWith`, `=`, `+`, `defineVariable`). This is how tests are categorized; 116 distinct values currently exist
- `inputfile` — reference to a fixture file in `r5/` (required for most tests)
  - Available input files: `patient-example.xml`, `observation-example.xml`, `questionnaire-example.xml`, `valueset-example-expansion.xml`, `patient-example-name.xml`, `parameters-example-types.xml`, `ccda.xml`, `patient-example-period.xml`, `explanationofbenefit-example.json`, `appointment-examplereq.json`, `diagnosticreport-eric.json`, `patient-container-example.json`, `codesystem-example.xml`, `conceptmap-example.xml`, `patient-name-extensions.json`

#### Expression element
- Normal test: `<expression>Patient.name.exists()</expression>`
- Expected failure: `<expression invalid="semantic">...</expression>` — values: `false`, `true`, `syntax`, `semantic`, `execution`

#### Output elements
- One `<output>` per expected result item, in order: `<output type="boolean">true</output>`
- Valid types: `boolean`, `code`, `date`, `dateTime`, `decimal`, `integer`, `id`, `Quantity`, `string`, `time`
- No `<output>` elements = expression expected to return empty collection `{}`
- Multiple `<output>` elements = expression returns a multi-item collection (order matters)

#### Optional test attributes
- `mode` — evaluation context: `strict` (choice types use base name like `Patient.deceased`), `lenient` (allows `Patient.deceasedBoolean`), `lenient/polymorphics` (lenient + polymorphic path resolution like `Observation.valueQuantity`), `element` (invariant-style evaluation from element context), `cda` (CDA document), `tx` (needs terminology services via `%terminologies`)
- `description` — human-readable description of what's being tested
- `ordered` — `true`/`false` whether output order must match (default: ordered)
- `skipStaticCheck` — `true` to bypass static type checking
- `predicate` — `true` if the test represents a predicate expression
- `version` / `versionTo` — FHIRPath spec version range the test applies to
- `reference` — URI reference to the specification area under test

#### XML escaping reminders
FHIRPath uses `&` for string concatenation — in XML this must be `&amp;`:
```xml
<expression>Patient.id &amp; '-' &amp; Patient.name.first().family</expression>
```
Similarly: `<` → `&lt;`, `>` → `&gt;` in expressions.

#### Adding a new test — checklist
1. Identify the function/operator and find its `<group>` (search for `group name=`) - use existing groups when possible, or create a new one if it doesn't exist (e.g. `startsWith` for `startsWith` function tests)
2. Choose a unique `name` — follow the group's naming pattern (e.g. `testStartsWith14`)
3. Set `testing` to match the function being tested
4. Pick an appropriate `inputfile` from the available fixtures
5. Write the `<expression>` with proper XML escaping
6. Add `<output>` elements for each expected result (or none for empty result)
7. For expected-failure tests, add `invalid="semantic"` (or `syntax`/`execution`) on `<expression>` and omit `<output>`

### Naming conventions
- Resources: `{resourcetype}-{qualifier}.{json|xml}` (e.g., `patient-good.json`, `bundle-slice-bad1.xml`), use existing fixtures when possible
- Use `-good`/`-bad` suffixes to indicate expected validation outcome
- test names should be unique across the entire file, and follow the pattern of existing tests in the same group (e.g. `testStartsWith1`, `testStartsWith2`, etc.) and should be descriptive enough to indicate what's being tested (e.g. `testStartsWith14` could be `testStartsWith14_caseInsensitive` if testing case sensitivity, but keep brief)


## Important Notes

- The `testing` attribute in the test XML (e.g., `testing="startsWith"`) is the key that links tests to review files
- The test XML at `tests-fhir-r5.xml` is the **single source of truth** for FHIRPath tests; R4 copies exist for distribution only
- Engine test results come from [fhirpath-lab](https://dev.fhirpath-lab.com/FhirPath-engines): Aidbox, fhirpath.js, Firely, Helios, Ignixa, Java
- When a test fails in only one engine, it suggests an engine bug rather than a test/spec issue
- If creating intermediate datafile during processing, create these in the `temp` directory which is excluded from accidental inclusion in version control