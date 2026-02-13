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
- ✅ Boolean input returns true (testTrueLiteralConvertsToBoolean, testFalseLiteralConvertsToBoolean)
- ✅ Integer equal to Boolean representation returns true (testIntegerLiteralConvertsToBoolean, testIntegerLiteralFalseConvertsToBoolean)
- ✅ Integer not equal to Boolean representation returns false (testIntegerLiteralConvertsToBooleanFalse, testNegativeIntegerLiteralConvertsToBooleanFalse)
- ✅ Decimal equal to Boolean representation returns true (testDecimalLiteralConvertsToBoolean)
- ✅ String equal to Boolean representation returns true (testStringTrueLiteralConvertsToBoolean, testStringFalseLiteralConvertsToBoolean)
- ✅ Case-insensitive string matching for Boolean values (testStringFalseLiteralAlsoConvertsToBoolean)

**Gaps:**
- ❌ Empty input collection returns empty not tested
- ❌ Multiple items in input collection signals error not tested
- ❌ Decimal value that does not convert to Boolean (e.g., 2.0) returns false not tested
- ❌ String that does not convert to Boolean (e.g., 'abc') returns false not tested

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

Three tests each fail in 1 engine, suggesting engine-specific bugs with integer and string Boolean conversion edge cases.
