## Review `count() : Integer`
Name: count
Date: 2026-02-11
Test Count: 5

### Specification Extract 
Header in specification: count() : Integer

Returns the integer count of the number of items in the input collection. Returns 0 when the input collection is empty.

### Example(s) from Specification
_No examples found in specification._

### Coverage
5 tests found for `count` (testCount1, testCount2, testCount3, testCount4, testWhere1).

**Covered:**
- ✅ Returns integer count of items in a multi-item collection (testCount1, testCount2, testWhere1)
- ✅ Returns count of 1 for a single item (testCount3, testCount4)

**Gaps:**
- ❌ Returns 0 when the input collection is empty

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testCount1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testCount2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testCount3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testCount4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testWhere1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 30/30 (100%) — 5 tests × 6 engines
