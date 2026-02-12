## Review `contains(substring) : Boolean` ¹
Name: contains
Date: 2026-02-11
Test Count: 21

### Specification Extract 
Header in specification: contains(substring : String) : Boolean

Returns `true` when the given `substring` is a substring of the input string.

If `substring` is the empty string (`''`), the result is `true`.

If the input collection is empty, the result is empty.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.


> **Note:** The `.contains()` function described here is a string function that looks for a substring in a string. This is different than the [`contains`](#contains-containership--boolean) operator, which is a list operator that looks for an item in a list.

### Example(s) from Specification
``` fhirpath
'abc'.contains('b') // true
'abc'.contains('bc') // true
'abc'.contains('d') // false
```

### Coverage

21 tests found for `contains` (testContainsString1, testContainsString2, testContainsString3, testContainsString4, testContainsString5, testContainsString6, testContainsString7, testContainsString8, testContainsString9, testContainsString10, testContainsString10a, testContainsNonString1, testContainsCollection1, testContainsCollection2, testContainsCollection3, testContainsCollection4, testContainsCollectionEmpty1, testContainsCollectionEmpty2, testContainsCollectionEmpty3, testContainsCollectionEmpty4, testContainsCollectionEmptyDateTime).

**Covered:**
- ✅ Substring found in string (testContainsString2, testContainsString3, testContainsString5)
- ✅ Substring not found in string (testContainsString1, testContainsString4, testContainsString6)
- ✅ Empty substring returns true (testContainsString7)
- ✅ Empty input collection returns empty (testContainsString8, testContainsString9)
- ✅ Non-string input type signals semantic error (testContainsNonString1)
- ✅ String contains used in select context (testContainsString10)
- ✅ Invalid usage signals semantic error (testContainsString10a)
- ✅ Contains operator with integers and strings (testContainsCollection1, testContainsCollection2, testContainsCollection3, testContainsCollection4)
- ✅ Contains operator with empty collection (testContainsCollectionEmpty1, testContainsCollectionEmpty2, testContainsCollectionEmpty3, testContainsCollectionEmpty4, testContainsCollectionEmptyDateTime)

**Gaps:**
- ❌ Multiple items in input collection signals an error (string function)
- ❌ Case sensitivity behavior not tested

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testContainsString1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testContainsString2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testContainsString3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testContainsString4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testContainsString5 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testContainsString6 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testContainsString7 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testContainsString8 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testContainsString9 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testContainsString10 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testContainsString10a | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testContainsNonString1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testContainsCollection1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testContainsCollection2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testContainsCollection3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testContainsCollection4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testContainsCollectionEmpty1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testContainsCollectionEmpty2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testContainsCollectionEmpty3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testContainsCollectionEmpty4 | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| testContainsCollectionEmptyDateTime | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:**
- Overall pass rate: 124/126 (98%)
- Tests: 21
- Engines with failures: Aidbox, Firely-5.12.2.
- Engines passing all tests: fhirpath.js-4.8.3, Helios-0.1.32, Ignixa-0.0.151, Java-6.7.8.
