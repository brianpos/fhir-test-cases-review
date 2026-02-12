## Review `timezoneOffsetOf() : Decimal`
Name: timezoneOffsetOf
Date: 2026-02-11
Test Count: 0

### Specification Extract 
Header in specification: timezoneOffsetOf(): Decimal

If the input collection contains a single DateTime, this function will return the timezone offset component. It is expressed as the number of hours difference from UTC, with fractional hours expressed as decimal values (e.g. -7.5 for UTC-7:30).

If the input collection is empty, or the timezone offset is not present in the value, the result is empty.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

### Example(s) from Specification
``` fhirpath
@2012-01-01T12:30:00.000-07:00.timezoneOffsetOf() // -7.0
@2012-01-01T12:30:00.000+08:45.timezoneOffsetOf() // 8.75 Eucla, Western Australia
```

### Coverage
0 tests found for `timezoneOffsetOf`.

**Covered:**
(none)

**Gaps:**
- ❌ All specification requirements lack test coverage

### Test Results

No tests exist for this function yet. Test results will be added once tests are created.
