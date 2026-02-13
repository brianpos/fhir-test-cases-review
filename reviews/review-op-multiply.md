## Review Multiplication
Name: *
Date: 2026-02-11
Test Count: 8

### Specification Extract 
Header in specification: * (multiplication)

Multiplies both arguments (supported for Integer, Decimal, and Quantity). For multiplication involving quantities, the resulting quantity will have an appropriate unit as determined by application of the UCUM specification:

### Example(s) from Specification
``` fhirpath
12 'cm' * 3 'cm' // 36 'cm2'
3 'cm' * 12 'cm2' // 36 'cm3'
```

### Coverage
8 tests found for `*` (testQuantity9, testMixedPrecisionArithmetic2, testMultiply1, testMultiply2, testMultiply3, testMultiplyEmpty1, testMultiplyEmpty2, testMultiplyEmpty3).

**Covered:**
- ✅ Integer multiplication (testMultiply1, testMultiply2)
- ✅ Decimal multiplication (testMultiply3)
- ✅ Quantity multiplication with UCUM unit derivation (testQuantity9)
- ✅ Mixed precision Integer*Decimal via implicit conversion (testMixedPrecisionArithmetic2)
- ✅ Empty operand returns empty (testMultiplyEmpty1, testMultiplyEmpty2, testMultiplyEmpty3)

**Gaps:**
- ❌ Multiplication of two quantities with same units producing squared unit (e.g., 12 'cm' * 3 'cm' = 36 'cm2')
- ❌ Multiplication of quantity by quantity with higher-dimension units (e.g., 3 'cm' * 12 'cm2' = 36 'cm3')

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testQuantity9 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMixedPrecisionArithmetic2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMultiply1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMultiply2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMultiply3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMultiplyEmpty1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMultiplyEmpty2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMultiplyEmpty3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 47/48 (98%) — 8 tests × 6 engines

1 of 8 tests fails in 1 engine - quantity multiplication with different units, suggesting an engine-specific bug.
