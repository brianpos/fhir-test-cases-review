## Review Subtraction
Name: -
Date: 2026-02-11
Test Count: 12

### Specification Extract 
Header in specification: - (subtraction)

Subtracts the right operand from the left operand (supported for Integer, Decimal, and Quantity).

When subtracting quantities, the dimensions of each quantity must be the same, but not necessarily the unit.

### Example(s) from Specification
``` fhirpath
3 'm' - 3 'cm' // 297 'cm'
```

### Coverage
12 tests found for `-` (testMixedPrecisionArithmetic4, testMinus1, testMinus2, testMinus3, testMinus4, testMinus5, testMinus6, testMinus7, testMinus8, testMinusEmpty1, testMinusEmpty2, testMinusEmpty3).

**Covered:**
- ✅ Integer subtraction (testMinus1, testMinus2)
- ✅ Decimal subtraction (testMinus3)
- ✅ Mixed precision decimal - integer (testMixedPrecisionArithmetic4)
- ✅ String subtraction returns execution error (testMinus4)
- ✅ Date - duration quantity (testMinus5)
- ✅ Time - duration with wrapping past midnight (testMinus7, testMinus8)
- ✅ Date - incompatible unit returns execution error (testMinus6)
- ✅ Empty collection propagation (testMinusEmpty1, testMinusEmpty2, testMinusEmpty3)

**Gaps:**
- ❌ No test for quantity - quantity with same dimensions (spec example: `3 'm' - 3 'cm'`)

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testMinus1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMinus2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMinus3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMinus4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMinus5 | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| testMinus6 | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ |
| testMinus7 | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| testMinus8 | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| testMinusEmpty1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMinusEmpty2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMinusEmpty3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMixedPrecisionArithmetic4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 63/72 (88%) — 12 tests × 6 engines

1 test(s) fail in only one engine, suggesting engine-specific implementation issues rather than problems with the tests or specification. 3 test(s) fail in multiple (but not all) engines, which may indicate differing interpretations of the specification.
