## Review `replace(pattern, substitution) : String`
Name: replace
Date: 2026-02-11
Test Count: 6

### Specification Extract 
Header in specification: replace(pattern : String, substitution : String) : String

Returns the input string with all instances of `pattern` replaced with `substitution`. If the substitution is the empty string (`''`), instances of `pattern` are removed from the result. If `pattern` is the empty string (`''`), every character in the input string is surrounded by the substitution, e.g. `'abc'.replace('','x')` becomes `'xaxbxcx'`.

If the input collection, `pattern`, or `substitution` are empty, the result is empty (`{ }`).

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

### Example(s) from Specification
``` fhirpath
'abcdefg'.replace('cde', '123') // 'ab123fg'
'abcdefg'.replace('cde', '') // 'abfg'
'abc'.replace('', 'x') // 'xaxbxcx'
```

### Coverage

6 tests found for `replace` (testReplace1, testReplace2, testReplace3, testReplace4, testReplace5, testReplace6).

**Covered:**
- ✅ Basic pattern replacement (testReplace1)
- ✅ Empty pattern surrounds each character with substitution (testReplace2)
- ✅ Empty substitution removes pattern occurrences (testReplace3)
- ✅ Empty input, empty pattern arg, or empty substitution arg returns empty (testReplace4, testReplace5, testReplace6)

**Gaps:**
- ❌ Multiple occurrences of pattern all replaced in one string
- ❌ Error on multiple items in input collection

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testReplace1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testReplace2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testReplace3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testReplace4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testReplace5 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testReplace6 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 34/36 (94%) — 6 tests × 6 engines

2 test(s) fail in only one engine, suggesting engine-specific implementation issues rather than problems with the tests or specification.
