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
- ✅ Integer not-equals returning true for different values (testLiteralIntegerNotEqual, testNEquality3)
- ✅ Integer not-equals returning false for same values (testNEquality1, testNEquality9)
- ✅ String not-equals (testNEquality4, testNEquality5)
- ✅ Decimal not-equals (testNEquality6, testNEquality7)
- ✅ Decimal trailing zeros treated as equal (testNEquality8, testNEquality10)
- ✅ Date not-equals (testNEquality11, testNEquality12)
- ✅ DateTime not-equals with different precisions returns empty (testDateNotEqual, testNEquality13, testNEquality17)
- ✅ DateTime not-equals with timezone offsets (testDateNotEqualTimezoneOffsetBefore, testDateNotEqualTimezoneOffsetAfter, testDateNotEqualUTC, testNEquality18)
- ✅ DateTime not-equals with trailing zero seconds (testNEquality15, testNEquality16)
- ✅ DateTime not-equals returning true for different times (testNEquality14)
- ✅ Date not-equals with different type (date vs time) returns true (testDateNotEqualTimeSecond, testDateNotEqualTimeMinute)
- ✅ Collection not-equals with empty returns empty (testCollectionNotEqualEmpty, testNEquality2)
- ✅ Collection not-equals comparing equal collections (testNEquality19, testNEquality20)
- ✅ Collection not-equals with different order returns true (testNEquality21)
- ✅ Decimal division rounding in not-equals (testNEquality22, testNEquality23)
- ✅ Quantity not-equals with different units (testQuantity3, testNEquality24)
- ✅ Count result in not-equals (testLiteralIntegerCountNotEqual)
- ✅ Mixed precision Integer/Decimal not-equals (testMixedPrecisionNotEquals1, testMixedPrecisionNotEquals2)

**Gaps:**
- (none)

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

11 of 36 tests fail in 1-2 engines each, spread across timezone handling, empty collection semantics, trailing zero precision, and rounding, suggesting engine-specific bugs rather than test issues.
