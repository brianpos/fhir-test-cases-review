## Review `repeat(projection) : collection`
Name: repeat
Date: 2026-02-11
Test Count: 3

### Specification Extract 
Header in specification: repeat(projection: ($this) => collection) : collection

> This is a [scoped function](#scoped-functions): The `projection` argument is evaluated for each item (setting `$this` before each iteration); and the results are included in the output collection. The function is then re-evaluated on the output collection, repeating until no new items are added.<br/>Note: As the function iterates on itself, the meaning of `$index` is undefined and not set here.

A version of `select` that will repeat the `projection` and add items to the output collection only if they are not already in the output collection as determined by the [equals](#equals) (`=`) operator.

This can be evaluated by adding all items in the input collection to an input queue, then for each item in the input queue evaluate the repeat expression. If the result of the repeat expression is not in the output collection, add it to both the output collection and also the input queue. Processing continues until the input queue is empty.

This function can be used to traverse a tree and selecting only specific children:


Will repeat finding children called `contains`, until no new items are found.


Will repeat finding children called `item`, until no new items are found.

Note that this is slightly different from:


which would find *any* descendants called `item`, not just the ones nested inside other `item` elements.

The order of items returned by the `repeat()` function is undefined.

### Example(s) from Specification
``` fhirpath
ValueSet.expansion.repeat(contains)
```

``` fhirpath
Questionnaire.repeat(item)
```

``` fhirpath
Questionnaire.descendants().select(item)
```

### Coverage
3 tests found for `repeat` (testRepeat1, testRepeat2, testRepeat5).

**Covered:**
- ✅ Recursive tree traversal on hierarchical FHIR structures (testRepeat1, testRepeat2)
- ✅ Repeat with constant expression (testRepeat5)

**Gaps:**
- ❌ Empty input collection returns empty
- ❌ Deduplication behavior (items already in output collection are not re-added)

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testRepeat1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testRepeat2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testRepeat5 | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |

**Summary:** 17/18 (94%) — 3 tests × 6 engines

1 test(s) fail in only one engine, suggesting engine-specific implementation issues rather than problems with the tests or specification.
