## Review `first() : any`
Name: first
Date: 2026-02-11
Test Count: 1

### Specification Extract 
Header in specification: first() : any

Returns a collection containing only the first item in the input collection. This function is equivalent to `item[0]`, so it will return an empty collection if the input collection has no items.

### Example(s) from Specification
_No examples found in specification._

### Coverage
1 tests found for `first` (testFirstLast1).

**Covered:**
- ✅ Returns first item from non-empty collection (testFirstLast1)

**Gaps:**
- ❌ Empty input returns empty collection
- ❌ Equivalence to item[0]

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testFirstLast1 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 5/6 (83%) — 1 tests × 6 engines

One engine fails, suggesting an engine-specific bug.
