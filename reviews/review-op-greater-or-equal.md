## Review Greater or Equal
Name: >=
Date: 2026-02-11
Test Count: 32

### Specification Extract 
Header in specification: &gt;= (Greater or Equal)

The greater or equal operator (`>=`) returns `true` if the first operand is greater than or equal to the second. The operands must be of the same type, or convertible to the same type using implicit conversion.

### Example(s) from Specification
``` fhirpath
10 >= 5 // true
10 >= 5.0 // true - note the 10 is converted to a decimal to perform the comparison
'abc' >= 'ABC' // true
4 'm' >= 4 'cm' // true (or { } if the implementation does not support unit conversion)

@2018-03-01 >= @2018-01-01 // true
@2018-01-01 >= @2018-01-01 // true - equal with same precision
@2018-03 >= @2018-03-01 // empty ({ }) - different precisions
@2018-03-01T10:30:00 >= @2018-03-01T10:00:00 // true
@2018-03-01T10 >= @2018-03-01T10:30 // empty ({ }) - different precisions
@2018-03-01T10:30:00 >= @2018-03-01T10:30:00.0 // true - values are equal to seconds, trailing zeroes after the decimal are ignored

@T10:30:00 >= @T10:00:00 // true
@T10 >= @T10:30 // empty ({ }) - different precisions
@T10:30:00 >= @T10:30:00.0 // true - values are equal to seconds, trailing zeroes after the decimal are ignored
```

### Coverage
32 tests found for `>=` (testMixedPrecisionGreaterOrEqual1, testMixedPrecisionGreaterOrEqual2, testGreatorOrEqual1, testGreatorOrEqual2, testGreatorOrEqual3, testGreatorOrEqual4, testGreatorOrEqual5, testGreatorOrEqual6, testGreatorOrEqual7, testGreatorOrEqual8, testGreatorOrEqual9, testGreatorOrEqual10, testGreatorOrEqual11, testGreatorOrEqual12, testGreatorOrEqual13, testGreatorOrEqual14, testGreatorOrEqual15, testGreatorOrEqual16, testGreatorOrEqual17, testGreatorOrEqual18, testGreatorOrEqual19, testGreatorOrEqual20, testGreatorOrEqual21, testGreatorOrEqual22, testGreatorOrEqual23, testGreatorOrEqual24, testGreatorOrEqual25, testGreatorOrEqual26, testGreatorOrEqual27, testGreatorOrEqualEmpty1, testGreatorOrEqualEmpty2, testGreatorOrEqualEmpty3).

**Covered:**
- ✅ Integer >= comparison for less, equal, and greater cases (testGreatorOrEqual1, testGreatorOrEqual8, testGreatorOrEqual15)
- ✅ Decimal >= comparison (testGreatorOrEqual2, testGreatorOrEqual9, testGreatorOrEqual16)
- ✅ String >= comparison is case-sensitive and lexical (testGreatorOrEqual3, testGreatorOrEqual4, testGreatorOrEqual10, testGreatorOrEqual11, testGreatorOrEqual17, testGreatorOrEqual18)
- ✅ Date >= comparison (testGreatorOrEqual5, testGreatorOrEqual12, testGreatorOrEqual19)
- ✅ DateTime >= comparison (testGreatorOrEqual6, testGreatorOrEqual13, testGreatorOrEqual20)
- ✅ Time >= comparison (testGreatorOrEqual7, testGreatorOrEqual14, testGreatorOrEqual21)
- ✅ Quantity >= comparison with unit conversion (testGreatorOrEqual22)
- ✅ Mixed precision implicit conversion between Integer and Decimal (testMixedPrecisionGreaterOrEqual1, testMixedPrecisionGreaterOrEqual2)
- ✅ Different precisions return empty for date, dateTime, and time (testGreatorOrEqual23, testGreatorOrEqual24, testGreatorOrEqual25)
- ✅ Trailing zeroes after decimal are ignored in dateTime and time (testGreatorOrEqual26, testGreatorOrEqual27)
- ✅ Empty operand handling returns empty (testGreatorOrEqualEmpty1, testGreatorOrEqualEmpty2, testGreatorOrEqualEmpty3)

**Gaps:**
- ❌ DateTime with timezone offset comparison (spec preamble requires respecting timezone offsets)
- ❌ Quantity with same-dimension cross-unit conversion (e.g., 4 'm' >= 4 'cm')

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testMixedPrecisionGreaterOrEqual1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMixedPrecisionGreaterOrEqual2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreatorOrEqual1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreatorOrEqual2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreatorOrEqual3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreatorOrEqual4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreatorOrEqual5 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreatorOrEqual6 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreatorOrEqual7 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreatorOrEqual8 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreatorOrEqual9 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreatorOrEqual10 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreatorOrEqual11 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreatorOrEqual12 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreatorOrEqual13 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreatorOrEqual14 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreatorOrEqual15 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreatorOrEqual16 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreatorOrEqual17 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreatorOrEqual18 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreatorOrEqual19 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreatorOrEqual20 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreatorOrEqual21 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreatorOrEqual22 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreatorOrEqual23 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreatorOrEqual24 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreatorOrEqual25 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreatorOrEqual26 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreatorOrEqual27 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreatorOrEqualEmpty1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreatorOrEqualEmpty2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testGreatorOrEqualEmpty3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 189/192 (98%) — 32 tests × 6 engines

Three tests fail on a single engine each: quantity comparison and trailing zero handling, suggesting engine-specific bugs.
