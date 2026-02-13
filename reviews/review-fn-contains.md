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
- ✅ Returns true when substring is found in input string (testContainsString2, testContainsString3, testContainsString5)
- ✅ Returns false when substring is not found in input string (testContainsString1, testContainsString4, testContainsString6)
- ✅ Empty substring returns true (testContainsString7)
- ✅ Empty input collection returns empty (testContainsString8, testContainsString9)
- ✅ Non-string input type signals error (testContainsNonString1)
- ✅ Static type checking for contains argument (testContainsString10a)
- ✅ Contains function used within select scope (testContainsString10)
- ✅ Contains operator tests membership in collection with integers (testContainsCollection1, testContainsCollection2)
- ✅ Contains operator tests membership in collection with strings (testContainsCollection3, testContainsCollection4)
- ✅ Contains operator with empty collection returns false (testContainsCollectionEmpty1, testContainsCollectionEmpty2, testContainsCollectionEmpty3, testContainsCollectionEmptyDateTime)
- ✅ Contains operator with empty right operand returns empty (testContainsCollectionEmpty4)

**Gaps:**
- (none)

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

**Summary:** 124/126 (98%) — 21 tests × 6 engines

Two tests each fail in 1 engine, suggesting engine-specific bugs with semantic error handling and empty collection containership.
