## Review `lowBoundary([precision]) : Decimal | Date | DateTime | Time` — STU
Name: lowBoundary
Date: 2026-02-11
Test Count: 28

### Specification Extract 
Header in specification: lowBoundary([precision: Integer]): Decimal | Date | DateTime | Time

The least possible value of the input to the specified precision.

The function can only be used with Decimal, Date, DateTime, and Time values, and returns the same type as the value in the input collection.

If no precision is specified, the greatest precision of the type of the input value is used (i.e. at least 8 for Decimal, 4 for Date, at least 17 for DateTime, and at least 9 for Time).

If the precision is greater than the maximum possible precision of the implementation, the result is empty *(CQL returns null)*.

If the input collection is empty, the result is empty.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

### Example(s) from Specification
``` fhirpath
1.587.lowBoundary() // 1.58650000
1.587.lowBoundary(6) // 1.586500
1.587.lowBoundary(2) // 1.58
1.587.lowBoundary(0) // 1
(-1.587).lowBoundary() // -1.58750000
(-1.587).lowBoundary(6) // -1.587500
(-1.587).lowBoundary(2) // -1.59
(-1.587).lowBoundary(0) // -2
@2014.lowBoundary(6) // @2014-01
@2014-01-01T08.lowBoundary(17) // @2014-01-01T08:00:00.000
@T10:30.lowBoundary(9) // @T10:30:00.000
```

### Coverage

28 tests found for `lowBoundary` (LowBoundaryDecimalDefault, LowBoundaryDecimal1, LowBoundaryDecimal2, LowBoundaryDecimal3, LowBoundaryDecimal4, LowBoundaryDecimal5, LowBoundaryDecimal6, LowBoundaryDecimal7, LowBoundaryDecimal8, LowBoundaryDecimal9, LowBoundaryDecimal10, LowBoundaryDecimal11, LowBoundaryDecimal12, LowBoundaryDecimal13, LowBoundaryDecimal14, LowBoundaryDecimal15, LowBoundaryNegDecimalDefault, LowBoundaryNegDecimal1, LowBoundaryNegDecimal2, LowBoundaryNegDecimal3, LowBoundaryNegDecimal4, LowBoundaryNegDecimal5, LowBoundaryQuantity, LowBoundaryDateMonth, LowBoundaryDateTimeMillisecond1, LowBoundaryDateTimeMillisecond2, LowBoundaryDateTimeMillisecond3, LowBoundaryTimeMillisecond).

**Covered:**
- ✅ Decimal with default and explicit precision, including zero precision (LowBoundaryDecimalDefault, LowBoundaryDecimal1, LowBoundaryDecimal2, LowBoundaryDecimal4, LowBoundaryDecimal7, LowBoundaryDecimal8, LowBoundaryDecimal9, LowBoundaryDecimal10, LowBoundaryDecimal11, LowBoundaryDecimal12, LowBoundaryDecimal14, LowBoundaryDecimal15)
- ✅ Negative decimal values with default and explicit precision (LowBoundaryNegDecimalDefault, LowBoundaryNegDecimal1, LowBoundaryNegDecimal2, LowBoundaryNegDecimal4, LowBoundaryDecimal13)
- ✅ Precision exceeding max implementation precision returns empty (LowBoundaryDecimal5, LowBoundaryDecimal6, LowBoundaryNegDecimal5)
- ✅ Negative precision returns empty (LowBoundaryDecimal3, LowBoundaryNegDecimal3)
- ✅ Quantity type support (LowBoundaryQuantity)
- ✅ Date type with month precision (LowBoundaryDateMonth)
- ✅ DateTime type with millisecond precision and timezone handling (LowBoundaryDateTimeMillisecond1, LowBoundaryDateTimeMillisecond2, LowBoundaryDateTimeMillisecond3)
- ✅ Time type with millisecond precision (LowBoundaryTimeMillisecond)

**Gaps:**
- ❌ Empty input collection returning empty
- ❌ Multiple items in input collection signaling error

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| LowBoundaryDateMonth | N/A | N/A | ❌ | ✅ | ✅ | ✅ |
| LowBoundaryDateTimeMillisecond1 | N/A | N/A | ❌ | ✅ | ✅ | ✅ |
| LowBoundaryDateTimeMillisecond2 | N/A | N/A | ✅ | ✅ | ✅ | ✅ |
| LowBoundaryDateTimeMillisecond3 | N/A | N/A | ❌ | ✅ | ✅ | ✅ |
| LowBoundaryDecimal1 | N/A | N/A | ✅ | ✅ | ✅ | ✅ |
| LowBoundaryDecimal10 | N/A | N/A | ❌ | ✅ | ✅ | ✅ |
| LowBoundaryDecimal11 | N/A | N/A | ✅ | ✅ | ✅ | ✅ |
| LowBoundaryDecimal12 | N/A | N/A | ✅ | ✅ | ✅ | ✅ |
| LowBoundaryDecimal13 | N/A | N/A | ✅ | ✅ | ✅ | ✅ |
| LowBoundaryDecimal14 | N/A | N/A | ❌ | ✅ | ✅ | ✅ |
| LowBoundaryDecimal15 | N/A | N/A | ❌ | ✅ | ✅ | ✅ |
| LowBoundaryDecimal2 | N/A | N/A | ❌ | ✅ | ✅ | ✅ |
| LowBoundaryDecimal3 | N/A | N/A | ❌ | ❌ | ✅ | ✅ |
| LowBoundaryDecimal4 | N/A | N/A | ❌ | ✅ | ✅ | ✅ |
| LowBoundaryDecimal5 | N/A | N/A | ❌ | ✅ | ✅ | ✅ |
| LowBoundaryDecimal6 | N/A | N/A | ❌ | ✅ | ✅ | ✅ |
| LowBoundaryDecimal7 | N/A | N/A | ✅ | ✅ | ✅ | ✅ |
| LowBoundaryDecimal8 | N/A | N/A | ❌ | ✅ | ✅ | ✅ |
| LowBoundaryDecimal9 | N/A | N/A | ✅ | ✅ | ✅ | ✅ |
| LowBoundaryDecimalDefault | N/A | N/A | ✅ | ✅ | ✅ | ✅ |
| LowBoundaryNegDecimal1 | N/A | N/A | ✅ | ✅ | ✅ | ✅ |
| LowBoundaryNegDecimal2 | N/A | N/A | ❌ | ✅ | ✅ | ✅ |
| LowBoundaryNegDecimal3 | N/A | N/A | ❌ | ❌ | ✅ | ✅ |
| LowBoundaryNegDecimal4 | N/A | N/A | ❌ | ✅ | ✅ | ✅ |
| LowBoundaryNegDecimal5 | N/A | N/A | ❌ | ✅ | ✅ | ✅ |
| LowBoundaryNegDecimalDefault | N/A | N/A | ✅ | ✅ | ✅ | ✅ |
| LowBoundaryQuantity | N/A | N/A | ✅ | ✅ | ✅ | ✅ |
| LowBoundaryTimeMillisecond | N/A | N/A | ✅ | ✅ | ✅ | ✅ |

**Summary:** 94/168 (56%) — 28 tests × 6 engines

14 test(s) fail in only one engine, suggesting engine-specific implementation issues rather than problems with the tests or specification. 2 test(s) fail in multiple (but not all) engines, which may indicate differing interpretations of the specification. 12 additional test(s) are not yet implemented in some engines.
