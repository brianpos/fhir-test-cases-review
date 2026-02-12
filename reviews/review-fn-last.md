## Review `last() : any`
Name: last
Date: 2026-02-11
Test Count: 1

### Specification Extract 
Header in specification: last() : any

Returns a collection containing only the last item in the input collection. Will return an empty collection if the input collection has no items.

### Example(s) from Specification
_No examples found in specification._

### Coverage
1 tests found for `last` (testFirstLast2).

**Covered:**
- ✅ Returns last item from a multi-item collection (testFirstLast2)

**Gaps:**
- ❌ Empty input collection returning empty

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testFirstLast2 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 5/6 (83%) — 1 tests × 6 engines

1 test(s) fail in only one engine, suggesting engine-specific implementation issues rather than problems with the tests or specification.
