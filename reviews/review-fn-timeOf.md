## Review `timeOf() : Time`
Name: timeOf
Date: 2026-02-11
Test Count: 0

### Specification Extract 
Header in specification: timeOf(): Time

If the input collection contains a single DateTime, this function will return the time component.

If the input collection is empty, or the time is not present in the value, the result is empty.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

### Example(s) from Specification
``` fhirpath
@2012-01-01T12:30:00.000-07:00.timeOf() // @T12:30:00.000
```

### Coverage
0 tests found for `timeOf`.

**Covered:**
(none)

**Gaps:**
- ❌ All specification requirements lack test coverage

### Test Results

No tests exist for this function yet. Test results will be added once tests are created.
