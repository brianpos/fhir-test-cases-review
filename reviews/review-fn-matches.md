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
11 tests found for `matches` (testMatchesCaseSensitive1, testMatchesCaseSensitive2, testMatchesEmpty, testMatchesEmpty2, testMatchesEmpty3, testMatchesSingleLineMode1, testMatchesWithinUrl1, testMatchesWithinUrl1a, testMatchesWithinUrl2, testMatchesWithinUrl3, testMatchesWithinUrl4).

**Covered:**
- ✅ Case-sensitive matching (testMatchesCaseSensitive1, testMatchesCaseSensitive2)
- ✅ Empty input or empty regex returns empty (testMatchesEmpty, testMatchesEmpty2, testMatchesEmpty3)
- ✅ Single-line mode: `.` matches newline (testMatchesSingleLineMode1)
- ✅ Partial match within strings and `^`/`$` anchors (testMatchesWithinUrl1, testMatchesWithinUrl1a, testMatchesWithinUrl2, testMatchesWithinUrl3, testMatchesWithinUrl4)

**Gaps:**
- ❌ Multiple items in input collection signaling error
- ❌ Optional `flags` parameter (`i` for case-insensitive, `m` for multi-line)

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
| testMatchesWithinUrl1a | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMatchesWithinUrl2 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMatchesWithinUrl3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMatchesWithinUrl4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 62/66 (94%) — 11 tests × 6 engines

2 test(s) fail in only one engine, suggesting engine-specific implementation issues rather than problems with the tests or specification. 1 test(s) fail in multiple (but not all) engines, which may indicate differing interpretations of the specification.
