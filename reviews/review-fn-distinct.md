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
- ✅ Distinct removes duplicate strings from a collection (testExpressions)
- ✅ Distinct on collection with no duplicates (testDistinct4)
- ✅ Distinct on extracted properties with count verification (testDistinct5, testDistinct6)

**Gaps:**
- ❌ No test for empty input returning empty

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testDistinct4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDistinct5 | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| testDistinct6 | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| testExpressions | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 20/24 (83%) — 4 tests × 6 engines

2 test(s) fail in only one engine, suggesting engine-specific implementation issues rather than problems with the tests or specification. 1 test(s) fail in multiple (but not all) engines, which may indicate differing interpretations of the specification.
