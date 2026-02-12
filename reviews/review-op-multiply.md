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
- ✅ Integer multiplication including identity and zero (testMultiply1, testMultiply2)
- ✅ Decimal multiplication (testMultiply3)
- ✅ Mixed precision decimal * integer (testMixedPrecisionArithmetic2)
- ✅ Quantity * Quantity with UCUM unit derivation (testQuantity9)
- ✅ Empty collection propagation (testMultiplyEmpty1, testMultiplyEmpty2, testMultiplyEmpty3)

**Gaps:**
- ❌ No test for integer * integer yielding larger results (e.g. negative numbers)
- ❌ No test for scalar * quantity (spec example: UCUM unit multiplication rules)

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testMixedPrecisionArithmetic2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMultiply1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMultiply2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMultiply3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMultiplyEmpty1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMultiplyEmpty2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMultiplyEmpty3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testQuantity9 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 47/48 (98%) — 8 tests × 6 engines

1 test(s) fail in only one engine, suggesting engine-specific implementation issues rather than problems with the tests or specification.
