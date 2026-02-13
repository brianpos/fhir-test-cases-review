## Review `iif(criterion, true-result, [otherwise])`
Name: iif
Date: 2026-02-11
Test Count: 19

### Specification Extract 
Header in specification: iif(criterion: ($this, $index) => Boolean, true-result: ($this, $index) => collection [, otherwise-result: ($this, $index) => collection]) : collection

> This is a [scoped function](#scoped-functions): The `criterion` argument is evaluated once (with `$this` set to the input value, and $index will be set to `0`).<br/> If it returns `true`, then the `true-result` argument is evaluated (with `$this` set to the input value, and `$index` set to `0`) and returned,<br/> otherwise the `false-result` argument is evaluated (with `$this` set to the input value, and `$index` set to `0`) and returned.

The `iif` function in FHIRPath is an _immediate if_, also known as a conditional operator (such as the C programming language's `? :` operator).

Unlike most other functions it can be called with no context (hence uses the context of the expression's evaluation input), or with a single item context.
In either case, the `$index` variable is set to `0` during evaluation of the arguments, ensuring that its value corresponds with the value of $this.

The `criterion` expression is expected to evaluate to a Boolean.

If `criterion` is `true`, the function returns the value of the `true-result` argument.

If `criterion` is `false` or an empty collection, the function returns `otherwise-result`, unless the optional `otherwise-result` is not given, in which case the function returns an empty collection.

Note that short-circuit behavior is expected in this function. In other words, `true-result` should only be evaluated if the `criterion` evaluates to `true`, and `otherwise-result` should only be evaluated otherwise. For implementations, this means delaying evaluation of the output arguments (specifically true-result and otherwise-result) to remove the chance that their evaluation throws an error and terminates the expression early.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

### Example(s) from Specification
```
// call with no context
iif(true, 'It is true', 'It is false') // returns 'It is true'

// several ways to return the patient's birthDate, or '(unknown)' if no birthDate is present
iif(birthDate.exists(), birthDate.toString(), '(unknown)')
birthDate.iif(exists(), $this.toString(), '(unknown)')
birthDate.iif(exists(), toString(), '(unknown)')

// same example but as a function call on the name

```

### Coverage
19 tests found for `iif` (testCollectionBoolean1, testCollectionBoolean2, testCollectionBoolean3, testCollectionBoolean4, testCollectionBoolean5, testCollectionBoolean6, testIif1, testIif2, testIif3, testIif4, testIif5, testIif6, testIif7, testIif8, testIif9, testIif10, testIif11, testIif12, testIndex).

**Covered:**
- ✅ Criterion true returns true-result (testCollectionBoolean3, testIif1)
- ✅ Criterion false or empty returns otherwise-result (testCollectionBoolean2, testIif2, testIif5)
- ✅ Otherwise-result omitted returns empty when criterion is false (testIif5)
- ✅ Short-circuit behavior: unevaluated branch not executed (testCollectionBoolean5, testCollectionBoolean6, testIif3, testIif4)
- ✅ Non-boolean criterion signals semantic error (testCollectionBoolean1, testIif6)
- ✅ Called with no context, empty context, and single-item context (testCollectionBoolean3, testIif7, testIif8)
- ✅ Multiple items in input collection signals execution error (testIif10)
- ✅ `$this` set to input value in criterion and true-result (testIif9, testIif11, testIif12)
- ✅ `$index` available during evaluation (testIndex)

**Gaps:**
- ❌ `$index` explicitly verified as `0` when called directly (not inside `select`)

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testCollectionBoolean1 | ❌ | ❌ | ✅ | ✅ | ❌ | ✅ |
| testCollectionBoolean2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testCollectionBoolean3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testCollectionBoolean4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testCollectionBoolean5 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testCollectionBoolean6 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testIif1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testIif2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testIif3 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testIif4 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testIif5 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testIif6 | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ |
| testIif7 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testIif8 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testIif9 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testIif10 | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ |
| testIif11 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testIif12 | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| testIndex | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 99/114 (87%) — 19 tests × 6 engines

6 test(s) fail in only one engine, suggesting engine-specific implementation issues rather than problems with the tests or specification. 3 test(s) fail in multiple (but not all) engines, which may indicate differing interpretations of the specification.
