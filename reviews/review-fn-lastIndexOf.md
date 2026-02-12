## Review `lastIndexOf(substring) : Integer` — STU
Name: lastIndexOf
Date: 2026-02-11
Test Count: 0

### Specification Extract 
Header in specification: lastIndexOf(substring : String) : Integer

> **Note:** The contents of this section are Standard for Trial Use (STU)

Returns the 0-based index of the last position `substring` is found in the input string, or -1 if it is not found.

If `substring` is an empty string (`''`), the function returns the length of the string.

If the input or `substring` is empty (`{ }`), the result is empty (`{ }`).

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

### Example(s) from Specification
``` fhirpath
'abcdefg'.lastIndexOf('bc') // 1
'abcdefg'.lastIndexOf('x') // -1
'abcdefg'.lastIndexOf('abcdefg') // 0
'abc abc'.lastIndexOf('a') // 4
'0123'.lastIndexOf('') // 4
'0'.lastIndexOf('') // 1
''.lastIndexOf('') // 0
```

### Coverage
0 tests found for `lastIndexOf`.

**Covered:**
(none)

**Gaps:**
- ❌ All specification requirements lack test coverage

### Test Results

No tests exist for this function yet. Test results will be added once tests are created.
