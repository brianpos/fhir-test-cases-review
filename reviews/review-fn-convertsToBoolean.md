## Review `convertsToBoolean() : Boolean`
Name: convertsToBoolean
Date: 2026-02-11
Test Count: 10

### Specification Extract 
Header in specification: convertsToBoolean() : Boolean

If the input collection contains a single item, this function will return `true` if:

* the item is a Boolean
* the item is an Integer that is equal to one of the possible integer representations of Boolean values
* the item is a Decimal that is equal to one of the possible decimal representations of Boolean values
* the item is a String that is equal to one of the possible string representations of Boolean values

If the item is not one of the above types, or the item is a String, Integer, or Decimal, but is not equal to one of the possible values convertible to a Boolean, the result is `false`.

Possible values for Integer, Decimal, and String are described in the toBoolean() function.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

If the input collection is empty, the result is empty.

### Example(s) from Specification
_No examples found in specification._

### Coverage
10 tests found for `convertsToBoolean` (testIntegerLiteralConvertsToBoolean, testIntegerLiteralConvertsToBooleanFalse, testNegativeIntegerLiteralConvertsToBooleanFalse, testIntegerLiteralFalseConvertsToBoolean, testDecimalLiteralConvertsToBoolean, testStringTrueLiteralConvertsToBoolean, testStringFalseLiteralConvertsToBoolean, testStringFalseLiteralAlsoConvertsToBoolean, testTrueLiteralConvertsToBoolean, testFalseLiteralConvertsToBoolean).

**Covered:**
- ✅ Boolean literal input returns true (testTrueLiteralConvertsToBoolean, testFalseLiteralConvertsToBoolean)
- ✅ Integer 0 and 1 are convertible (testIntegerLiteralConvertsToBoolean, testIntegerLiteralFalseConvertsToBoolean)
- ✅ Non-convertible Integer returns false (testIntegerLiteralConvertsToBooleanFalse, testNegativeIntegerLiteralConvertsToBooleanFalse)
- ✅ Decimal 1.0 is convertible (testDecimalLiteralConvertsToBoolean)
- ✅ String representations are convertible, case-insensitive (testStringTrueLiteralConvertsToBoolean, testStringFalseLiteralConvertsToBoolean, testStringFalseLiteralAlsoConvertsToBoolean)

**Gaps:**
- ❌ Empty input collection returns empty
- ❌ Multiple items in input collection signals an error
- ❌ Decimal 0.0 convertibility not tested
- ❌ Non-convertible String returns false (e.g. 'hello'.convertsToBoolean())
- ❌ Non-convertible types (Date, Quantity) return false

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testIntegerLiteralConvertsToBoolean | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testIntegerLiteralConvertsToBooleanFalse | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNegativeIntegerLiteralConvertsToBooleanFalse | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testIntegerLiteralFalseConvertsToBoolean | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDecimalLiteralConvertsToBoolean | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringTrueLiteralConvertsToBoolean | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringFalseLiteralConvertsToBoolean | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringFalseLiteralAlsoConvertsToBoolean | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testTrueLiteralConvertsToBoolean | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testFalseLiteralConvertsToBoolean | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 57/60 (95%) — 10 tests × 6 engines
- Overall pass rate: 57/60 (95%)
- Tests: 10
