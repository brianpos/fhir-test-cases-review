## Review `defineVariable(name, [projection]) : collection` — STU
Name: defineVariable
Date: 2026-02-11
Test Count: 21

### Specification Extract 
Header in specification: defineVariable(name: String [, projection: collection])

> **Note:** The contents of this section are Standard for Trial Use (STU)

Defines a variable named `name` that is accessible in subsequent expressions on the output collection and has the value of `projection` if present, otherwise the value of the input collection. In either case the function does not change the input and the output is the same as the input collection.

> **Note:** This is not a scoped function, it does not change any variables such as `$this` or `$index`.<br/>
>
> This function is the only function that changes the state of the context for processing on the output collection.<br/>
> Whereas [scoped functions](#scoped-functions) only impact the context while evaluating the function, and it's parameters, and the context is restored to the same as before the function was called.

If the name already exists in the current expression scope, the evaluation will end and signal an error to the calling environment.

Example:


> **Note:** this could be implemented using expression scoping on the variable stack and after expression completion the temporary variable would be popped off the stack.

### Example(s) from Specification
``` fhirpath
group.select(
  defineVariable('grp')
  .select(
    element.select(
      defineVariable('src')
      .target.select(
        %grp.source & '#' & %src.code
        & ' ' & equivalence & ' '
        & %grp.target & '#' & code
      )
    )
  )
)
```

### Coverage
21 tests found for `defineVariable` (defineVariable1, defineVariable2, defineVariable3, defineVariable4, defineVariable5, defineVariable6, defineVariable7, defineVariable8, defineVariable9, defineVariable10, dvRedefiningVariableThrowsError, defineVariable12, defineVariable13, defineVariable14, defineVariable15, defineVariable16, dvCantOverwriteSystemVar, dvConceptMapExample, defineVariable19, dvParametersDontColide, dvUsageOutsideScopeThrows).

**Covered:**
- ✅ Define variable with projection value, accessible via %name (defineVariable1)
- ✅ Variable holds collection values from projection expression (defineVariable2, defineVariable3)
- ✅ Define variable without projection uses input collection as value (dvConceptMapExample)
- ✅ Multiple variables in union expressions with separate scopes (defineVariable4, defineVariable5, defineVariable6, defineVariable7)
- ✅ Chaining multiple defineVariable calls in sequence (defineVariable8, defineVariable13, defineVariable14, defineVariable15)
- ✅ Variable not accessible outside its expression scope (defineVariable9, defineVariable12, defineVariable16, dvUsageOutsideScopeThrows)
- ✅ Accessing undefined variable signals error (defineVariable10)
- ✅ Redefining variable in same scope signals error (dvRedefiningVariableThrowsError)
- ✅ Cannot overwrite system variables like %context (dvCantOverwriteSystemVar)
- ✅ Complex nested usage matching spec ConceptMap example pattern (dvConceptMapExample)
- ✅ Variables in nested function parameters don't collide (defineVariable19, dvParametersDontColide)
- ✅ Output collection is same as input — function does not change the input (defineVariable7)

**Gaps:**
- ❌ Does not change scoped variables $this or $index (implicitly tested but not explicitly verified)

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| defineVariable1 | N/A | ✅ | ✅ | ✅ | ✅ | ✅ |
| defineVariable2 | N/A | ❌ | ✅ | ✅ | ✅ | ✅ |
| defineVariable3 | N/A | ❌ | ✅ | ✅ | ✅ | ✅ |
| defineVariable4 | N/A | ❌ | ✅ | ✅ | ✅ | ✅ |
| defineVariable5 | N/A | ❌ | ✅ | ✅ | ✅ | ✅ |
| defineVariable6 | N/A | ❌ | ✅ | ✅ | ✅ | ✅ |
| defineVariable7 | N/A | ❌ | ✅ | ✅ | ✅ | ✅ |
| defineVariable8 | N/A | ✅ | ✅ | ✅ | ✅ | ✅ |
| defineVariable9 | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ |
| defineVariable10 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| dvRedefiningVariableThrowsError | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| defineVariable12 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| defineVariable13 | N/A | ✅ | ✅ | ✅ | ✅ | ✅ |
| defineVariable14 | N/A | ✅ | ✅ | ✅ | ✅ | ✅ |
| defineVariable15 | N/A | ✅ | ✅ | ✅ | ✅ | ✅ |
| defineVariable16 | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ |
| dvCantOverwriteSystemVar | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| dvConceptMapExample | N/A | ✅ | ✅ | ✅ | ✅ | ✅ |
| defineVariable19 | N/A | ✅ | ✅ | ✅ | ✅ | ✅ |
| dvParametersDontColide | N/A | ✅ | ✅ | ✅ | ✅ | ✅ |
| dvUsageOutsideScopeThrows | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ |

**Summary:** 103/126 (82%) — 21 tests × 6 engines

Multiple tests consistently fail in 1 engine, suggesting incomplete defineVariable implementation. Several scope-boundary error tests also show 1 engine failing to detect out-of-scope variable usage.
