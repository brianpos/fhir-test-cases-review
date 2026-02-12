## Review `empty() : Boolean`
Name: empty
Date: 2026-02-11
Test Count: 1

### Specification Extract 
Header in specification: empty() : Boolean

Returns `true` if the input collection is empty (`{ }`) and `false` otherwise.

### Example(s) from Specification
_No examples found in specification._

### Coverage
1 tests found for `empty` (testEmpty).

**Covered:**
- ✅ Empty returns true for element with no items (testEmpty)

**Gaps:**
- ❌ No test for non-empty collection returning false

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testEmpty | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 6/6 (100%) — 1 tests × 6 engines

All tests pass across all engines.
