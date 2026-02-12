## Review `convertsToInteger() : Boolean`
Name: convertsToInteger
Date: 2026-02-11
Test Count: 5

### Specification Extract 
Header in specification: convertsToInteger() : Boolean

If the input collection contains a single item, this function will return `true` if:

* the item is an Integer
* the item is a String and is convertible to an Integer
* the item is a Boolean

If the item is not one of the above types, or the item is a String, but is not convertible to an Integer (using the regex format `(\+|-)?\d+`), the result is `false`.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

If the input collection is empty, the result is empty.

### Example(s) from Specification
_No examples found in specification._

### Coverage

5 tests found for `convertsToInteger` (testIntegerLiteralConvertsToInteger, testStringLiteralConvertsToInteger, testStringLiteralConvertsToIntegerFalse, testStringDecimalConvertsToIntegerFalse, testBooleanLiteralConvertsToInteger).

**Covered:**
- ✅ Integer input is convertible (testIntegerLiteralConvertsToInteger)
- ✅ Convertible String returns true (testStringLiteralConvertsToInteger)
- ✅ Non-convertible String returns false (testStringLiteralConvertsToIntegerFalse, testStringDecimalConvertsToIntegerFalse)
- ✅ Boolean input is convertible (testBooleanLiteralConvertsToInteger)

**Gaps:**
- ❌ Empty input collection returns empty
- ❌ Multiple items in input collection signals an error
- ❌ Non-convertible types (Date, Quantity) return false

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testIntegerLiteralConvertsToInteger | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringLiteralConvertsToInteger | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringLiteralConvertsToIntegerFalse | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringDecimalConvertsToIntegerFalse | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testBooleanLiteralConvertsToInteger | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:**
- Overall pass rate: 30/30 (100%)
- Tests: 5
- All engines pass all tests — fully consistent.
