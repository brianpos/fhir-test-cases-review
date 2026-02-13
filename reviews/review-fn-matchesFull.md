## Review `matchesFull(regex, [flags]) : Boolean` — STU
Name: matchesFull
Date: 2026-02-11
Test Count: 5

### Specification Extract 
Header in specification: matchesFull(regex : String, [flags : String]) : Boolean

> **Note:** The contents of this section are Standard for Trial Use (STU)

Returns `true` when the value completely matches the given regular expression (implying that the start/end of line markers `^`, `$` are always surrounding the regex expression provided).

Regular expressions should function consistently, regardless of any culture- and locale-specific settings in the environment, should be case-sensitive, use 'single line' mode and allow Unicode characters.

If the input collection or `regex` are empty, the result is empty (`{ }`).

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

The optional `flags` parameter can be set to:

* `i` to perform a case-insensitive search (otherwise is case-sensitive)
* `m` - Matches the start and end of each line using ^ and $ (multi-line)<br/>(not only begin/end of string)

### Example(s) from Specification
``` fhirpath
'http://fhir.org/guides/cqf/common/Library/FHIR-ModelInfo|4.0.1'.matchesFull('Library') // returns false
'N8000123123'.matchesFull('N[0-9]{8}') // returns false as the string is not an 8 char number (it has 10)
'N8000123123'.matchesFull('N[0-9]{10}') // returns true as the string has an 10 number sequence in it starting with `N`
```

### Coverage
5 tests found for `matchesFull` (testMatchesFullWithinUrl1, testMatchesFullWithinUrl3, testMatchesFullWithinUrl4, testMatchesFullWithinUrl1a, testMatchesFullWithinUrl2).

**Covered:**
- ✅ Full match required: partial matches return false (testMatchesFullWithinUrl1, testMatchesFullWithinUrl3, testMatchesFullWithinUrl2)
- ✅ Explicit `^`/`$` anchors with partial match still returns false (testMatchesFullWithinUrl4)
- ✅ Full match with `.*` wildcard returns true (testMatchesFullWithinUrl1a)

**Gaps:**
- ❌ Empty input or empty regex returning empty
- ❌ Multiple items in input collection signaling error
- ❌ Optional `flags` parameter (`i` for case-insensitive, `m` for multi-line)
- ❌ Single-line mode behavior with newlines

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testMatchesFullWithinUrl1 | N/A | N/A | N/A | ✅ | ✅ | ✅ |
| testMatchesFullWithinUrl1a | N/A | N/A | N/A | ✅ | ✅ | ✅ |
| testMatchesFullWithinUrl2 | N/A | N/A | N/A | ✅ | ✅ | ✅ |
| testMatchesFullWithinUrl3 | N/A | N/A | N/A | ✅ | ✅ | ✅ |
| testMatchesFullWithinUrl4 | N/A | N/A | N/A | ✅ | ✅ | ✅ |

**Summary:** 15/30 (50%) — 5 tests × 6 engines

5 test(s) are not implemented in some engines, but all implemented tests pass.
