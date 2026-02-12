## Review `children() : collection`
Name: children
Date: 2026-02-11
Test Count: 1

### Specification Extract 
Header in specification: children() : collection

Returns a collection with all immediate child nodes of all items in the input collection. Note that the ordering of the children is undefined and using functions like `first()` on the result may return different results on different platforms.

### Example(s) from Specification
_No examples found in specification._

### Coverage
1 tests found for `children` (testRepeat4).

**Covered:**
- ✅ Returns immediate child nodes from a resource (testRepeat4)

**Gaps:**
- ❌ Children of primitive types not tested
- ❌ Empty input collection behavior not tested

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testRepeat4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:**
- Overall pass rate: 6/6 (100%)
- Tests: 1
- All engines pass all tests — fully consistent.
