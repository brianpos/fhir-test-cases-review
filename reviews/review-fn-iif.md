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
- ✅ Scoped function: criterion evaluated with $this set to input value (testIif11, testIif9)
- ✅ $index variable accessible during iif evaluation within iteration context (testIndex)
- ✅ If criterion is true, returns the true-result argument (testCollectionBoolean3, testIif1, testIif8)
- ✅ If criterion is false, returns the otherwise-result argument (testIif2)
- ✅ If criterion is empty collection, returns otherwise-result (testCollectionBoolean2)
- ✅ If otherwise-result is not given and criterion is false, returns empty collection (testIif5)
- ✅ Short-circuit: true-result only evaluated when criterion is true (testCollectionBoolean5, testIif3)
- ✅ Short-circuit: otherwise-result only evaluated when criterion is false/empty (testCollectionBoolean6, testIif4)
- ✅ Can be called with no context (testIif7)
- ✅ Can be called with single item context (testIif8, testIif9)
- ✅ Multiple items in input collection signals error (testIif10)
- ✅ Criterion expected to evaluate to Boolean; multi-item collection as criterion signals error (testCollectionBoolean1)
- ✅ Union with empty resolves to single-item collection for criterion (testCollectionBoolean4)
- ✅ Non-boolean criterion behavior — contested (testIif6)
- ✅ Real-world usage with FHIR resource data in criterion and results (testIif1, testIif2, testIif12)

**Gaps:**
- ❌ $this and $index set to 0 specifically in otherwise-result evaluation (only true-result tested with $this)

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

testCollectionBoolean1 (3/6) and testIif10 (2/6) show inconsistent error-signaling behavior across engines for multi-item input/criterion. Short-circuit tests (testCollectionBoolean5, testCollectionBoolean6, testIif3, testIif4) each fail in 1 engine. testIif6 (4/6) is explicitly contested — non-boolean criterion handling varies.
