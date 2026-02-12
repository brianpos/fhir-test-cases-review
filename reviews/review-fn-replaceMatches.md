## Review `replaceMatches(regex, substitution, [flags]) : String`
Name: replaceMatches
Date: 2026-02-11
Test Count: 7

### Specification Extract 
Header in specification: replaceMatches(regex : String, substitution: String, [flags : String]) : String

Matches the input using the regular expression in `regex` and replaces each match with the `substitution` string. The substitution may refer to identified match groups in the regular expression, as illustrated by the example below that uses named capture groups for `month`, `day`, and `year` to perform a conversion from one date format to another.

If the input collection, `regex`, or `substitution` are empty, the result is empty (`{ }`).

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

The optional `flags` parameter can be set to:

* `i` to perform a case-insensitive search (otherwise is case-sensitive)
* `m` - Matches the start and end of each line using ^ and $ (multi-line)<br/>(not only begin/end of string)

This example of `replaceMatches()` will convert a string with a date formatted as MM/dd/yy to dd-MM-yy:

This example locates all the instances of `aa` and surrounds them with double quotes:

> **Note:** Platforms will typically use native regular expression implementations. These are typically fairly similar, but there will always be small differences. As such, FHIRPath does not prescribe a particular dialect, but recommends the use of the [\[PCRE\]](#PCRE) flavor as the dialect most likely to be broadly supported and understood.

### Example(s) from Specification
``` fhirpath
'11/30/1972'.replaceMatches('\\b(?<month>\\d{1,2})/(?<day>\\d{1,2})/(?<year>\\d{2,4})\\b',
       '${day}-${month}-${year}')
```

``` fhirpath
'aaabaa'.replaceMatches('aa', '"aa"') // returns "aa"ab"aa"
```

### Coverage
7 tests found for `replaceMatches` (testReplaceMatches1, testReplaceMatches2, testReplaceMatches3, testReplaceMatches4, testReplaceMatches5, testReplaceMatches6, testReplaceMatches7).

**Covered:**
- ✅ Basic regex pattern replacement and character class patterns (testReplaceMatches1, testReplaceMatches7)
- ✅ Empty regex and empty substitution behavior (testReplaceMatches2, testReplaceMatches3)
- ✅ Empty input, empty regex arg, or empty substitution arg returns empty (testReplaceMatches4, testReplaceMatches5, testReplaceMatches6)

**Gaps:**
- ❌ Capture group references in substitution string (e.g. named groups ${day}-${month}-${year})
- ❌ Optional flags parameter (`i` for case-insensitive, `m` for multi-line)
- ❌ Error on multiple items in input collection

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testReplaceMatches1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testReplaceMatches2 | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| testReplaceMatches3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testReplaceMatches4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testReplaceMatches5 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testReplaceMatches6 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testReplaceMatches7 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 37/42 (88%) — 7 tests × 6 engines

2 test(s) fail in only one engine, suggesting engine-specific implementation issues rather than problems with the tests or specification. 1 test(s) fail in multiple (but not all) engines, which may indicate differing interpretations of the specification.
