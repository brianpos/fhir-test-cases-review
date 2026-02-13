## Review Modulo
Name: mod
Date: 2026-02-11
Test Count: 10

### Specification Extract 
Header in specification: mod

Computes the remainder of the truncated division of its arguments (supported for Integer and Decimal).

### Example(s) from Specification
``` fhirpath
5 mod 2 // 1
5.5 mod 0.7 // 0.6
5 mod 0 // empty ({ })
```

### Coverage
10 tests found for `mod` (testMixedPrecisionArithmetic6, testMod1, testMod2, testMod3, testMod4, testMod5, testMod6, testModEmpty1, testModEmpty2, testModEmpty3).

**Covered:**
- ✅ Integer mod returning zero remainder (testMod1, testMod2)
- ✅ Integer mod returning non-zero remainder (testMod3)
- ✅ Decimal mod (testMod4)
- ✅ Mod by zero returns empty (testMod5)
- ✅ Negative number mod (testMod6)
- ✅ Mixed precision Integer/Decimal mod via implicit conversion (testMixedPrecisionArithmetic6)
- ✅ Empty operand returns empty (testModEmpty1, testModEmpty2, testModEmpty3)

**Gaps:**
- (none)

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testMixedPrecisionArithmetic6 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMod1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMod2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMod3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMod4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMod5 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMod6 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testModEmpty1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testModEmpty2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testModEmpty3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 58/60 (97%) — 10 tests × 6 engines

2 of 10 tests fail in 1 engine each - mod by zero and negative mod, suggesting engine-specific bugs.
