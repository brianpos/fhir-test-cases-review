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
- ✅ Collection contains: item present in collection (testContainsCollection1, testContainsCollection3)
- ✅ Collection contains: item not in collection (testContainsCollection2, testContainsCollection4)
- ✅ Collection contains: empty left operand returns false (testContainsCollectionEmpty1, testContainsCollectionEmpty2, testContainsCollectionEmpty3)
- ✅ Collection contains: empty right operand returns empty (testContainsCollectionEmpty4)
- ✅ Collection contains: DateTime type (testContainsCollectionEmptyDateTime)
- ✅ String contains(): substring found and not found (testContainsString1 through testContainsString6)
- ✅ String contains(): empty substring returns true (testContainsString7)
- ✅ String contains(): empty input returns empty (testContainsString8, testContainsString9)
- ✅ String contains() in select context (testContainsString10, testContainsString10a)
- ✅ Non-string input behavior (testContainsNonString1)

**Gaps:**
- ❌ No explicit test verifying contains is converse of in (same result for x contains y and y in x)

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testContainsCollection1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testContainsCollection2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testContainsCollection3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testContainsCollection4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testContainsCollectionEmpty1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testContainsCollectionEmpty2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testContainsCollectionEmpty3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testContainsCollectionEmpty4 | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| testContainsCollectionEmptyDateTime | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testContainsNonString1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testContainsString1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testContainsString10 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testContainsString10a | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testContainsString2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testContainsString3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testContainsString4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testContainsString5 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testContainsString6 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testContainsString7 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testContainsString8 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testContainsString9 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 124/126 (98%) — 21 tests × 6 engines

2 test(s) fail in only one engine, suggesting engine-specific implementation issues rather than problems with the tests or specification.
