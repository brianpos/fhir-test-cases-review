## Review `difference(value, precision) : Integer`
Name: difference
Date: 2026-02-11
Test Count: 0

### Specification Extract 
Header in specification: difference(value: date | datetime | time, precision: identifier): Integer

Returns the number of boundaries crossed for the specified `precision` between the input value and the `value` arguments. If the input value is after the `value` argument, the result is negative. The result of this operation is always an integer; any fractional boundaries are dropped.

For input and value types of `date` values, the `precision` argument must be one of: `year`, `month`, `week`, or `day`.

For input and value types of `datetime` values, the `precision` argument must be one of: `year`, `month`, `week`, `day`, `hour`, `minute`, `second`, or `millisecond`.

For input and value types of `time` values, the `precision` argument must be one of: `hour`, `minute`, `second`, or `millisecond`.

If the input value or `value` argument are of less precision than the specified `precision`, the result is empty.

For calculations involving weeks, Sunday is considered to be the first day of the week for the purposes of determining the number of boundaries crossed.

When computing the difference between `datetime` values with different timezone offsets, implementations should normalize the timezone when a `precision` of `hour`, `minute`, `second`, or `millisecond` is requested.

If either the input or `value` argument is empty, the result is empty.

The following examples illustrate the behavior of the difference function:

### Example(s) from Specification
```fhirpath
@2025-01-02.difference(@2025-01-07, 'week') // 1 - crossed a week boundary (Sunday)
@2025-01-01.difference(@2025-09-01, 'year') // 0 - baby is 9 months old, but born this year
@2024-12-01.difference(@2025-09-01, 'year') // 1 - baby is 10 months old, but born last year
```

### Coverage
0 tests found for `difference`.

**Covered:**
(none)

**Gaps:**
- ❌ All specification requirements lack test coverage

### Test Results

No tests exist for this function yet. Test results will be added once tests are created.
