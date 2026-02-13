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
- ✅ Empty ~ empty returns true (testEquivalent2)
- ✅ Value ~ empty returns false (testEquivalent3)
- ✅ Integer equivalence (testEquivalent1, testEquivalent4, testEquivalent12, testEquivalent13)
- ✅ String equivalence, case insensitive (testEquivalent5, testEquivalent6, testEquivalent7)
- ✅ Decimal equivalence with precision rounding (testEquivalent8, testEquivalent9, testEquivalent10, testEquivalent11)
- ✅ Integer to Decimal implicit conversion (testIntegerLiteralToDeciamlEquivalent)
- ✅ Date equivalence (testEquivalent14, testEquivalent15)
- ✅ Date/DateTime precision mismatch returns false not empty (testEquivalent16)
- ✅ DateTime seconds/milliseconds precision (testEquivalent17, testEquivalent18)
- ✅ Complex type equivalence (testEquivalent19, testEquivalent20)
- ✅ Multi-item collection order independence (testEquivalent23, testEquivalent24)
- ✅ Quantity equivalence with unit conversion (testQuantity2, testQuantity4, testEquivalent22)

**Gaps:**
- ❌ No test for Boolean equivalence
- ❌ No test for Time equivalence
- ❌ No test for string whitespace normalization in equivalence

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

5 test(s) fail in only one engine, suggesting engine-specific implementation issues rather than problems with the tests or specification. 2 test(s) fail in multiple (but not all) engines, which may indicate differing interpretations of the specification. 1 additional test(s) are not yet implemented in some engines.
