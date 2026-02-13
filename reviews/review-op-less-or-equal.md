## Review Less or Equal
Name: <=
Date: 2026-02-11
Test Count: 32

### Specification Extract 
Header in specification: &lt;= (Less or Equal)

The less or equal operator (`<=`) returns `true` if the first operand is less than or equal to the second. The operands must be of the same type, or convertible to the same type using implicit conversion.

### Example(s) from Specification
``` fhirpath
10 <= 5 // false
10 <= 5.0 // false - note the 10 is converted to a decimal to perform the comparison
'abc' <= 'ABC' // false
4 'm' <= 4 'cm' // false (or { } if the implementation does not support unit conversion)

@2018-03-01 <= @2018-01-01 // false
@2018-01-01 <= @2018-01-01 // true - equal with same precision
@2018-03 <= @2018-03-01 // empty ({ }) - different precisions
@2018-03-01T10:30:00 <= @2018-03-01T10:00:00 // false
@2018-03-01T10 <= @2018-03-01T10:30 // empty ({ }) - different precisions
@2018-03-01T10:30:00 <= @2018-03-01T10:30:00.0 // true - values are equal to seconds, trailing zeroes after the decimal are ignored

@2018-01-01T16:00:00+11:00 <= @2018-01-01T15:00:00.0+10:00 // true (same moment in diff timezones)
@2018-01-01T16:00:00+12:00 <= @2018-01-01T15:00:00.0+10:00 // true (4pm+12 is less than 5pm+10 when timezones are considered)

@T10:30:00 <= @T10:00:00 // false
@T10 <= @T10:30 // empty ({ }) - different precisions
@T10:30:00 <= @T10:30:00.0 // true
```

### Coverage
32 tests found for `<=` (testMixedPrecisionLessOrEqual1, testMixedPrecisionLessOrEqual2, testLessOrEqual1, testLessOrEqual2, testLessOrEqual3, testLessOrEqual4, testLessOrEqual5, testLessOrEqual6, testLessOrEqual7, testLessOrEqual8, testLessOrEqual9, testLessOrEqual10, testLessOrEqual11, testLessOrEqual12, testLessOrEqual13, testLessOrEqual14, testLessOrEqual15, testLessOrEqual16, testLessOrEqual17, testLessOrEqual18, testLessOrEqual19, testLessOrEqual20, testLessOrEqual21, testLessOrEqual22, testLessOrEqual23, testLessOrEqual24, testLessOrEqual25, testLessOrEqual26, testLessOrEqual27, testLessOrEqualEmpty1, testLessOrEqualEmpty2, testLessOrEqualEmpty3).

**Covered:**
- ✅ Integer <= comparison for less, equal, and greater cases (testLessOrEqual1, testLessOrEqual8, testLessOrEqual15)
- ✅ Decimal <= comparison (testLessOrEqual2, testLessOrEqual9, testLessOrEqual16)
- ✅ String <= comparison is case-sensitive and lexical (testLessOrEqual3, testLessOrEqual4, testLessOrEqual10, testLessOrEqual11, testLessOrEqual17, testLessOrEqual18)
- ✅ Date <= comparison (testLessOrEqual5, testLessOrEqual12, testLessOrEqual19)
- ✅ DateTime <= comparison (testLessOrEqual6, testLessOrEqual13, testLessOrEqual20)
- ✅ Time <= comparison (testLessOrEqual7, testLessOrEqual14, testLessOrEqual21)
- ✅ Quantity <= comparison with unit conversion (testLessOrEqual22)
- ✅ Mixed precision implicit conversion between Integer and Decimal (testMixedPrecisionLessOrEqual1, testMixedPrecisionLessOrEqual2)
- ✅ Different precisions return empty for date, dateTime, and time (testLessOrEqual23, testLessOrEqual24, testLessOrEqual25)
- ✅ Trailing zeroes after decimal are ignored in dateTime and time (testLessOrEqual26, testLessOrEqual27)
- ✅ Empty operand handling returns empty (testLessOrEqualEmpty1, testLessOrEqualEmpty2, testLessOrEqualEmpty3)

**Gaps:**
- ❌ DateTime with timezone offset comparison (spec examples include timezone offset cases)
- ❌ Quantity with same-dimension cross-unit conversion (e.g., 4 'm' <= 4 'cm')

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testMixedPrecisionLessOrEqual1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMixedPrecisionLessOrEqual2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqual1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqual2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqual3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqual4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqual5 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqual6 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqual7 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqual8 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqual9 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqual10 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqual11 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqual12 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqual13 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqual14 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqual15 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqual16 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqual17 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqual18 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqual19 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqual20 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqual21 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqual22 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqual23 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqual24 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqual25 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqual26 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqual27 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqualEmpty1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqualEmpty2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqualEmpty3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 189/192 (98%) — 32 tests × 6 engines

Three tests fail on a single engine each: quantity comparison and trailing zero handling, suggesting engine-specific bugs.
