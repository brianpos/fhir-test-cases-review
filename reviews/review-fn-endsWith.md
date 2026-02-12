## Review `endsWith(suffix) : Boolean`
Name: endsWith
Date: 2026-02-11
Test Count: 12

### Specification Extract 
Header in specification: endsWith(suffix : String) : Boolean

Returns `true` when the input string ends with the given `suffix`.

If `suffix` is the empty string (`''`), the result is `true`.

If the input collection is empty, the result is empty.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

### Example(s) from Specification
``` fhirpath
'abcdefg'.endsWith('efg') // true
'abcdefg'.endsWith('abc') // false
```

### Coverage
12 tests found for `endsWith` (testEndsWith1, testEndsWith2, testEndsWith3, testEndsWith4, testEndsWith5, testEndsWith6, testEndsWith7, testEndsWith8, testEndsWith9, testEndsWith10, testEndsWith10a, testEndsWithNonString1).

**Covered:**
- ✅ Suffix at end returns true, suffix not at end returns false (testEndsWith1, testEndsWith2, testEndsWith3, testEndsWith4)
- ✅ Full string as suffix returns true (testEndsWith5)
- ✅ Suffix longer than string returns false (testEndsWith6)
- ✅ Empty suffix returns true (testEndsWith7)
- ✅ Empty input returns empty (testEndsWith8, testEndsWith9)
- ✅ Computed suffix via select context (testEndsWith10)
- ✅ Error on non-string input type (testEndsWith10a, testEndsWithNonString1)

**Gaps:**
- ❌ No test for error when input collection contains multiple string items

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testEndsWith1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEndsWith10 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEndsWith10a | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEndsWith2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEndsWith3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEndsWith4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEndsWith5 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEndsWith6 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEndsWith7 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEndsWith8 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEndsWith9 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEndsWithNonString1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 71/72 (99%) — 12 tests × 6 engines

1 test(s) fail in only one engine, suggesting engine-specific implementation issues rather than problems with the tests or specification.
