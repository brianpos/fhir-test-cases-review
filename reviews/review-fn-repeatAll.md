## Review `repeatAll(projection) : collection` — STU
Name: repeatAll
Date: 2026-02-11
Test Count: 0

### Specification Extract 
Header in specification: repeatAll(projection: ($this) => collection) : collection

> **Note:** The contents of this section are Standard for Trial Use (STU)

> This is a [scoped function](#scoped-functions): The `projection` argument is evaluated for each item (setting `$this` before each iteration); and the results are included in the output collection. The function is then re-evaluated on the output collection, repeating until no new items are added.<br/>Note: As the function iterates on itself, the meaning of `$index` is undefined and not set here.

A version of `repeat` that allows duplicate items in the output collection. Unlike `repeat`, this function does not check whether items are already present in the output collection before adding them.

This can be evaluated by adding all items in the input collection to an input queue, then for each item in the input queue evaluate the expression. The results are added to the output collection and also to a new iteration queue, regardless of whether they already exist in either collection. The input queue is then replaced by the new iteration queue and processing continues until there are no more items in the input queue to process.

This function provides better performance than `repeat` by eliminating the equality comparisons required to check for duplicates, while still providing more targeted traversal than `descendants()`.

The order of items returned by the `repeatAll()` function is undefined.

> Implementations SHOULD include safety mechanisms to prevent infinite loops. An implementation MAY impose a limit on the number of iterations, or MAY statically analyze the expression to ensure it references an element accessor that returns child elements.
> If an infinite loop is detected, or considered likely, the evaluation MAY end and signal an error to the calling environment.
{:.stu .dragon}

Safe usage typically relies on the hierarchical structure of the input data. Expressions that reference elements of the input collection and return child elements will naturally terminate when no more child elements are found.

Some safe expressions:


Some unsafe expressions:

### Example(s) from Specification
``` fhirpath
ValueSet.expansion.repeatAll(contains)
Questionnaire.repeatAll(item)
```

``` fhirpath
Questionnaire.repeatAll('item') // this is a common mistake where the "expression" was in a string, which then just keeps getting called.
'abc'.repeatAll(replace('a', 'A')) // does not rely on the resource structure for termination
```

### Coverage

0 tests found for `repeatAll`.

**Covered:**
(none)

**Gaps:**
- ❌ All specification requirements lack test coverage

### Test Results

No tests exist for this function yet. Test results will be added once tests are created.
