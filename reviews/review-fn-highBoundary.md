## Review `highBoundary([precision]) : Decimal | Date | DateTime | Time` — STU
Name: highBoundary
Date: 2026-02-11
Test Count: 24

### Specification Extract 
Header in specification: highBoundary([precision: Integer]): Decimal | Date | DateTime | Time

The greatest possible value of the input to the specified precision.

The function can only be used with Decimal, Date, DateTime, and Time values, and returns the same type as the value in the input collection.

If no precision is specified, the greatest precision of the type of the input value is used (i.e. at least 8 for Decimal, 4 for Date, at least 17 for DateTime, and at least 9 for Time).

If the precision is greater than the maximum possible precision of the implementation, the result is empty *(CQL returns null)*.

If the input collection is empty, the result is empty.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

### Example(s) from Specification
``` fhirpath
1.587.highBoundary() // 1.58750000
1.587.highBoundary(6) // 1.587500
1.587.highBoundary(2) // 1.59
1.587.highBoundary(0) // 2
(-1.587).highBoundary() // -1.58650000
(-1.587).highBoundary(6) // -1.586500
(-1.587).highBoundary(2) // -1.58
(-1.587).highBoundary(0) // 1
@2014.highBoundary(6) // @2014-12
@2014-01-01T08.highBoundary(17) // @2014-01-01T08:59:59.999
@T10:30.highBoundary(9) // @T10:30:59.999
```

### Coverage
24 tests found for `highBoundary` (HighBoundaryDecimalDefault, HighBoundaryDecimal1, HighBoundaryDecimal2, HighBoundaryDecimal3, HighBoundaryDecimal4, HighBoundaryDecimal5, HighBoundaryDecimal6, HighBoundaryDecimal7, HighBoundaryDecimal8, HighBoundaryDecimal9, HighBoundaryDecimal10, HighBoundaryDecimal11, HighBoundaryDecimal12, HighBoundaryDecimal13, HighBoundaryDecimal14, HighBoundaryDecimal15, HighBoundaryDecimal16, HighBoundaryDecimal, HighBoundaryQuantity, HighBoundaryDateMonth, HighBoundaryDateTimeMillisecond1, HighBoundaryDateTimeMillisecond2, HighBoundaryDateTimeMillisecond3, HighBoundaryTimeMillisecond).

**Covered:**
- ✅ Decimal with default precision returns value to 8 decimal places (HighBoundaryDecimalDefault, HighBoundaryDecimal)
- ✅ Decimal with explicit precision less than input digits (HighBoundaryDecimal1, HighBoundaryDecimal5, HighBoundaryDecimal11)
- ✅ Decimal with explicit precision greater than input digits (HighBoundaryDecimal2, HighBoundaryDecimal6, HighBoundaryDecimal10, HighBoundaryDecimal12)
- ✅ Decimal with zero precision (HighBoundaryDecimal9)
- ✅ Negative precision returns empty (HighBoundaryDecimal3)
- ✅ Negative decimal values compute correctly (HighBoundaryDecimal4, HighBoundaryDecimal5, HighBoundaryDecimal6, HighBoundaryDecimal14, HighBoundaryDecimal16)
- ✅ Precision exceeding maximum returns empty (HighBoundaryDecimal7)
- ✅ Integer input handled via implicit conversion (HighBoundaryDecimal8)
- ✅ Multi-digit and small decimal values (HighBoundaryDecimal13, HighBoundaryDecimal15)
- ✅ Quantity input returns Quantity with same units (HighBoundaryQuantity)
- ✅ Date with month precision (HighBoundaryDateMonth)
- ✅ DateTime with millisecond precision (HighBoundaryDateTimeMillisecond1, HighBoundaryDateTimeMillisecond2, HighBoundaryDateTimeMillisecond3)
- ✅ DateTime with timezone offset preserved (HighBoundaryDateTimeMillisecond2)
- ✅ Time with millisecond precision (HighBoundaryTimeMillisecond)

**Gaps:**
- ❌ Empty input returns empty
- ❌ Multiple items in input signals error
- ❌ Date with default precision (4)
- ❌ DateTime with default precision (17)
- ❌ Time with default precision (9)

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| HighBoundaryDecimalDefault | N/A | N/A | ✅ | ✅ | ✅ | ✅ |
| HighBoundaryDecimal1 | N/A | N/A | ❌ | ✅ | ✅ | ✅ |
| HighBoundaryDecimal2 | N/A | N/A | ✅ | ✅ | ✅ | ✅ |
| HighBoundaryDecimal3 | N/A | N/A | ❌ | ❌ | ✅ | ✅ |
| HighBoundaryDecimal4 | N/A | N/A | ✅ | ✅ | ✅ | ✅ |
| HighBoundaryDecimal5 | N/A | N/A | ❌ | ✅ | ✅ | ✅ |
| HighBoundaryDecimal6 | N/A | N/A | ✅ | ✅ | ✅ | ✅ |
| HighBoundaryDecimal7 | N/A | N/A | ❌ | ✅ | ✅ | ✅ |
| HighBoundaryDecimal8 | N/A | N/A | ❌ | ✅ | ✅ | ✅ |
| HighBoundaryDecimal9 | N/A | N/A | ❌ | ✅ | ✅ | ✅ |
| HighBoundaryDecimal10 | N/A | N/A | ✅ | ✅ | ✅ | ✅ |
| HighBoundaryDecimal11 | N/A | N/A | ❌ | ✅ | ✅ | ✅ |
| HighBoundaryDecimal12 | N/A | N/A | ✅ | ✅ | ✅ | ✅ |
| HighBoundaryDecimal13 | N/A | N/A | ✅ | ✅ | ✅ | ✅ |
| HighBoundaryDecimal14 | N/A | N/A | ✅ | ✅ | ✅ | ✅ |
| HighBoundaryDecimal15 | N/A | N/A | ❌ | ✅ | ✅ | ✅ |
| HighBoundaryDecimal16 | N/A | N/A | ❌ | ✅ | ✅ | ✅ |
| HighBoundaryDecimal | N/A | N/A | ✅ | ✅ | ✅ | ✅ |
| HighBoundaryQuantity | N/A | N/A | ✅ | ✅ | ✅ | ✅ |
| HighBoundaryDateMonth | N/A | N/A | ❌ | ✅ | ✅ | ✅ |
| HighBoundaryDateTimeMillisecond1 | N/A | N/A | ❌ | ✅ | ✅ | ✅ |
| HighBoundaryDateTimeMillisecond2 | ❌ | N/A | ✅ | ✅ | ✅ | ✅ |
| HighBoundaryDateTimeMillisecond3 | N/A | N/A | ❌ | ✅ | ✅ | ✅ |
| HighBoundaryTimeMillisecond | N/A | N/A | ✅ | ✅ | ✅ | ✅ |

**Summary:** 83/144 (58%) — 24 tests × 6 engines

58% pass rate with widespread failures. Several engines have not implemented highBoundary, and among those that have, failures occur on precision edge cases (negative precision, zero precision, boundary of max precision) and DateTime boundary calculations.
