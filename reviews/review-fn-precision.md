## Review `precision() : Integer` — STU
Name: precision
Date: 2026-02-11
Test Count: 6

### Specification Extract 
Header in specification: precision() : Integer

If the input collection contains a single item, this function will return the number of digits of precision.

The function can only be used with Decimal, Date, DateTime, and Time values.

If the input collection is empty, the result is empty.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

For Decimal values, the function returns the number of digits of precision after the decimal place in the input value.


For Date and DateTime values, the function returns the number of digits of precision in the input value.

### Example(s) from Specification
``` fhirpath
1.58700.precision() // 5
```

``` fhirpath
@2014.precision() // 4
@2014-01-05T10:30:00.000.precision() // 17
@T10:30.precision() // 4
@T10:30:00.000.precision() // 9
```

### Coverage

6 tests found for `precision` (PrecisionDecimal, PrecisionYear, PrecisionDateTimeMilliseconds, PrecisionTimeMinutes, PrecisionTimeMilliseconds, PrecisionEmpty).

**Covered:**
- ✅ Decimal precision returns digits after decimal point (PrecisionDecimal)
- ✅ Date and DateTime precision at year and millisecond granularity (PrecisionYear, PrecisionDateTimeMilliseconds)
- ✅ Time precision at minute and millisecond granularity (PrecisionTimeMinutes, PrecisionTimeMilliseconds)
- ✅ Empty input returns empty (PrecisionEmpty)

**Gaps:**
- ❌ Error on multiple items in input collection
- ❌ Date with intermediate precision (e.g. @2014-01 for year-month)

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| PrecisionDateTimeMilliseconds | N/A | N/A | ❌ | ✅ | ✅ | ✅ |
| PrecisionDecimal | N/A | N/A | ❌ | ❌ | ✅ | ✅ |
| PrecisionEmpty | N/A | N/A | ❌ | ✅ | ✅ | ✅ |
| PrecisionTimeMilliseconds | N/A | N/A | ❌ | ✅ | ✅ | ✅ |
| PrecisionTimeMinutes | N/A | N/A | ❌ | ✅ | ✅ | ✅ |
| PrecisionYear | N/A | N/A | ❌ | ✅ | ✅ | ✅ |

**Summary:** 17/36 (47%) — 6 tests × 6 engines

5 test(s) fail in only one engine, suggesting engine-specific implementation issues rather than problems with the tests or specification. 1 test(s) fail in multiple (but not all) engines, which may indicate differing interpretations of the specification.
