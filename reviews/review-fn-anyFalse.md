## Review `anyFalse() : Boolean`
Name: anyFalse
Date: 2026-02-11
Test Count: 0

### Specification Extract 
Header in specification: anyFalse() : Boolean

Takes a collection of Boolean values and returns `true` if any of the items are `false`. If all the items are `true`, or if the input is empty (`{ }`), the result is `false`.

The following example returns `true` if any of the components of the Observation have a value that is not greater than 90 mm[Hg]:

### Example(s) from Specification
``` fhirpath
Observation.select(component.value > 90 'mm[Hg]').anyFalse()
```

### Coverage
0 tests found for `anyFalse`.

**Covered:**
(none)

**Gaps:**
- ❌ All specification requirements lack test coverage
