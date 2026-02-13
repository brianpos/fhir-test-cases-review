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
- ✅ Returns all but the first item in input collection (testTail1, testTail2)

**Gaps:**
- ❌ Empty input collection returns empty
- ❌ Single item input collection returns empty

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testTail1 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testTail2 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 10/12 (83%) — 2 tests × 6 engines

testTail1 and testTail2 each fail in 1 engine, suggesting engine-specific bugs.
