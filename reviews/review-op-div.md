## Review Truncated division
Name: div
Date: 2026-02-11
Test Count: 10

### Specification Extract 
Header in specification: div

Performs truncated division of the left operand by the right operand (supported for Integer and Decimal). In other words, the division that ignores any remainder:

### Example(s) from Specification
``` fhirpath
5 div 2 // 2
5.5 div 0.7 // 7
5 div 0 // empty ({ })
```

### Coverage
10 tests found for `div` (testMixedPrecisionArithmetic5, testDiv1, testDiv2, testDiv3, testDiv4, testDiv5, testDiv6, testDivEmpty1, testDivEmpty2, testDivEmpty3).

**Covered:**
- ✅ Integer truncated division (testDiv1, testDiv2, testDiv3)
- ✅ Decimal truncated division (testDiv4)
- ✅ Division by zero returns empty collection (testDiv5)
- ✅ Negative number truncated division (testDiv6)
- ✅ Mixed precision: integer div decimal (testMixedPrecisionArithmetic5)
- ✅ Empty operand propagation (testDivEmpty1, testDivEmpty2, testDivEmpty3)

**Gaps:**
- (none)

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testMixedPrecisionArithmetic5 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDiv1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDiv2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDiv3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDiv4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDiv5 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDiv6 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDivEmpty1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDivEmpty2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDivEmpty3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 58/60 (97%) — 10 tests × 6 engines

testDiv5 (division by zero) and testDiv6 (negative truncated division) each fail on single engines, suggesting engine-specific bugs.
