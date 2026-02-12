## Review Equals
Name: =
Date: 2026-02-11
Test Count: 39

### Specification Extract 
Header in specification: = (Equals)

Returns `true` if the left collection is equal to the right collection:

As noted above, if either operand is an empty collection, the result is an empty collection. Otherwise:

If both operands are collections with a single item, they must be of the same type (or be implicitly convertible to the same type), and:

* For primitives:
  * `String`: comparison is based on Unicode values
  * `Integer`: values must be exactly equal
  * `Decimal`: values must be equal, trailing zeroes after the decimal are ignored
  * `Boolean`: values must be the same
  * `Date`: must be exactly the same
  * `DateTime`: must be exactly the same, respecting the timezone offset (though +00:00 = -00:00 = Z)
  * `Time`: must be exactly the same
* For complex types, equality requires all child elements to be equal, recursively.

If both operands are collections with multiple items, check the equality of each pair of items in order:

* if the result is `false` for any pair, returns `false`
* if the result is `true` for all pairs, returns `true`
* otherwise returns empty ( `{ }` )

Note that this implies that if the collections have a different number of items to compare, the result will be `false`.

Typically, this operator is used with single fixed values as operands. This means that `Patient.telecom.system = 'phone'` will result in an error if there is more than one `telecom` with a `use`. Typically, you'd want `Patient.telecom.where(system = 'phone')`

If one or both of the operands is the empty collection, this operation returns an empty collection.

##### Quantity Equality

When comparing quantities for equality, the dimensions of each quantity must be the same, but not necessarily the unit. For example, units of `'cm'` and `'m'` can be compared, but units of `'cm2'` and `'cm'` cannot. The comparison will be made using the most granular unit of either input. Attempting to operate on quantities with invalid units will result in empty (`{ }`).

For time-valued quantities, note that calendar durations and definite quantity durations above days (and weeks) are considered un-comparable:


Implementations are not required to fully support operations on units, but they must at least respect units, recognizing when units differ.

Implementations that do support units shall do so as specified by [\[UCUM\]](#UCUM). Note that calendar unit conversions for months and years must be performed explicitly, as defined in the [toQuantity(unit)](#fn-toquantity) function.

##### Date/Time Equality

For `Date`, `DateTime` and `Time` equality, the comparison is performed by considering each precision in order, beginning with years (or hours for time values), and respecting timezone offsets. If the values are the same, comparison proceeds to the next precision; if the values are different, the comparison stops and the result is `false`. If one input has a value for the precision and the other does not, the comparison stops and the result is empty (`{ }`); if neither input has a value for the precision, or the last precision has been reached, the comparison stops and the result is `true`. For the purposes of comparison, seconds and milliseconds are considered a single precision using a decimal, with decimal equality semantics.

For example:


For `DateTime` values that do not have a timezone offsets, whether or not to provide a default timezone offset is a policy decision. In the simplest case, no default timezone offset is provided, but some implementations may use the client's or the evaluating system's timezone offset.

To support comparison of DateTime values, either both values have no timezone offset specified, or both values are converted to a common timezone offset. The timezone offset to use is an implementation decision. In the simplest case, it's the timezone offset of the local server. The following examples illustrate expected behavior:


Additional functions to support more sophisticated timezone offset comparison (such as .toUTC()) may be defined in a future version.

### Example(s) from Specification
``` fhirpath
1 year = 1 'a' // {} an empty collection, because comparisons between calendar and UCUM definite-time duration units above days (or weeks) result in empty
1 year = 12 months // empty ( {} ), because calendar unit conversion must be explicit
1 second = 1 's' // true
```

``` fhirpath
@2012 = @2012 // returns true
@2012 = @2013 // returns false
@2012-01 = @2012 // returns empty ({ })
@2012-01-01T10:30 = @2012-01-01T10:30 // returns true
@2012-01-01T10:30 = @2012-01-01T10:31 // returns false
@2012-01-01T10:30:31 = @2012-01-01T10:30 // returns empty ({ })
@2012-01-01T10:30:31.0 = @2012-01-01T10:30:31 // returns true
@2012-01-01T10:30:31.1 = @2012-01-01T10:30:31 // returns false
```

``` fhirpath
@2017-11-05T01:30:00.0-04:00 > @2017-11-05T01:15:00.0-05:00 // false
@2017-11-05T01:30:00.0-04:00 < @2017-11-05T01:15:00.0-05:00 // true
@2017-11-05T01:30:00.0-04:00 = @2017-11-05T01:15:00.0-05:00 // false
@2017-11-05T01:30:00.0-04:00 = @2017-11-05T00:30:00.0-05:00 // true
```

### Coverage

39 tests found for `=` (testLiteralIntegerEqual, testDateEqual, testLiteralDateTimeTZEqualFalse, testLiteralDateTimeTZEqualTrue, testExpressionsEqual, testQuantity1, testQuantity5, testQuantity6, testEquality1, testEquality2, testEquality3, testEquality4, testEquality5, testEquality6, testEquality7, testEquality8, testEquality9, testEquality10, testEquality11, testEquality12, testEquality13, testEquality14, testEquality15, testEquality16, testEquality17, testEquality18, testEquality19, testEquality20, testEquality21, testEquality22, testEquality23, testEquality24, testEquality25, testEquality26, testEquality27, testEquality28, testMixedPrecisionEquals1, testMixedPrecisionEquals2, testMixedPrecisionEquals3).

**Covered:**
- ✅ Integer equality (testEquality1, testEquality8, testEquality15)
- ✅ String equality, case sensitive (testEquality9, testEquality10, testEquality11)
- ✅ Decimal equality with trailing zeroes ignored (testEquality12, testEquality13, testEquality14, testEquality16)
- ✅ Mixed Integer/Decimal implicit conversion (testMixedPrecisionEquals1, testMixedPrecisionEquals2, testMixedPrecisionEquals3)
- ✅ Date equality (testEquality17, testEquality18, testDateEqual)
- ✅ DateTime equality with timezone offsets (testEquality20, testEquality24, testLiteralDateTimeTZEqualFalse, testLiteralDateTimeTZEqualTrue)
- ✅ Date/DateTime precision mismatch returns empty (testEquality19, testEquality23)
- ✅ DateTime seconds/milliseconds precision (testEquality21, testEquality22)
- ✅ Empty operand returns empty (testEquality2, testEquality3)
- ✅ Multi-item collection pairwise equality, order dependent (testEquality4, testEquality5, testEquality6, testEquality7, testEquality25, testEquality26, testEquality27)
- ✅ Quantity equality with unit conversion (testQuantity1, testQuantity5, testQuantity6, testEquality28)

**Gaps:**
- ❌ No test for Boolean equality
- ❌ No test for Time equality
- ❌ No test for complex type recursive equality beyond resource-level comparison

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testDateEqual | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquality1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquality10 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquality11 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquality12 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquality13 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquality14 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquality15 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquality16 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquality17 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquality18 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquality19 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquality2 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquality20 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquality21 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquality22 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquality23 | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| testEquality24 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquality25 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquality26 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquality27 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquality28 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquality3 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquality4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquality5 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquality6 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquality7 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquality8 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEquality9 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testExpressionsEqual | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLiteralDateTimeTZEqualFalse | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLiteralDateTimeTZEqualTrue | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLiteralIntegerEqual | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMixedPrecisionEquals1 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMixedPrecisionEquals2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testMixedPrecisionEquals3 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testQuantity1 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testQuantity5 | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ |
| testQuantity6 | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ |

**Summary:** 217/234 (93%) — 39 tests × 6 engines

11 test(s) fail in only one engine, suggesting engine-specific implementation issues rather than problems with the tests or specification. 3 test(s) fail in multiple (but not all) engines, which may indicate differing interpretations of the specification.
