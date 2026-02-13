## Review `aggregate(aggregator, [init]) : collection`
Name: aggregate
Date: 2026-02-11
Test Count: 4

### Specification Extract 
Header in specification: aggregate(aggregator : ($total, $this, $index) => collection [, init : collection]) : collection

Performs general-purpose aggregation by evaluating the aggregator expression for each item of the input collection. Within this expression, the standard iteration variables of `$this` and `$index` can be accessed, but also a `$total` aggregation variable.

> This is a [scoped function](#scoped-functions): The `init` argument is evaluated once at the start to initialize the `$total` variable.<br/> The `aggregator` argument is then evaluated for each item (setting `$this`and `$index` for each), and has access to the current value of `$total` available. The result of the evaluation is then assigned to `$total`.<br/> The final value of `$total` is returned as the result of the function.<br/>  The `init` argument is evaluated once before setting `$this` and `$index`, so will be evaluated on the outer context, and will have access to outer `$this` values.

The value of the `$total` variable is set to `init`, or empty (`{ }`) if no `init` value is supplied, and is set to the result of the aggregator expression after every iteration.<br/>
The result of the aggregate function is the value of `$total` after the last iteration.

Using this function, sum can be expressed as:


Min could be expressed as:


and average could be expressed as:

### Example(s) from Specification
``` fhirpath
value.aggregate($this + $total, 0)
```

``` fhirpath
value.aggregate(iif($total.empty(), $this, iif($this < $total, $this, $total)))
```

``` fhirpath
value.aggregate($total + $this, 0) / value.count()
```

### Coverage
4 tests found for `aggregate` (testAggregate1, testAggregate2, testAggregate3, testAggregate4).

**Covered:**
- ✅ Sum aggregation with explicit init value (testAggregate1, testAggregate2)
- ✅ Min aggregation without init, using $total.empty() check (testAggregate3)
- ✅ Max aggregation without init, using $total.empty() check (testAggregate4)

**Gaps:**
- ❌ $index variable usage not tested
- ❌ Empty input collection behavior not tested
- ❌ Aggregation over FHIR resource elements not tested (only literal collections)

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testAggregate1 | N/A | ✅ | ✅ | ✅ | ✅ | ✅ |
| testAggregate2 | N/A | ✅ | ✅ | ✅ | ✅ | ✅ |
| testAggregate3 | N/A | ✅ | ✅ | ✅ | ✅ | ✅ |
| testAggregate4 | N/A | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 20/24 (83%) — 4 tests × 6 engines
- Overall pass rate: 20/20 (100%)
- Tests: 4
- All implementing engines pass all tests. 1 engine(s) have not implemented this feature.
