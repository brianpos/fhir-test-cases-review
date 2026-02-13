## Review `convertsToDateTime([format]) : Boolean`
Name: convertsToDateTime
Date: 2026-02-11
Test Count: 9

### Specification Extract 
Header in specification: convertsToDateTime([format : string]) : Boolean

If the input collection contains a single item, this function will return `true` if:

* the item is a DateTime
* the item is a Date
* the item is a String and is convertible to a DateTime

If the item is not one of the above types, or is not convertible to a DateTime (using the default format `yyyy-MM-DDThh:mm:ss.fff(+\|-)hh:mm`), the result is `false`.

When the optional format parameter is provided, it is used as a [template](#format-codes) instead of the default format.
If the input is not a string, the format parameter it ignored.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

If the input collection is empty, the result is empty.

### Example(s) from Specification
_No examples found in specification._

### Coverage
9 tests found for `convertsToDateTime` (testStringYearConvertsToDateTime, testStringMonthConvertsToDateTime, testStringDayConvertsToDateTime, testStringHourConvertsToDateTime, testStringMinuteConvertsToDateTime, testStringSecondConvertsToDateTime, testStringMillisecondConvertsToDateTime, testStringUTCConvertsToDateTime, testStringTZConvertsToDateTime).

**Covered:**
- ✅ String with various DateTime precisions converts successfully (testStringYearConvertsToDateTime, testStringMonthConvertsToDateTime, testStringDayConvertsToDateTime, testStringHourConvertsToDateTime, testStringMinuteConvertsToDateTime, testStringSecondConvertsToDateTime, testStringMillisecondConvertsToDateTime)
- ✅ Timezone offset formats including UTC 'Z' and explicit offset (testStringUTCConvertsToDateTime, testStringTZConvertsToDateTime)

**Gaps:**
- ❌ DateTime input type returns true
- ❌ Date input type returns true
- ❌ Non-convertible String returns false
- ❌ Non-convertible types (Integer, Boolean) return false
- ❌ Empty input collection returns empty
- ❌ Multiple items in input collection signals an error
- ❌ Optional format parameter not tested

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testStringYearConvertsToDateTime | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringMonthConvertsToDateTime | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringDayConvertsToDateTime | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringHourConvertsToDateTime | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringMinuteConvertsToDateTime | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringSecondConvertsToDateTime | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringMillisecondConvertsToDateTime | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringUTCConvertsToDateTime | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringTZConvertsToDateTime | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 54/54 (100%) — 9 tests × 6 engines
- Overall pass rate: 54/54 (100%)
- Tests: 9
- All engines pass all tests — fully consistent.
