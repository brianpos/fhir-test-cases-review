## Review `convertsToDecimal() : Boolean`
Name: convertsToDecimal
Date: 2026-02-11
Test Count: 6

### Specification Extract 
Header in specification: convertsToDecimal() : Boolean

If the input collection contains a single item, this function will `true` if:

* the item is an Integer or Decimal
* the item is a String and is convertible to a Decimal
* the item is a Boolean

If the item is not one of the above types, or is not convertible to a Decimal (using the regex format `(\+|-)?\d+(\.\d+)?`), the result is `false`.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

If the input collection is empty, the result is empty.

### Example(s) from Specification
_No examples found in specification._

### Coverage
6 tests found for `convertsToDecimal` (testIntegerLiteralConvertsToDecimal, testDecimalLiteralConvertsToDecimal, testStringIntegerLiteralConvertsToDecimal, testStringLiteralConvertsToDecimalFalse, testStringDecimalLiteralConvertsToDecimal, testBooleanLiteralConvertsToDecimal).

**Covered:**
- ✅ Integer item returns true (testIntegerLiteralConvertsToDecimal)
- ✅ Decimal item returns true (testDecimalLiteralConvertsToDecimal)
- ✅ Convertible string returns true (testStringIntegerLiteralConvertsToDecimal, testStringDecimalLiteralConvertsToDecimal)
- ✅ Non-convertible string returns false (testStringLiteralConvertsToDecimalFalse)
- ✅ Boolean item returns true (testBooleanLiteralConvertsToDecimal)

**Gaps:**
- ❌ Multiple items in input signal an error not tested
- ❌ Empty input collection returns empty not tested

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testIntegerLiteralConvertsToDecimal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDecimalLiteralConvertsToDecimal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringIntegerLiteralConvertsToDecimal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringLiteralConvertsToDecimalFalse | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringDecimalLiteralConvertsToDecimal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testBooleanLiteralConvertsToDecimal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 36/36 (100%) — 6 tests × 6 engines
