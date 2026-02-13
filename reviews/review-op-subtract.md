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
- ✅ Mixed precision Integer/Decimal subtraction (testMixedPrecisionArithmetic4)
- ✅ Date minus duration quantity (testMinus5)
- ✅ Incompatible quantity subtraction from date signals error (testMinus6)
- ✅ String subtraction signals error (testMinus4)
- ✅ Time minus duration wraps around (testMinus7, testMinus8)
- ✅ Empty operand returns empty (testMinusEmpty1, testMinusEmpty2, testMinusEmpty3)

**Gaps:**
- ❌ Quantity subtraction with same dimensions but different units (e.g. 3 'm' - 3 'cm' = 297 'cm')
- ❌ Arithmetic overflow/underflow returning empty

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testMixedPrecisionArithmetic4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
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

**Summary:** 63/72 (88%) — 12 tests × 6 engines

4 of 12 tests fail in 1-3 engines — date minus month and time minus hours wrapping have the most failures (3/6 pass), suggesting possible spec ambiguity or inconsistent engine implementations for temporal arithmetic edge cases.
