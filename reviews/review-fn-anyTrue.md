## Review `anyTrue() : Boolean`
Name: anyTrue
Date: 2026-02-11
Test Count: 0

### Specification Extract 
Header in specification: anyTrue() : Boolean

Takes a collection of Boolean values and returns `true` if any of the items are `true`. If all the items are `false`, or if the input is empty (`{ }`), the result is `false`.

The following example returns `true` if any of the components of the Observation have a value greater than 90 mm[Hg]:

### Example(s) from Specification
``` fhirpath
Observation.select(component.value > 90 'mm[Hg]').anyTrue()
```

### Coverage
0 tests found for `anyTrue`.

**Covered:**
- (none)

**Gaps:**
- ❌ Returns true when any items in collection are true not tested
- ❌ Returns false when all items are false not tested
- ❌ Empty input returns false not tested

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|

**Summary:** 0/0 (0%) — 0 tests × 6 engines
