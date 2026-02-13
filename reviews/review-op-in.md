## Review Membership
Name: in
Date: 2026-02-11
Test Count: 8

### Specification Extract 
Header in specification: in (membership) : Boolean

If the left operand is a collection with a single item, this operator returns `true` if the item is in the right operand using equality semantics. If the left-hand side of the operator is empty, the result is empty, if the right-hand side is empty, the result is `false`. If the left operand has multiple items, an exception is thrown.

The following example returns `true` if `'Joe'` is in the list of given names for the Patient:

### Example(s) from Specification
``` fhirpath
'Joe' in Patient.name.given
```

### Coverage
8 tests found for `in` (testIn1, testIn2, testIn3, testIn4, testIn5, testInEmptyCollection, testInEmptyValue, testInEmptyBoth).

**Covered:**
- ✅ Single item found in collection returns true (testIn1, testIn3)
- ✅ Single item not found in collection returns false (testIn2, testIn4)
- ✅ Multiple items on left side throws exception (testIn5)
- ✅ Right side empty returns false (testInEmptyCollection)
- ✅ Left side empty returns empty (testInEmptyValue)
- ✅ Both sides empty returns empty (testInEmptyBoth)

**Gaps:**
- ❌ Equality semantics with implicit type conversion (e.g., Integer in Decimal collection)
- ❌ Quantity membership with unit conversion

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testIn1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testIn2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testIn3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testIn4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testIn5 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testInEmptyCollection | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testInEmptyValue | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| testInEmptyBoth | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |

**Summary:** 46/48 (96%) — 8 tests × 6 engines

Two tests fail on a single engine (testInEmptyValue, testInEmptyBoth), suggesting an engine-specific bug in empty collection handling.
