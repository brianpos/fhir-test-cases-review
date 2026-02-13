## Review `convertsToDate([format]) : Boolean`
Name: convertsToDate
Date: 2026-02-11
Test Count: 3

### Specification Extract 
Header in specification: convertsToDate([format : string]) : Boolean

If the input collection contains a single item, this function will return `true` if:

* the item is a Date
* the item is a DateTime
* the item is a String and is convertible to a Date

If the item is not one of the above types, or is not convertible to a Date (using the default format `yyyy-MM-DD`), the result is `false`.

When the optional format parameter is provided, it is used as a [template](#format-codes) instead of the default format.
If the input is not a string, the format parameter it ignored.

If the item contains a partial date (e.g. `'2012-01'`), the result is a partial date.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

If the input collection is empty, the result is empty.

### Example(s) from Specification
_No examples found in specification._

### Coverage
3 tests found for `convertsToDate` (testStringYearConvertsToDate, testStringMonthConvertsToDate, testStringDayConvertsToDate).

**Covered:**
- ✅ String convertible to Date returns true (testStringYearConvertsToDate, testStringMonthConvertsToDate, testStringDayConvertsToDate)
- ✅ Partial date strings are accepted - year-only and year-month (testStringYearConvertsToDate, testStringMonthConvertsToDate)

**Gaps:**
- ❌ Date item returns true not tested with an actual Date value
- ❌ DateTime item returns true not tested with a DateTime value
- ❌ Non-convertible type returns false not tested
- ❌ Non-convertible string returns false not tested
- ❌ Optional format parameter overrides default format not tested
- ❌ Format parameter is ignored for non-string input not tested
- ❌ Multiple items in input signal an error not tested
- ❌ Empty input collection returns empty not tested

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testStringYearConvertsToDate | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringMonthConvertsToDate | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringDayConvertsToDate | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 18/18 (100%) — 3 tests × 6 engines
