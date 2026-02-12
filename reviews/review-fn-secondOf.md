## Review `secondOf() : Integer`
Name: secondOf
Date: 2026-02-11
Test Count: 0

### Specification Extract 
Header in specification: secondOf(): Integer

If the input collection contains a single DateTime or Time, this function will return the second component.

If the input collection is empty, or the second is not present in the value, the result is empty.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

### Example(s) from Specification
``` fhirpath
@2012-01-01T12:30:40.002-07:00.secondOf() // 40
```

### Coverage

0 tests found for `secondOf`.

**Covered:**
(none)

**Gaps:**
- ❌ All specification requirements lack test coverage

### Test Results

No tests exist for this function yet. Test results will be added once tests are created.
