## Review `toDate([format]) : Date`
Name: toDate
Date: 2026-02-11
Test Count: 0

### Specification Extract 
Header in specification: toDate([format : string]) : Date

If the input collection contains a single item, this function will return a single date if:

* the item is a Date
* the item is a DateTime, in which case the year, month, and day components
are extracted directly without timezone conversion/normalization
* the item is a String and is convertible to a Date

If the item is not one of the above types, the result is empty.

If the item is a String, but the string is not convertible to a Date (using the default format `yyyy-MM-DD`), the result is empty.

When the optional format parameter is provided, it is used as a [template](#format-codes) instead of the default format.
If the input is not a string, the format parameter it ignored.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

If the input collection is empty, the result is empty.

For example:

### Example(s) from Specification
```fhirpath
@2024-01-15T23:30:00-05:00.toDate() // returns @2024-01-15
'2024-01-15'.toDate() // returns @2024-01-15
'150124'.toDate('ddMMyy') // returns @2024-01-15 
'15-01-2024'.toDate('dd-MM-yyyy') // returns @2024-01-15
'12-27'.toDate('MM-yy') // returns @2027-12 (a partial date with just year and month entered)
```

### Coverage
0 tests found for `toDate`.

**Covered:**
- (none)

**Gaps:**
- ❌ Date input returns itself
- ❌ DateTime input extracts year/month/day without timezone conversion
- ❌ Convertible string returns Date using default format yyyy-MM-DD
- ❌ Non-matching type returns empty
- ❌ Non-convertible string returns empty
- ❌ Optional format parameter used as template for string input
- ❌ Format parameter ignored for non-string input
- ❌ Multiple items in input signals an error
- ❌ Empty input collection returns empty

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|

**Summary:** 0/0 (0%) — 0 tests × 6 engines