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
- ✅ Floor of integer returns same value (testFloor1)
- ✅ Floor of positive decimal rounds down (testFloor2)
- ✅ Floor of negative decimal rounds toward negative infinity (testFloor3)
- ✅ Empty input returns empty (testFloorEmpty)

**Gaps:**
- ❌ No test for Quantity input returning Quantity with same units
- ❌ No test for error when input collection contains multiple items

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testFloor1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testFloor2 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testFloor3 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testFloorEmpty | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 22/24 (92%) — 4 tests × 6 engines

2 test(s) fail in only one engine, suggesting engine-specific implementation issues rather than problems with the tests or specification.
