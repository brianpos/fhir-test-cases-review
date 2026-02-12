## Review `duration(value, precision) : Integer`
Name: duration
Date: 2026-02-11
Test Count: 0

### Specification Extract 
Header in specification: duration(value: date | datetime | time, precision: identifier): Integer

Returns the number of whole calendar periods at the specified `precision` between the given input value and the `value` argument. If the input value is after the `value` argument, the result is negative. The result of this operation is always an integer; any fractional periods are dropped.

For input and value types of `date` values, the `precision` argument must be one of: `year`, `month`, `week`, or `day`.

For input and value types of `datetime` values, the `precision` argument must be one of: `year`, `month`, `week`, `day`, `hour`, `minute`, `second`, or `millisecond`.

For input and value types of `time` values, the `precision` argument must be one of: `hour`, `minute`, `second`, or `millisecond`.

If the input value or `value` argument are of less precision than the specified `precision`, the result is empty.

When computing the duration between DateTime values with different timezone offsets, implementations should normalize the timezone when a `precision` of `hour`, `minute`, `second`, or `millisecond` is requested.

If either the input or `value` argument is empty, the result is empty.

The following examples illustrate the behavior of the duration function:

### Example(s) from Specification
```fhirpath
@2025-01-02.duration(@2025-01-07, 'week') // 0 - hasn't passed 7 days duration
@2025-01-01.duration(@2025-09-01, 'year') // 0 - baby is 9 months old
@2024-12-01.duration(@2025-09-01, 'year') // 0 - baby is 10 months old
```

### Coverage
0 tests found for `duration`.

**Covered:**
(none)

**Gaps:**
- ❌ All specification requirements lack test coverage

### Test Results

No tests exist for this function yet. Test results will be added once tests are created.
