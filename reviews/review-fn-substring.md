## Review `substring(start, [length]) : String`
Name: substring
Date: 2026-02-11
Test Count: 12

### Specification Extract 
Header in specification: substring(start : Integer [, length : Integer]) : String

Returns the part of the string starting at position `start` (zero-based). If `length` is given, will return at most `length` number of characters from the input string. <span class="fhir-highlight">Both `start` and `length` are measured in characters (Unicode scalar values).</span>

If `start` lies outside the length of the string, the function returns empty (`{ }`). If there are fewer remaining characters in the string than indicated by `length`, the function returns just the remaining characters.

If the input or `start` is empty, the result is empty.

If an empty `length` is provided, the behavior is the same as if `length` had not been provided.

If a negative or zero `length` is provided, the function returns an empty string (`''`).

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

### Example(s) from Specification
``` fhirpath
'abcdefg'.substring(3) // 'defg'
'abcdefg'.substring(1, 2) // 'bc'
'abcdefg'.substring(6, 2) // 'g'
'abcdefg'.substring(7, 1) // { } (start position is outside the string)
'abcdefg'.substring(-1, 1) // { } (start position is outside the string,
                           //     this can happen when the -1 was the result of a calculation rather than explicitly provided)
'abcdefg'.substring(3, 0) // '' (empty string)
'abcdefg'.substring(3, -1) // '' (empty string)
'abcdefg'.substring(-1, -1) // {} (start position is outside the string)
```

### Coverage
12 tests found for `substring` (testSubstring1, testSubstring2, testSubstring3, testSubstring4, testSubstring5, testSubstring7, testSubstring8, testSubstring9, testSubstring10, testSubstring10a, testSubstring11, testSubstring12).

**Covered:**
- ✅ Returns part of string starting at zero-based position (testSubstring1, testSubstring7)
- ✅ Length parameter limits number of characters returned (testSubstring2, testSubstring7, testSubstring8)
- ✅ Fewer remaining characters than length returns just remaining characters (testSubstring3)
- ✅ Start position outside string length returns empty (testSubstring4)
- ✅ Negative start position returns empty (testSubstring5)
- ✅ Empty input returns empty (testSubstring9, testSubstring11)
- ✅ Empty start parameter returns empty (testSubstring11, testSubstring12)
- ✅ Dynamic length calculation using indexOf (testSubstring8)
- ✅ Scoped usage with select for relative parameter resolution (testSubstring10)
- ✅ Semantic error for non-scoped ambiguous parameter (testSubstring10a)

**Gaps:**
- ❌ Unicode scalar value measurement (no test with multi-byte characters)
- ❌ Empty length behaves as if length had not been provided
- ❌ Negative or zero length returns empty string
- ❌ Multiple items in input signals error

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testSubstring1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testSubstring2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testSubstring3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testSubstring4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testSubstring5 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testSubstring7 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testSubstring8 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testSubstring9 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testSubstring10 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testSubstring10a | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testSubstring11 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testSubstring12 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 69/72 (96%) — 12 tests × 6 engines

testSubstring5, testSubstring10a, and testSubstring12 each fail in 1 engine, suggesting engine-specific bugs with negative start handling, semantic checking, and empty start parameter handling respectively.
