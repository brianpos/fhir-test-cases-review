## Review `exclude(other) : collection`
Name: exclude
Date: 2026-02-11
Test Count: 4

### Specification Extract 
Header in specification: exclude(other: collection) : collection

Returns the set of items that are not in the `other` collection. Duplicate items will not be eliminated by this function, and order will be preserved.

e.g. `(1 | 2 | 3).exclude(2)` returns `(1 | 3)`.

### Example(s) from Specification
_No examples found in specification._

### Coverage
4 tests found for `exclude` (testExclude1, testExclude2, testExclude3, testExclude4).

**Covered:**
- ✅ Excluding items present in other collection (testExclude1)
- ✅ Excluding when no items match other collection (testExclude2)
- ✅ Excluding empty collection leaves input unchanged (testExclude3)
- ✅ Duplicate items preserved after exclude (testExclude4)

**Gaps:**
- ❌ No test for empty input collection

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testExclude1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testExclude2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testExclude3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testExclude4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 24/24 (100%) — 4 tests × 6 engines

All tests pass across all engines.
