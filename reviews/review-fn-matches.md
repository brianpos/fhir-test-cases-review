## Review `matches(regex, [flags]) : Boolean`
Name: matches
Date: 2026-02-11
Test Count: 11

### Specification Extract 
Header in specification: matches(regex : String, [flags : String]) : Boolean

Returns `true` when the value matches the given regular expression. Regular expressions should function consistently, regardless of any culture- and locale-specific settings in the environment, should be case-sensitive, use 'single line' mode and allow Unicode characters.
The start/end of line markers `^`, `$` can be used to match the entire string.

If the input collection or `regex` are empty, the result is empty (`{ }`).

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

The optional `flags` parameter can be set to:

* `i` to perform a case-insensitive search (otherwise is case-sensitive)
* `m` - Matches the start and end of each line using ^ and $ (multi-line)<br/>(not only begin/end of string)

### Example(s) from Specification
``` fhirpath
'http://fhir.org/guides/cqf/common/Library/FHIR-ModelInfo|4.0.1'.matches('Library') // returns true
'N8000123123'.matches('^N[0-9]{8}$') // returns false as the string is not an 8 char number (it has 10)
'N8000123123'.matches('N[0-9]{8}') // returns true as the string has an 8 number sequence in it starting with `N`
```

### Coverage
11 tests found for `matches` (testMatchesCaseSensitive1, testMatchesCaseSensitive2, testMatchesEmpty, testMatchesEmpty2, testMatchesEmpty3, testMatchesSingleLineMode1, testMatchesWithinUrl1, testMatchesWithinUrl2, testMatchesWithinUrl3, testMatchesWithinUrl1a, testMatchesWithinUrl4).

**Covered:**
- ✅ Returns true when value matches given regular expression (testMatchesCaseSensitive1, testMatchesWithinUrl2)
- ✅ Case-sensitive matching by default (testMatchesCaseSensitive1, testMatchesCaseSensitive2)
- ✅ Single line mode: dot matches newlines (testMatchesSingleLineMode1)
- ✅ Start/end markers ^/$ can match entire string (testMatchesWithinUrl3)
- ✅ Partial regex matching within strings (testMatchesWithinUrl2, testMatchesWithinUrl1a)
- ✅ Returns false when value does not match (testMatchesWithinUrl1, testMatchesWithinUrl4)
- ✅ Empty regex returns empty (testMatchesEmpty)
- ✅ Empty input returns empty (testMatchesEmpty2)
- ✅ Both input and regex empty returns empty (testMatchesEmpty3)

**Gaps:**
- ❌ Optional 'i' flag for case-insensitive search
- ❌ Optional 'm' flag for multi-line mode
- ❌ Unicode character handling in regex
- ❌ Multiple items in input collection signals error
- ❌ Culture and locale independence verification

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testMatchesCaseSensitive1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMatchesCaseSensitive2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMatchesEmpty | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMatchesEmpty2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMatchesEmpty3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMatchesSingleLineMode1 | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ |
| testMatchesWithinUrl1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMatchesWithinUrl2 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMatchesWithinUrl3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMatchesWithinUrl1a | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMatchesWithinUrl4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 62/66 (94%) — 11 tests × 6 engines

testMatchesSingleLineMode1 fails in 2 engines (4/6), suggesting disagreement on single-line mode (dot matching newlines). testMatchesEmpty and testMatchesWithinUrl2 each fail in 1 engine.
