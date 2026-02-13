## Review Containership ¹
Name: contains
Date: 2026-02-11
Test Count: 21

### Specification Extract 
Header in specification: contains (containership) : Boolean

If the right operand is a collection with a single item, this operator returns `true` if the item is in the left operand using equality semantics. If the right-hand side of the operator is empty, the result is empty, if the left-hand side is empty, the result is `false`. This is the converse operation of `in`.

The following example returns `true` if the list of given names for the Patient has `'Joe'` in it:

### Example(s) from Specification
``` fhirpath
Patient.name.given contains 'Joe'
```

### Coverage
21 tests found for `contains` (testContainsString1, testContainsString2, testContainsString3, testContainsString4, testContainsString5, testContainsString6, testContainsString7, testContainsString8, testContainsString9, testContainsString10, testContainsString10a, testContainsNonString1, testContainsCollection1, testContainsCollection2, testContainsCollection3, testContainsCollection4, testContainsCollectionEmpty1, testContainsCollectionEmpty2, testContainsCollectionEmpty3, testContainsCollectionEmpty4, testContainsCollectionEmptyDateTime).

**Covered:**
- ✅ Collection containership: returns true when single item is in left collection (testContainsCollection1, testContainsCollection3)
- ✅ Collection containership: returns false when item is not in left collection (testContainsCollection2, testContainsCollection4)
- ✅ Collection containership: empty left operand returns false (testContainsCollectionEmpty1, testContainsCollectionEmpty2, testContainsCollectionEmpty3, testContainsCollectionEmptyDateTime)
- ✅ Collection containership: empty right operand returns empty (testContainsCollectionEmpty4)
- ✅ String contains function: substring present and absent cases (testContainsString1, testContainsString2, testContainsString3, testContainsString4, testContainsString5, testContainsString6)
- ✅ String contains: empty string is contained in any string (testContainsString7)
- ✅ String contains: empty collection input returns empty (testContainsString8, testContainsString9)
- ✅ String contains: with computed expression argument via select (testContainsString10)
- ✅ Semantic error for contains on non-string types or ambiguous overload (testContainsString10a, testContainsNonString1)

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

testContainsString10a and testContainsCollectionEmpty4 each fail on single engines, suggesting engine-specific bugs in semantic error detection and empty collection handling.
