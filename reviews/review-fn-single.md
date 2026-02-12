## Review `single() : any`
Name: single
Date: 2026-02-11
Test Count: 2

### Specification Extract 
Header in specification: single() : any

Will return the single item in the input if there is just one item. If the input collection is empty (`{ }`), the result is empty. If there are multiple items, an error is signaled to the evaluation environment. This function is useful for ensuring that an error is returned if an assumption about cardinality is violated at run-time.

The following example returns the name of the Patient if there is one. If there are no names, an empty collection, and if there are multiple names, an error is signaled to the evaluation environment:

### Example(s) from Specification
``` fhirpath
Patient.name.single()
```

### Coverage
2 tests found for `single` (testSingle1, testSingle2).

**Covered:**
- ✅ Single item in collection returns successfully (testSingle1)
- ✅ Multiple items signals error (testSingle2)

**Gaps:**
- ❌ Empty input collection returns empty

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testSingle1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testSingle2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 12/12 (100%) — 2 tests × 6 engines

All tests pass across all engines.
