## Review `trace(name, [projection]) : collection`
Name: trace
Date: 2026-02-11
Test Count: 2

### Specification Extract 
Header in specification: trace(name : String [, projection: ($this, $index) => any]) : collection

> This is a [scoped function](#scoped-functions): If no `projection` argument is provided, the input collection is logged without the need for scoping. If the `projection` argument is provided, it is evaluated for each item (setting `$this` and `$index` before each iteration) and the result logged. The input collection is returned as the result of the function.<br/>
> The `name` parameter is evaluated before the function is executed and is not re-evaluated for each iteration of the projection.

Adds a String representation of the input collection to the diagnostic log, using the `name` argument as the name in the log. This log should be made available to the user in some appropriate fashion. Does not change the input, so returns the input collection as output.

If the `projection` argument is used, the trace would log the result of evaluating the project expression on the input, but still return the input to the trace function unchanged.


The above example traces only the id elements of the result of the where.

### Example(s) from Specification
``` fhirpath
contained.where(criteria).trace('unmatched', id).empty()
```

### Coverage
2 tests found for `trace` (testTrace1, testTrace2).

**Covered:**
- ✅ Returns input collection unchanged when called without projection (testTrace1)
- ✅ Returns input collection unchanged when called with projection argument (testTrace2)

**Gaps:**
- ❌ Behavior with empty input collection is not tested

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testTrace1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testTrace2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 12/12 (100%) — 2 tests × 6 engines

All tests pass across all engines.
