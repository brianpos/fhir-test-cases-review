## Review Less Than
Name: <
Date: 2026-02-11
Test Count: 39

### Specification Extract 
Header in specification: &lt; (Less Than)

The less than operator (`<`) returns `true` if the first operand is strictly less than the second. The operands must be of the same type, or convertible to the same type using implicit conversion.

### Example(s) from Specification
``` fhirpath
10 < 5 // false
10 < 5.0 // false - note the 10 is converted to a decimal to perform the comparison
'abc' < 'ABC' // false
4 'm' < 4 'cm' // false (or { } if the implementation does not support unit conversion)

@2018-03-01 < @2018-01-01 // false
@2018-01-01 < @2018-01-01 // false - same precision
@2018-03 < @2018-03-01 // empty ({ }) - different precisions
@2018-03-01T10:30:00 < @2018-03-01T10:00:00 // false
@2018-03-01T10 < @2018-03-01T10:30 // empty ({ }) - different precisions
@2018-03-01T10:30:00 < @2018-03-01T10:30:00.0 // false - values are equal to seconds, trailing zeroes after the decimal are ignored

@2018-01-01T16:00:00+11:00 < @2018-01-01T15:00:00.0+10:00 // false (same moment in diff timezones)
@2018-01-01T16:00:00+12:00 < @2018-01-01T15:00:00.0+10:00 // true (4pm+12 is less than 5pm+10 when timezones are considered)

@T10:30:00 < @T10:00:00 // false
@T10 < @T10:30 // empty ({ }) - different precisions
@T10:30:00 < @T10:30:00.0 // false - values are equal to seconds, trailing zeroes after the decimal are ignored
```

### Coverage
39 tests found for `<` (testLiteralIntegerLessThanTrue, testLiteralIntegerLessThanFalse, testLiteralDecimalLessThanInteger, testLiteralDecimalLessThanInvalid, testDateNotEqualToday, testLiteralDateTimeTZLess, testQuantity7, testMixedPrecisionLessThan1, testMixedPrecisionLessThan2, testLessThan1, testLessThan2, testLessThan3, testLessThan4, testLessThan5, testLessThan6, testLessThan7, testLessThan8, testLessThan9, testLessThan10, testLessThan11, testLessThan12, testLessThan13, testLessThan14, testLessThan15, testLessThan16, testLessThan17, testLessThan18, testLessThan19, testLessThan20, testLessThan21, testLessThan22, testLessThan23, testLessThan24, testLessThan25, testLessThan26, testLessThan27, testLessThanEmpty1, testLessThanEmpty2, testLessThanEmpty3).

**Covered:**
- ✅ Integer < comparisons: less-than, equal, greater-than cases (testLiteralIntegerLessThanTrue, testLiteralIntegerLessThanFalse, testLessThan1, testLessThan8, testLessThan15)
- ✅ Decimal < comparisons (testLessThan2, testLessThan9, testLessThan16, testLiteralDecimalLessThanInteger)
- ✅ String < comparisons with case sensitivity (testLessThan3, testLessThan4, testLessThan10, testLessThan11, testLessThan17, testLessThan18)
- ✅ Date < comparisons (testLessThan5, testLessThan12, testLessThan19, testDateNotEqualToday)
- ✅ DateTime < comparisons with timezone (testLessThan6, testLessThan13, testLessThan20, testLiteralDateTimeTZLess)
- ✅ Time < comparisons (testLessThan7, testLessThan14, testLessThan21)
- ✅ Quantity < with unit conversion (testLessThan22, testQuantity7)
- ✅ Mixed precision integer/decimal implicit conversion (testMixedPrecisionLessThan1, testMixedPrecisionLessThan2)
- ✅ Type mismatch returns execution error (testLiteralDecimalLessThanInvalid)
- ✅ Different precision dates/dateTimes/times return empty (testLessThan23, testLessThan24, testLessThan25)
- ✅ Trailing zeroes in dateTime/time ignored (testLessThan26, testLessThan27)
- ✅ Empty collection propagation (testLessThanEmpty1, testLessThanEmpty2, testLessThanEmpty3)

**Gaps:**
- ❌ No test for multi-character string comparison (spec example: `'abc' < 'ABC'`)

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testDateNotEqualToday | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessThan1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessThan10 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessThan11 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessThan12 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessThan13 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessThan14 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessThan15 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessThan16 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessThan17 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessThan18 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessThan19 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessThan2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessThan20 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessThan21 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessThan22 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessThan23 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessThan24 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessThan25 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessThan26 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessThan27 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessThan3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessThan4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessThan5 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessThan6 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessThan7 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessThan8 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessThan9 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessThanEmpty1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessThanEmpty2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessThanEmpty3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLiteralDateTimeTZLess | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLiteralDecimalLessThanInteger | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLiteralDecimalLessThanInvalid | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLiteralIntegerLessThanFalse | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLiteralIntegerLessThanTrue | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMixedPrecisionLessThan1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMixedPrecisionLessThan2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testQuantity7 | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ |

**Summary:** 228/234 (97%) — 39 tests × 6 engines

4 test(s) fail in only one engine, suggesting engine-specific implementation issues rather than problems with the tests or specification. 1 test(s) fail in multiple (but not all) engines, which may indicate differing interpretations of the specification.
