## Review `convertsToQuantity([unit]) : Boolean`
Name: convertsToQuantity
Date: 2026-02-11
Test Count: 9

### Specification Extract 
Header in specification: convertsToQuantity([unit : String]) : Boolean

If the input collection contains a single item, this function will return `true` if:

* the item is an Integer, Decimal, or Quantity
* the item is a String that is convertible to a Quantity using the regex format:
* the item is a Boolean

If the input collection is empty, the result is empty.

If the item is not one of the above, the result is `false`.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

If the `unit` argument is provided, it must be the string representation of a UCUM code (or a FHIRPath calendar duration keyword), and is used to determine whether the input quantity can be converted to the given unit, according to the unit conversion rules specified by UCUM. If the input quantity can be converted, the result is `true`, otherwise, the result is `false`.

> Implementations are not required to support a complete UCUM implementation, and may return empty (`{ }`) when the `unit` argument is used and it is different than the input quantity unit.

### Example(s) from Specification
``` regex
(?'value'(\+|-)?\d+(\.\d+)?)\s*('(?'unit'[^']+)'|(?'time'[a-zA-Z]+))?
```

### Coverage
9 tests found for `convertsToQuantity` (testIntegerLiteralConvertsToQuantity, testDecimalLiteralConvertsToQuantity, testStringIntegerLiteralConvertsToQuantity, testStringQuantityLiteralConvertsToQuantity, testStringQuantityWeekConvertsToQuantity, testStringQuantityWeekConvertsToQuantityFalse, testStringDecimalLiteralConvertsToQuantityFalse, testStringDecimalLiteralConvertsToQuantity, testBooleanLiteralConvertsToQuantity).

**Covered:**
- ✅ Integer item returns true (testIntegerLiteralConvertsToQuantity)
- ✅ Decimal item returns true (testDecimalLiteralConvertsToQuantity)
- ✅ String integer convertible to Quantity (testStringIntegerLiteralConvertsToQuantity)
- ✅ String with calendar duration keyword is convertible (testStringQuantityLiteralConvertsToQuantity)
- ✅ String with UCUM unit in quotes is convertible (testStringQuantityWeekConvertsToQuantity)
- ✅ String with unquoted non-keyword unit is not convertible (testStringQuantityWeekConvertsToQuantityFalse)
- ✅ Non-convertible string returns false (testStringDecimalLiteralConvertsToQuantityFalse)
- ✅ String decimal convertible to Quantity (testStringDecimalLiteralConvertsToQuantity)
- ✅ Boolean item returns true (testBooleanLiteralConvertsToQuantity)

**Gaps:**
- ❌ Quantity item returns true not tested with an actual Quantity value
- ❌ Empty input collection returns empty not tested
- ❌ Multiple items in input signal an error not tested
- ❌ Unit argument for UCUM unit conversion checking not tested
- ❌ Implementations may return empty for unsupported unit conversions not tested

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testIntegerLiteralConvertsToQuantity | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDecimalLiteralConvertsToQuantity | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringIntegerLiteralConvertsToQuantity | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringQuantityLiteralConvertsToQuantity | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringQuantityWeekConvertsToQuantity | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringQuantityWeekConvertsToQuantityFalse | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringDecimalLiteralConvertsToQuantityFalse | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringDecimalLiteralConvertsToQuantity | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testBooleanLiteralConvertsToQuantity | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 52/54 (96%) — 9 tests × 6 engines

2 tests each fail in 1 engine, suggesting engine-specific bugs in string-to-quantity conversion.
