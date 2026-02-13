## Review `[index] : any` (indexer)
Name: []
Date: 2026-02-11
Test Count: 2

### Specification Extract 
Header in specification: [ index : Integer ] : any

The indexer operation returns a collection with only the `index`-th item (0-based index). If the input collection is empty (`{ }`), or the index lies outside the boundaries of the input collection, an empty collection is returned.

> **Note:** Unless specified otherwise by the underlying Object Model, the first item in a collection has index 0. Note that if the underlying model specifies that a collection is 1-based (the only reasonable alternative to 0-based collections), _any collections generated from operations on the 1-based list are 0-based_.

The following example returns the item in the `name` collection of the Patient at index 0:

### Example(s) from Specification
``` fhirpath
Patient.name[0]
```

### Coverage
2 tests found for `[]` (testIndexer1, testIndexer2).

**Covered:**
- ✅ Returns item at 0-based index position for first element (testIndexer1)
- ✅ Returns item at 0-based index position for non-first element (testIndexer2)

**Gaps:**
- ❌ Empty input returns empty collection
- ❌ Index outside boundaries returns empty collection

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testIndexer1 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testIndexer2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 11/12 (92%) — 2 tests × 6 engines

testIndexer1 fails in 1 engine, suggesting an engine-specific bug.
