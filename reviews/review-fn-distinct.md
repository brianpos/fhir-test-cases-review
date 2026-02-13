## Review `distinct() : collection`
Name: distinct
Date: 2026-02-11
Test Count: 4

### Specification Extract 
Header in specification: distinct() : collection

Returns a collection containing only the unique items in the input collection. To determine whether two items are the same, the [equals](#equals) (`=`) operator is used, as defined below.

If the input collection is empty (`{ }`), the result is empty.

Note that the order of items in the input collection is not guaranteed to be preserved in the result.

The following example returns the distinct list of tags on the given Patient:

### Example(s) from Specification
``` fhirpath
Patient.meta.tag.distinct()
```

### Coverage
4 tests found for `distinct` (testExpressions, testDistinct4, testDistinct5, testDistinct6).

**Covered:**
- ✅ Returns collection containing only unique items (testExpressions, testDistinct4)
- ✅ Works with string elements from resource descendants (testDistinct5, testDistinct6)
- ✅ Handles already-distinct collections without change (testDistinct4)

**Gaps:**
- ❌ Empty input returns empty
- ❌ Uses equals (=) operator to determine uniqueness is not explicitly demonstrated
- ❌ Order of items in result is not guaranteed to be preserved (not explicitly tested)

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testExpressions | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| testDistinct4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDistinct5 | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| testDistinct6 | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |

**Summary:** 20/24 (83%) — 4 tests × 6 engines

testExpressions fails in 2 engines; testDistinct5 and testDistinct6 each fail in 1 engine. Failures may indicate differences in how distinctness is evaluated across engines.
