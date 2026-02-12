## Review `max() : any` — STU
Name: max
Date: 2026-02-11
Test Count: 0

### Specification Extract 
Header in specification: max() : Integer | Long | Decimal | Quantity | Date | DateTime | Time | String

Returns the maximum item in the input collection. Comparison semantics are defined by the [Comparison Operators](#comparison) for the type of value being aggregated.

Accepts input collections with items of type: Integer, Long, Decimal, Quantity, Date, DateTime, Time, or String.

All items in the input collection SHALL be the same type, otherwise an exception is thrown.

If the input collection is empty (`{ }`), the result is empty.

The following examples illustrate the behavior of the `max` function:

### Example(s) from Specification
``` fhirpath
( 2, 4, 8, 6 ).max() // 8
( 2L, 4L, 8L, 6L ).max() // 8L
( @2012-12-31, @2013-01-01, @2012-01-01 ).max() // @2013-01-01
```

### Coverage
0 tests found for `max`.

**Covered:**
(none)

**Gaps:**
- ❌ All specification requirements lack test coverage

### Test Results

No tests exist for this function yet. Test results will be added once tests are created.
