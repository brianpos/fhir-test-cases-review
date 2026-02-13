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
- (none)

**Gaps:**
- ❌ Returns 0-based index of last position substring is found
- ❌ Returns -1 if substring is not found
- ❌ Empty string returns the length of the string
- ❌ Empty input or substring returns empty
- ❌ Multiple items in input collection signals error

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|

**Summary:** 0/0 (0%) — 0 tests × 6 engines