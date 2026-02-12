## Review `toQuantity([unit]) : Quantity`
Name: toQuantity
Date: 2026-02-11
Test Count: 9

### Specification Extract 
Header in specification: toQuantity([unit : String]) : Quantity

If the input collection contains a single item, this function will return a single quantity if:

* the item is an Integer, or Decimal, where the resulting quantity will have the default unit (`'1'`)
* the item is a Quantity
* the item is a String and is convertible to a Quantity using the regex format:
* the item is a Boolean, where `true` results in the quantity `1.0 '1'`, and `false` results in the quantity `0.0 '1'`

If the item is not one of the above, the result is empty.

For example, the following are valid quantity strings:


If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

If the input collection is empty, the result is empty.

If the `unit` argument is provided, it must be the string representation of a UCUM code (or a FHIRPath calendar duration keyword), and is used to determine whether the input quantity can be converted to the given unit, according to the unit conversion rules specified by UCUM. If the input quantity can be converted, the result is the converted quantity, otherwise, the result is empty.

For calendar durations, FHIRPath defines the following conversion factors:

| Calendar duration | Conversion factor |
| - | -|
| `1 year` | `12 months` or `365 days` |
| `1 month` | `30 days` |
| `1 week` | `7 days` |
| `1 day` | `24 hours` |
| `1 hour` | `60 minutes` |
| `1 minute` | `60 seconds` |
| `1 second` | `1 's'` |

Note that because calendar duration conversion factors are approximate, they must be invoked explicitly using the `toQuantity(unit)` function. Attempts to perform comparisons or arithmetic (other than Date/Time arithmetic) requiring calendar duration conversions result in empty (`{ }`).
Note that calendar duration conversion factors are only used when time-valued quantities appear in unanchored calculations. 
See [Date/Time Arithmetic](#datetime-arithmetic) for more information on using time-valued quantities in FHIRPath.

If `q` is a Quantity of `'kg'` and one wants to convert to a Quantity in `'g'` (grams):

> Implementations are not required to support a complete UCUM implementation, and may return empty (`{ }`) when the `unit` argument is used and it is different than the input quantity unit.

### Example(s) from Specification
``` regex
(?'value'(\+|-)?\d+(\.\d+)?)\s*('(?'unit'[^']+)'|(?'time'[a-zA-Z]+))?
```

``` fhirpath
'4 days'
'10 \'mg[Hg]\''
```

``` fhirpath
q.toQuantity('g') // changes the value and units in the quantity according to UCUM conversion rules
```

### Coverage
9 tests found for `toQuantity` (testIntegerLiteralToQuantity, testDecimalLiteralToQuantity, testStringIntegerLiteralToQuantity, testStringQuantityLiteralToQuantity, testStringQuantityDayLiteralToQuantity, testStringQuantityWeekLiteralToQuantity, testStringQuantityMonthLiteralToQuantity, testStringQuantityYearLiteralToQuantity, testStringDecimalLiteralToQuantity).

**Covered:**
- ✅ Integer and Decimal convert to Quantity with default unit '1' (testIntegerLiteralToQuantity, testDecimalLiteralToQuantity, testStringIntegerLiteralToQuantity, testStringDecimalLiteralToQuantity)
- ✅ String with calendar duration units converts to Quantity (testStringQuantityLiteralToQuantity, testStringQuantityDayLiteralToQuantity, testStringQuantityWeekLiteralToQuantity, testStringQuantityMonthLiteralToQuantity, testStringQuantityYearLiteralToQuantity)

**Gaps:**
- ❌ Quantity identity conversion (Quantity input returning same Quantity) is not tested
- ❌ Boolean conversion (true → `1.0 '1'`, false → `0.0 '1'`) is not tested
- ❌ Unit conversion via the optional `unit` parameter is not tested
- ❌ Empty input collection returning empty is not tested
- ❌ Multiple items in input collection signaling an error is not tested

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testDecimalLiteralToQuantity | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testIntegerLiteralToQuantity | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringDecimalLiteralToQuantity | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringIntegerLiteralToQuantity | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| testStringQuantityDayLiteralToQuantity | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringQuantityLiteralToQuantity | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringQuantityMonthLiteralToQuantity | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ |
| testStringQuantityWeekLiteralToQuantity | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringQuantityYearLiteralToQuantity | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ |

**Summary:** 45/54 (83%) — 9 tests × 6 engines

3 test(s) fail in only one engine, suggesting engine-specific implementation issues rather than problems with the tests or specification. 3 test(s) fail in multiple (but not all) engines, which may indicate differing interpretations of the specification.
