## Review `allTrue() : Boolean`
Name: allTrue
Date: 2026-02-11
Test Count: 3

### Specification Extract 
Header in specification: allTrue() : Boolean

Takes a collection of Boolean values and returns `true` if all the items are `true`. If any items are `false`, the result is `false`. If the input is empty (`{ }`), the result is `true`.

The following example returns `true` if all of the components of the Observation have a value greater than 90 mm[Hg]:

### Example(s) from Specification
``` fhirpath
Observation.select(component.value > 90 'mm[Hg]').allTrue()
```

### Coverage
3 tests found for `allTrue` (testAllTrue1, testAllTrue2, from-zulip-2).

**Covered:**
- ✅ Returns true when all items are true (testAllTrue1)
- ✅ Returns false when any item is false (testAllTrue2)
- ✅ Non-Boolean items in collection signal an error (from-zulip-2)

**Gaps:**
- ❌ Empty input collection returns true
- ❌ Collection containing only false values not tested

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testAllTrue1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testAllTrue2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| from-zulip-2 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:**
- Overall pass rate: 17/18 (94%)
- Tests: 3
