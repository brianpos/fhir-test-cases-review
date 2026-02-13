## Review `toDecimal() : Decimal`
Name: toDecimal
Date: 2026-02-11
Test Count: 8

### Specification Extract 
Header in specification: toDecimal() : Decimal

If the input collection contains a single item, this function will return a single decimal if:

* the item is an Integer or Decimal
* the item is a String and is convertible to a Decimal
* the item is a Boolean, where `true` results in a `1.0` and `false` results in a `0.0`.

If the item is not one of the above types, the result is empty.

If the item is a String, but the string is not convertible to a Decimal (using the regex format `(\+|-)?\d+(\.\d+)?`), the result is empty.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

If the input collection is empty, the result is empty.

### Example(s) from Specification
_No examples found in specification._

### Coverage
8 tests found for `toDecimal` (testIntegerLiteralToDecimal, testDecimalLiteralToDecimal, testDecimalLiteralToDecimalEqual, testBooleanLiteralToDecimal, testToDecimal1, testToDecimal3, testToDecimal4, testToDecimal5).

**Covered:**
- ✅ Integer input converts to Decimal (testIntegerLiteralToDecimal)
- ✅ Decimal input returns itself (testDecimalLiteralToDecimal)
- ✅ String with decimal point converts to Decimal (testDecimalLiteralToDecimalEqual, testToDecimal4)
- ✅ Boolean true converts to 1.0 (testBooleanLiteralToDecimal)
- ✅ String integer converts to Decimal (testToDecimal1, testToDecimal3)
- ✅ Non-convertible string returns empty (testToDecimal5)

**Gaps:**
- ❌ Boolean false converts to 0.0
- ❌ String with sign prefix converts to Decimal (e.g., '+1.0', '-1.5')
- ❌ Non-matching type (e.g., Date) returns empty
- ❌ Multiple items in input signals an error
- ❌ Empty input collection returns empty

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testIntegerLiteralToDecimal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDecimalLiteralToDecimal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDecimalLiteralToDecimalEqual | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testBooleanLiteralToDecimal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testToDecimal1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testToDecimal3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testToDecimal4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testToDecimal5 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 48/48 (100%) — 8 tests × 6 engines
