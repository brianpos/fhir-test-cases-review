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
- ✅ String with year-only converts to Date (testStringYearConvertsToDate)
- ✅ String with year-month converts to Date (testStringMonthConvertsToDate)
- ✅ String with full date converts to Date (testStringDayConvertsToDate)

**Gaps:**
- ❌ Date input type returns true
- ❌ DateTime input type returns true
- ❌ Non-convertible String returns false
- ❌ Non-convertible types (Integer, Boolean) return false
- ❌ Empty input collection returns empty
- ❌ Multiple items in input collection signals an error
- ❌ Optional format parameter not tested

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testStringYearConvertsToDate | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringMonthConvertsToDate | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringDayConvertsToDate | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:**
- Overall pass rate: 18/18 (100%)
- Tests: 3
- All engines pass all tests — fully consistent.
