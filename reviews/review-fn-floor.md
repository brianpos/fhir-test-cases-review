## Review `floor() : Integer | Quantity`
Name: floor
Date: 2026-02-11
Test Count: 4

### Specification Extract 
Header in specification: floor() : Integer | Quantity

Returns the first integer less than or equal to the input.

Accepts input types of Decimal or Quantity.

When used with a Decimal input type, the result is an Integer.<br/>
When used with a Quantity, the result is a Quantity with the same units and the value *(Decimal)* set to the integer result calculated.

If the input collection is empty, the result is empty.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.


> Note: We may consider a FloorLong() function to handle Long output types.

### Example(s) from Specification
``` fhirpath
1.floor() // 1
2.1.floor() // 2
(-2.1).floor() // -3
```

### Coverage
4 tests found for `floor` (testFloor1, testFloor2, testFloor3, testFloorEmpty).

**Covered:**
- ✅ Floor of integer value returns same value (testFloor1)
- ✅ Floor of positive decimal returns next lower integer (testFloor2)
- ✅ Floor of negative decimal rounds toward negative infinity (testFloor3)
- ✅ Empty input returns empty (testFloorEmpty)

**Gaps:**
- ❌ Quantity input returns Quantity with floored value and same units
- ❌ Multiple items in input signals error

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testFloor1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testFloor2 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testFloor3 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testFloorEmpty | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 22/24 (92%) — 4 tests × 6 engines

testFloor2 and testFloor3 each fail in 1 engine, likely the same engine, suggesting an engine-specific issue with decimal floor computation.
