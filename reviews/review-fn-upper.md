## Review `upper() : String`
Name: upper
Date: 2026-02-11
Test Count: 2

### Specification Extract 
Header in specification: upper() : String

Returns the input string with all characters converted to upper case.

If the input collection is empty, the result is empty.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

### Example(s) from Specification
``` fhirpath
'abcdefg'.upper() // 'ABCDEFG'
'AbCdefg'.upper() // 'ABCDEFG'
```

### Coverage
2 tests found for `upper` (testCase1, testCase3).

**Covered:**
- ✅ Converts lowercase character to uppercase (testCase1)
- ✅ Already uppercase character remains unchanged (testCase3)

**Gaps:**
- ❌ Multi-character string conversion (e.g. 'abcdefg' to 'ABCDEFG')
- ❌ Mixed case string conversion (e.g. 'AbCdefg' to 'ABCDEFG')
- ❌ Empty input returns empty
- ❌ Multiple items in input collection signals error

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testCase1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testCase3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 12/12 (100%) — 2 tests × 6 engines
