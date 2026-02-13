## Review Not Equals
Name: !=
Date: 2026-02-11
Test Count: 36

### Specification Extract 
Header in specification: != (Not Equals)

The converse of the equals operator, returning `true` if equal returns `false`; `false` if equal returns `true`; and empty (`{ }`) if equal returns empty. In other words, `A != B` is short-hand for `(A = B).not()`.

### Example(s) from Specification
_No examples found in specification._

### Coverage
36 tests found for `!=` (testLiteralIntegerNotEqual, testLiteralIntegerCountNotEqual, testDateNotEqual, testDateNotEqualTimezoneOffsetBefore, testDateNotEqualTimezoneOffsetAfter, testDateNotEqualUTC, testDateNotEqualTimeSecond, testDateNotEqualTimeMinute, testCollectionNotEqualEmpty, testQuantity3, testNEquality1, testNEquality2, testNEquality3, testNEquality4, testNEquality5, testNEquality6, testNEquality7, testNEquality8, testNEquality9, testNEquality10, testNEquality11, testNEquality12, testNEquality13, testNEquality14, testNEquality15, testNEquality16, testNEquality17, testNEquality18, testNEquality19, testNEquality20, testNEquality21, testNEquality22, testNEquality23, testNEquality24, testMixedPrecisionNotEquals1, testMixedPrecisionNotEquals2).

**Covered:**
- ✅ Integer != comparisons with negatives and zero (testLiteralIntegerNotEqual, testLiteralIntegerCountNotEqual, testNEquality1, testNEquality3, testNEquality9, testNEquality10)
- ✅ Decimal != comparisons including trailing zeroes (testNEquality6, testNEquality7, testNEquality8, testNEquality22, testNEquality23)
- ✅ String != comparisons (testNEquality4, testNEquality5)
- ✅ Date != comparisons including different precisions returning empty (testNEquality11, testNEquality12, testNEquality13, testDateNotEqual, testDateNotEqualTimezoneOffsetBefore, testDateNotEqualTimezoneOffsetAfter, testDateNotEqualUTC)
- ✅ DateTime != with timezone handling (testNEquality14, testNEquality15, testNEquality16, testNEquality17, testNEquality18)
- ✅ Date != Time returns true (testDateNotEqualTimeSecond, testDateNotEqualTimeMinute)
- ✅ Quantity != with unit mismatch (testQuantity3, testNEquality24)
- ✅ Collection != comparisons with order sensitivity (testNEquality19, testNEquality20, testNEquality21)
- ✅ Mixed precision integer/decimal (testMixedPrecisionNotEquals1, testMixedPrecisionNotEquals2)
- ✅ Empty collection behavior (testNEquality2, testCollectionNotEqualEmpty)

**Gaps:**
- ❌ No test for boolean != comparisons

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testLiteralIntegerNotEqual | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLiteralIntegerCountNotEqual | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDateNotEqual | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDateNotEqualTimezoneOffsetBefore | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDateNotEqualTimezoneOffsetAfter | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDateNotEqualUTC | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDateNotEqualTimeSecond | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDateNotEqualTimeMinute | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testCollectionNotEqualEmpty | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testQuantity3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNEquality1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNEquality2 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNEquality3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNEquality4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNEquality5 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNEquality6 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNEquality7 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNEquality8 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNEquality9 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNEquality10 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNEquality11 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNEquality12 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNEquality13 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNEquality14 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNEquality15 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNEquality16 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNEquality17 | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| testNEquality18 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNEquality19 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNEquality20 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNEquality21 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNEquality22 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNEquality23 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNEquality24 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMixedPrecisionNotEquals1 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMixedPrecisionNotEquals2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 204/216 (94%) — 36 tests × 6 engines

10 test(s) fail in only one engine, suggesting engine-specific implementation issues rather than problems with the tests or specification. 1 test(s) fail in multiple (but not all) engines, which may indicate differing interpretations of the specification.
