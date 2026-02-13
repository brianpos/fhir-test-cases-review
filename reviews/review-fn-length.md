## Review `length() : Integer`
Name: length
Date: 2026-02-11
Test Count: 6

### Specification Extract 
Header in specification: length() : Integer

Returns the number of characters <span class="fhir-highlight">(Unicode scalar values)</span> in the input string. If the input collection is empty (`{ }`), the result is empty.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

Note that `length()` counts characters (Unicode scalar values), not visual characters (grapheme clusters). For example, the string `'é'` encoded as U+0065 + U+0301 (combining form) has a length of 2, while `'é'` encoded as U+00E9 (precomposed form) has a length of 1.

### Example(s) from Specification
_No examples found in specification._

### Coverage
6 tests found for `length` (testLength1, testLength2, testLength3, testLength4, testLength5, testLength6).

**Covered:**
- ✅ Returns number of characters in input string (testLength1, testLength2, testLength3, testLength4)
- ✅ Empty string returns 0 (testLength5)
- ✅ Empty collection returns empty (testLength6)

**Gaps:**
- ❌ Counts Unicode scalar values, not grapheme clusters (no test with combining characters)
- ❌ Multiple items in input collection signals error

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testLength1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLength2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLength3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLength4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLength5 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLength6 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 36/36 (100%) — 6 tests × 6 engines
