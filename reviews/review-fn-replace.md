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
- ✅ Replaces instances of pattern with substitution (testReplace1)
- ✅ Empty substitution removes instances of pattern (testReplace3)
- ✅ Empty pattern surrounds every character with substitution (testReplace2)
- ✅ Empty input collection returns empty (testReplace4)
- ✅ Empty pattern parameter returns empty (testReplace5)
- ✅ Empty substitution parameter returns empty (testReplace6)

**Gaps:**
- ❌ Multiple occurrences of pattern in same string all replaced
- ❌ Multiple items in input signals error

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

testReplace5 and testReplace6 each fail in 1 engine (5/6 pass), suggesting engine-specific bugs with empty parameter propagation.
