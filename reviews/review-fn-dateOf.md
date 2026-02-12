## Review `dateOf() : Date`
Name: dateOf
Date: 2026-02-11
Test Count: 0

### Specification Extract 
Header in specification: dateOf(): Date

If the input collection contains a single Date or DateTime, this function will return the date component (up to the precision present in the input value).

If the input collection is empty, the result is empty.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

### Example(s) from Specification
``` fhirpath
@2012-01-01T12:30:00.000-07:00.dateOf() // @2012-01-01
```

### Coverage
0 tests found for `dateOf`.

**Covered:**
(none)

**Gaps:**
- ❌ All specification requirements lack test coverage

### Test Results

No tests exist for this function yet. Test results will be added once tests are created.
