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
- ✅ Integer <= comparisons: less-than, equal, greater-than cases (testLessOrEqual1, testLessOrEqual8, testLessOrEqual15)
- ✅ Decimal <= comparisons (testLessOrEqual2, testLessOrEqual9, testLessOrEqual16)
- ✅ String <= comparisons with case sensitivity (testLessOrEqual3, testLessOrEqual4, testLessOrEqual10, testLessOrEqual11, testLessOrEqual17, testLessOrEqual18)
- ✅ Date <= comparisons (testLessOrEqual5, testLessOrEqual12, testLessOrEqual19)
- ✅ DateTime <= comparisons (testLessOrEqual6, testLessOrEqual13, testLessOrEqual20)
- ✅ Time <= comparisons (testLessOrEqual7, testLessOrEqual14, testLessOrEqual21)
- ✅ Quantity <= with unit conversion (testLessOrEqual22)
- ✅ Mixed precision integer/decimal implicit conversion (testMixedPrecisionLessOrEqual1, testMixedPrecisionLessOrEqual2)
- ✅ Different precision dates/dateTimes/times return empty (testLessOrEqual23, testLessOrEqual24, testLessOrEqual25)
- ✅ Trailing zeroes in dateTime/time ignored for equality (testLessOrEqual26, testLessOrEqual27)
- ✅ Empty collection propagation (testLessOrEqualEmpty1, testLessOrEqualEmpty2, testLessOrEqualEmpty3)

**Gaps:**
- ❌ No test for timezone-aware comparison (spec example: `@2018-01-01T16:00:00+11:00 <= @2018-01-01T15:00:00.0+10:00`)
- ❌ No test for multi-character string comparison (spec example: `'abc' <= 'ABC'`)

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testLessOrEqual1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
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
| testLessOrEqual2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqual20 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqual21 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqual22 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqual23 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqual24 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqual25 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqual26 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqual27 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqual3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqual4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqual5 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqual6 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqual7 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqual8 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqual9 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqualEmpty1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqualEmpty2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLessOrEqualEmpty3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMixedPrecisionLessOrEqual1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMixedPrecisionLessOrEqual2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 189/192 (98%) — 32 tests × 6 engines

3 test(s) fail in only one engine, suggesting engine-specific implementation issues rather than problems with the tests or specification.
