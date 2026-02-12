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
(none)

**Gaps:**
- ❌ All specification requirements lack test coverage
