## Review `abs() : Integer | Decimal | Quantity`
Name: abs
Date: 2026-02-11
Test Count: 4

### Specification Extract 
Header in specification: abs() : Integer | Long | Decimal | Quantity

Returns the absolute value of the input (in the same type). When taking the absolute value of a quantity, the unit is unchanged.

Accepts input types of Integer, Long, Decimal or Quantity.

If the input collection is empty, the result is empty.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

### Example(s) from Specification
``` fhirpath
(-5).abs() // 5
(-5.5).abs() // 5.5
(-5.5 'mg').abs() // 5.5 'mg'
```

### Coverage
4 tests found for `abs` (testAbs1, testAbs2, testAbs3, testAbsEmpty).

**Covered:**
- ✅ Absolute value of negative Integer returns positive Integer (testAbs1)
- ✅ Absolute value of negative Decimal returns positive Decimal (testAbs2)
- ✅ Absolute value of negative Quantity preserves unit (testAbs3)
- ✅ Empty input collection returns empty (testAbsEmpty)

**Gaps:**
- ❌ Absolute value of positive input returns same value
- ❌ Long input type not tested
- ❌ Multiple items in input collection signals an error

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testAbs1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testAbs2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testAbs3 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testAbsEmpty | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 23/24 (96%) — 4 tests × 6 engines
- Overall pass rate: 23/24 (96%)
- Tests: 4
