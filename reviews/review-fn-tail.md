## Review `tail() : collection`
Name: tail
Date: 2026-02-11
Test Count: 2

### Specification Extract 
Header in specification: tail() : collection

Returns a collection containing all but the first item in the input collection. Will return an empty collection if the input collection has no items, or only one item.

### Example(s) from Specification
_No examples found in specification._

### Coverage

2 tests found for `tail` (testTail1, testTail2).

**Covered:**
- ✅ Returns all but first item from a multi-item collection (testTail1, testTail2)

**Gaps:**
- ❌ Empty input collection returning empty is not tested
- ❌ Single-item input collection returning empty is not tested

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testTail1 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testTail2 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 10/12 (83%) — 2 tests × 6 engines

2 test(s) fail in only one engine, suggesting engine-specific implementation issues rather than problems with the tests or specification.
