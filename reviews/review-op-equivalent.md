## Review Equivalent
Name: ~
Date: 2026-02-11
Test Count: 27

### Specification Extract 
Header in specification: ~ (Equivalent)

Returns `true` if the collections are the same. In particular, comparing empty collections for equivalence `{ } ~ { }` will result in `true`.

If both operands are collections with a single item, they must be of the same type (or implicitly convertible to the same type), and:

* For primitives
  * `String`: the strings must be the same, ignoring case and locale, and normalizing whitespace (see [String Equivalence](#string-equivalence) for more details).
  * `Integer`: exactly equal
  * `Decimal`: values must be equal, comparison is done on values rounded to the precision of the least precise operand. Trailing zeroes after the decimal are ignored in determining precision.
  * `Date`, `DateTime` and `Time`: values must be equal, except that if the input values have different levels of precision, the comparison returns `false`, not empty (`{ }`).
  * `Boolean`: the values must be the same
* For complex types, equivalence requires all child elements to be equivalent, recursively.

If both operands are collections with multiple items:

* Each item must be equivalent
* Comparison is not order dependent

Note that this implies that if the collections have a different number of items to compare, or if one input is a value and the other is empty (`{ }`), the result will be `false`.

##### Quantity Equivalence

When comparing quantities for equivalence, the dimensions of each quantity must be the same, but not necessarily the unit. For example, units of `'cm'` and `'m'` can be compared, but units of `'cm2'` and `'cm'` cannot. The comparison will be made using the most granular unit of either input. Attempting to operate on quantities with invalid units will result in `false`.

For time-valued quantities, calendar durations and definite quantity durations are considered equivalent:


Implementations are not required to fully support operations on units, but they must at least respect units, recognizing when units differ.

Implementations that do support units shall do so as specified by [\[UCUM\]](#UCUM). Note that calendar unit conversions for months and years must be performed explicitly, as defined in the [toQuantity(unit)](#fn-toquantity) function.

##### Date/Time Equivalence

For `Date`, `DateTime` and `Time` equivalence, the comparison is the same as for equality, with the exception that if the input values have different levels of precision, the result is `false`, rather than empty (`{ }`). As with equality, the second and millisecond precisions are considered a single precision using a decimal, with decimal equivalence semantics.

For example:


##### String Equivalence

For strings, equivalence returns `true` if the strings are the same value while ignoring case and locale, and normalizing whitespace. Normalizing whitespace means that all whitespace characters are treated as equivalent, with whitespace characters as defined in the [Whitespace](#whitespace) lexical category.

### Example(s) from Specification
``` fhirpath
1 year ~ 1 'a' // true
1 second ~ 1 's' // true
```

``` fhirpath
@2012 ~ @2012 // returns true
@2012 ~ @2013 // returns false
@2012-01 ~ @2012 // returns false as well
@2012-01-01T10:30 ~ @2012-01-01T10:30 // returns true
@2012-01-01T10:30 ~ @2012-01-01T10:31 // returns false
@2012-01-01T10:30:31 ~ @2012-01-01T10:30 // returns false as well
@2012-01-01T10:30:31.0 ~ @2012-01-01T10:30:31 // returns true
@2012-01-01T10:30:31.1 ~ @2012-01-01T10:30:31 // returns false
```

### Coverage
27 tests found for `~` (testIntegerLiteralToDeciamlEquivalent, testQuantity2, testQuantity4, testEquivalent1, testEquivalent2, testEquivalent3, testEquivalent4, testEquivalent5, testEquivalent6, testEquivalent7, testEquivalent8, testEquivalent9, testEquivalent10, testEquivalent11, testEquivalent12, testEquivalent13, testEquivalent14, testEquivalent15, testEquivalent16, testEquivalent17, testEquivalent18, testEquivalent19, testEquivalent20, testEquivalent21, testEquivalent22, testEquivalent23, testEquivalent24).

**Covered:**
- ✅ Integer equivalence (testEquivalent1, testEquivalent4)
- ✅ Empty collections are equivalent: {} ~ {} returns true (testEquivalent2)
- ✅ Value vs empty returns false (testEquivalent3)
- ✅ String equivalence is case-insensitive (testEquivalent5, testEquivalent6, testEquivalent7)
- ✅ Decimal equivalence with trailing zeroes ignored (testEquivalent8, testEquivalent9, testEquivalent10, testEquivalent12, testEquivalent13)
- ✅ Decimal precision rounding to least precise operand (testEquivalent11)
- ✅ Date equivalence (testEquivalent14, testEquivalent15)
- ✅ Different precision returns false instead of empty (testEquivalent16)
- ✅ Seconds and milliseconds as single precision (testEquivalent17, testEquivalent18)
- ✅ Complex type equivalence with recursive comparison (testEquivalent19)
- ✅ Multi-item collection equivalence is not order dependent (testEquivalent20, testEquivalent21, testEquivalent23, testEquivalent24)
- ✅ Quantity equivalence with unit conversion (testQuantity2, testQuantity4, testEquivalent22)
- ✅ Integer to Decimal implicit conversion for equivalence (testIntegerLiteralToDeciamlEquivalent)

**Gaps:**
- ❌ Boolean equivalence
- ❌ Time equivalence
- ❌ String whitespace normalization in equivalence
- ❌ Quantity with invalid units returns false

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testIntegerLiteralToDeciamlEquivalent | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testQuantity2 | N/A | ✅ | ✅ | ✅ | ✅ | ✅ |
| testQuantity4 | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| testEquivalent1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquivalent2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquivalent3 | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| testEquivalent4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquivalent5 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquivalent6 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquivalent7 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquivalent8 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquivalent9 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquivalent10 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquivalent11 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquivalent12 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquivalent13 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquivalent14 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquivalent15 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquivalent16 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquivalent17 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquivalent18 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquivalent19 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquivalent20 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquivalent21 | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| testEquivalent22 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquivalent23 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquivalent24 | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 151/162 (93%) — 27 tests × 6 engines

testQuantity4 (4 'g' ~ 4040 'mg') fails on 3/6 engines, suggesting possible spec ambiguity about precision handling in quantity equivalence. testEquivalent21 (order-independent collection equivalence) also has mixed results.
