## Review Division
Name: /
Date: 2026-02-11
Test Count: 12

### Specification Extract 
Header in specification: / (division)

Divides the left operand by the right operand (supported for Integer, Decimal, and Quantity). The result of a division is always Decimal, even if the inputs are both Integer. For integer division, use the `div` operator.

If an attempt is made to divide by zero, the result is empty.

For division involving quantities, the resulting quantity will have an appropriate unit:

### Example(s) from Specification
``` fhirpath
12 'cm2' / 3 'cm' // 4.0 'cm'
12 / 0 // empty ({ })
```

### Coverage
12 tests found for `/` (testQuantity10, testQuantity11, testMixedPrecisionArithmetic3, testDivide1, testDivide2, testDivide3, testDivide4, testDivide5, testDivide6, testDivideEmpty1, testDivideEmpty2, testDivideEmpty3).

**Covered:**
- ✅ Integer division (testDivide1, testDivide2, testDivide4)
- ✅ Decimal division (testDivide3, testDivide5)
- ✅ Mixed Integer/Decimal division (testMixedPrecisionArithmetic3)
- ✅ Quantity division with resulting unit (testQuantity10, testQuantity11)
- ✅ Division by zero returns empty (testDivide6)
- ✅ Empty operand propagation (testDivideEmpty1, testDivideEmpty2, testDivideEmpty3)

**Gaps:**
- ❌ No test verifying result type is always Decimal even when both inputs are Integer

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testDivide1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDivide2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDivide3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDivide4 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDivide5 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDivide6 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDivideEmpty1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDivideEmpty2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDivideEmpty3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMixedPrecisionArithmetic3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testQuantity10 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testQuantity11 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 67/72 (93%) — 12 tests × 6 engines

5 test(s) fail in only one engine, suggesting engine-specific implementation issues rather than problems with the tests or specification.
