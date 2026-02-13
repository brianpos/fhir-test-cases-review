## Review `min() : any` — STU
Name: min
Date: 2026-02-11
Test Count: 0

### Specification Extract 
Header in specification: min() : Integer | Long | Decimal | Quantity | Date | DateTime | Time | String

Returns the minimum item in the input collection. Comparison semantics are defined by the [Comparison Operators](#comparison) for the type of value being aggregated.

Accepts input collections with items of type: Integer, Long, Decimal, Quantity, Date, DateTime, Time, or String.

All items in the input collection SHALL be the same type, otherwise an exception is thrown.

If the input collection is empty (`{ }`), the result is empty.

The following examples illustrate the behavior of the `min` function:

### Example(s) from Specification
``` fhirpath
( 2, 4, 8, 6 ).min() // 2
( 2L, 4L, 8L, 6L ).min() // 2L
( @2012-12-31, @2013-01-01, @2012-01-01 ).min() // @2012-01-01
```

### Coverage
0 tests found for `min`.

**Covered:**
- (none)

**Gaps:**
- ❌ Returns the minimum item in the input collection
- ❌ Comparison semantics defined by Comparison Operators for the type being aggregated
- ❌ Accepts Integer input
- ❌ Accepts Long input
- ❌ Accepts Decimal input
- ❌ Accepts Quantity input
- ❌ Accepts Date input
- ❌ Accepts DateTime input
- ❌ Accepts Time input
- ❌ Accepts String input
- ❌ All items in input collection SHALL be the same type, otherwise exception is thrown
- ❌ Empty input collection returns empty

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|

**Summary:** 0/0 (0%) — 0 tests × 6 engines