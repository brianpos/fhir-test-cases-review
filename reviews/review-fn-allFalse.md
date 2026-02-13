## Review `allFalse() : Boolean`
Name: allFalse
Date: 2026-02-11
Test Count: 0

### Specification Extract 
Header in specification: allFalse() : Boolean

Takes a collection of Boolean values and returns `true` if all the items are `false`. If any items are `true`, the result is `false`. If the input is empty (`{ }`), the result is `true`.

The following example returns `true` if none of the components of the Observation have a value greater than 90 mm[Hg]:

### Example(s) from Specification
``` fhirpath
Observation.select(component.value > 90 'mm[Hg]').allFalse()
```

### Coverage
0 tests found for `allFalse`.

**Covered:**
- (none)

**Gaps:**
- ❌ Returns true when all items in collection are false not tested
- ❌ Returns false when any items are true not tested
- ❌ Empty input returns true not tested

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|

**Summary:** 0/0 (0%) — 0 tests × 6 engines
