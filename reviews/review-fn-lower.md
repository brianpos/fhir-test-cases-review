## Review `lower() : String`
Name: lower
Date: 2026-02-11
Test Count: 2

### Specification Extract 
Header in specification: lower() : String

Returns the input string with all characters converted to lower case.

If the input collection is empty, the result is empty.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

### Example(s) from Specification
``` fhirpath
'ABCDEFG'.lower() // 'abcdefg'
'aBcDEFG'.lower() // 'abcdefg'
```

### Coverage

2 tests found for `lower` (testCase2, testCase4).

**Covered:**
- ✅ Uppercase character converted to lowercase (testCase4)
- ✅ Already-lowercase character unchanged (testCase2)

**Gaps:**
- ❌ Empty input collection returning empty
- ❌ Multiple items in input collection signaling error
- ❌ Full multi-character string conversion (spec examples show `'ABCDEFG'.lower()`)

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testCase2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testCase4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 12/12 (100%) — 2 tests × 6 engines

All tests pass across all engines.
