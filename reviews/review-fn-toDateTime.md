## Review `toDateTime([format]) : DateTime`
Name: toDateTime
Date: 2026-02-11
Test Count: 0

### Specification Extract 
Header in specification: toDateTime([format : string]) : DateTime

If the input collection contains a single item, this function will return a single datetime if:

* the item is a DateTime
* the item is a Date, in which case the result is a DateTime with the year, month, and day of the Date, and the time components empty (not set to zero)
* the item is a String and is convertible to a DateTime

If the item is not one of the above types, the result is empty.

If the item is a String, but the string is not convertible to a DateTime (using the default format `yyyy-MM-DDThh:mm:ss.fff(+\|-)hh:mm`), the result is empty.

When the optional format parameter is provided, it is used as a [template](#format-codes) instead of the default format.
If the input is not a string, the format parameter it ignored.

If the item contains a partial datetime (e.g. `'2012-01-01T10:00'`), the result is a partial datetime.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

If the input collection is empty, the result is empty.

### Example(s) from Specification
_No examples found in specification._

### Coverage
0 tests found for `toDateTime`.

**Covered:**
- (none)

**Gaps:**
- ❌ DateTime input returns itself
- ❌ Date input converts to DateTime with time components empty (not zero)
- ❌ Convertible string returns DateTime using default format
- ❌ Non-matching type returns empty
- ❌ Non-convertible string returns empty
- ❌ Optional format parameter used as template for string input
- ❌ Format parameter ignored for non-string input
- ❌ Partial datetime string produces partial datetime result
- ❌ Multiple items in input signals an error
- ❌ Empty input collection returns empty

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|

**Summary:** 0/0 (0%) — 0 tests × 6 engines