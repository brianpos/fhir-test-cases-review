## Review `ceiling() : Integer | Quantity`
Name: ceiling
Date: 2026-02-11
Test Count: 4

### Specification Extract 
Header in specification: ceiling() : Integer | Quantity

Returns the first integer greater than or equal to the input.

Accepts input types of Decimal or Quantity.

When used with a Decimal input type, the result is an Integer.<br/>
When used with a Quantity, the result is a Quantity with the same units and the value *(Decimal)* set to the integer result calculated.

If the input collection is empty, the result is empty.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.


> Note: We may consider a CeilingLong() function to handle Long output types.

### Example(s) from Specification
``` fhirpath
1.ceiling() // 1
1.1.ceiling() // 2
(-1.1).ceiling() // -1
```

### Coverage
4 tests found for `ceiling` (testCeiling1, testCeiling2, testCeiling3, testCeilingEmpty).

**Covered:**
- ✅ Returns first integer greater than or equal to input (testCeiling1, testCeiling2, testCeiling3)
- ✅ Accepts Decimal input type (testCeiling2, testCeiling3)
- ✅ Decimal input returns Integer result (testCeiling1, testCeiling2, testCeiling3)
- ✅ Negative decimal correctly rounds toward zero (testCeiling2)
- ✅ Empty input collection returns empty (testCeilingEmpty)

**Gaps:**
- ❌ Quantity input type not tested (result should be Quantity with same units and integer value)
- ❌ Multiple items in input collection signals error not tested

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testCeiling1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testCeiling2 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testCeiling3 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testCeilingEmpty | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 22/24 (92%) — 4 tests × 6 engines

Two decimal ceiling tests each fail in 1 engine, suggesting engine-specific bugs.
