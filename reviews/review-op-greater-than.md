## Review Greater Than
Name: >
Date: 2026-02-11
Test Count: 41

### Specification Extract 
Header in specification: &gt; (Greater Than)

The greater than operator (`>`) returns `true` if the first operand is strictly greater than the second. The operands must be of the same type, or convertible to the same type using an implicit conversion.

### Example(s) from Specification
``` fhirpath
10 > 5 // true
10 > 5.0 // true; note the 10 is converted to a decimal to perform the comparison
'abc' > 'ABC' // true
4 'm' > 4 'cm' // true (or { } if the implementation does not support unit conversion)

@2018-03-01 > @2018-01-01 // true - same precision
@2018-03 > @2018-03-01 // empty ({ }) - different precisions
@2018-03-01T10:30:00 > @2018-03-01T10:00:00 // true
@2018-03-01T10 > @2018-03-01T10:30 // empty ({ }) - different precisions
@2018-03-01T10:30:00 > @2018-03-01T10:30:00.0 // false (values are equal to seconds, trailing zeroes after the decimal are ignored)

@T10:30:00 > @T10:00:00 // true
@T10 > @T10:30 // empty ({ }) - different precisions
@T10:30:00 > @T10:30:00.0 // false - values are equal to seconds, trailing zeroes after the decimal are ignored
```

### Coverage
41 tests found for `>` (testLiteralIntegerGreaterThan, testLiteralDecimalGreaterThanNonZeroTrue, testLiteralDecimalGreaterThanZeroTrue, testLiteralDecimalGreaterThanIntegerTrue, testDateTimeGreaterThanDate1, testDateGreaterThanDate, testDateTimeGreaterThanDate2, testLiteralDateTimeTZGreater, testQuantity8, testMixedPrecisionGreaterThan1, testMixedPrecisionGreaterThan2, testGreaterThan1, testGreaterThan2, testGreaterThan3, testGreaterThan4, testGreaterThan5, testGreaterThan6, testGreaterThan7, testGreaterThan8, testGreaterThan9, testGreaterThan10, testGreaterThan11, testGreaterThan12, testGreaterThan13, testGreaterThan14, testGreaterThan15, testGreaterThan16, testGreaterThan17, testGreaterThan18, testGreaterThan19, testGreaterThan20, testGreaterThan21, testGreaterThan22, testGreaterThan23, testGreaterThan24, testGreaterThan25, testGreaterThan26, testGreaterThan27, testGreaterThanEmpty1, testGreaterThanEmpty2, testGreaterThanEmpty3).

**Covered:**
- ✅ Integer > comparison for less, equal, and greater cases (testGreaterThan1, testGreaterThan8, testGreaterThan15, testLiteralIntegerGreaterThan)
- ✅ Decimal > comparison (testGreaterThan2, testGreaterThan9, testGreaterThan16, testLiteralDecimalGreaterThanNonZeroTrue, testLiteralDecimalGreaterThanZeroTrue)
- ✅ String > comparison is case-sensitive and lexical (testGreaterThan3, testGreaterThan4, testGreaterThan10, testGreaterThan11, testGreaterThan17, testGreaterThan18)
- ✅ Date > comparison (testGreaterThan5, testGreaterThan12, testGreaterThan19, testDateGreaterThanDate)
- ✅ DateTime > comparison including timezone offset (testGreaterThan6, testGreaterThan13, testGreaterThan20, testDateTimeGreaterThanDate1, testLiteralDateTimeTZGreater)
- ✅ DateTime vs Date comparison returns empty for different precision (testDateTimeGreaterThanDate2)
- ✅ Time > comparison (testGreaterThan7, testGreaterThan14, testGreaterThan21)
- ✅ Quantity > with unit conversion (testGreaterThan22, testQuantity8)
- ✅ Mixed precision implicit conversion (testMixedPrecisionGreaterThan1, testMixedPrecisionGreaterThan2, testLiteralDecimalGreaterThanIntegerTrue)
- ✅ Different precisions return empty (testGreaterThan23, testGreaterThan24, testGreaterThan25)
- ✅ Trailing zeroes after decimal are ignored (testGreaterThan26, testGreaterThan27)
- ✅ Empty operand handling returns empty (testGreaterThanEmpty1, testGreaterThanEmpty2, testGreaterThanEmpty3)

**Gaps:**
- (none)

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testLiteralIntegerGreaterThan | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLiteralDecimalGreaterThanNonZeroTrue | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLiteralDecimalGreaterThanZeroTrue | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLiteralDecimalGreaterThanIntegerTrue | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDateTimeGreaterThanDate1 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDateGreaterThanDate | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDateTimeGreaterThanDate2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLiteralDateTimeTZGreater | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testQuantity8 | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ |
| testMixedPrecisionGreaterThan1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMixedPrecisionGreaterThan2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreaterThan1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreaterThan2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreaterThan3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreaterThan4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreaterThan5 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreaterThan6 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreaterThan7 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreaterThan8 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreaterThan9 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreaterThan10 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreaterThan11 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreaterThan12 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreaterThan13 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreaterThan14 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreaterThan15 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreaterThan16 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreaterThan17 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreaterThan18 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreaterThan19 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreaterThan20 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreaterThan21 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreaterThan22 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreaterThan23 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreaterThan24 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreaterThan25 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreaterThan26 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreaterThan27 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreaterThanEmpty1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreaterThanEmpty2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreaterThanEmpty3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 239/246 (97%) — 41 tests × 6 engines

Failures are mostly single-engine. testQuantity8 (8 days > 1 week) fails on 2 engines, likely due to calendar duration unit conversion support differences.
