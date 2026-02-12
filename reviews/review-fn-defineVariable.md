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
- ✅ Basic variable definition with literal projection value (defineVariable1)
- ✅ Variable with FHIRPath projection expression referencing input (defineVariable2, defineVariable3)
- ✅ Multiple variables in union expressions with independent scopes (defineVariable4, defineVariable5, defineVariable6, defineVariable7)
- ✅ Chaining variables with intermediate operations like trace (defineVariable8)
- ✅ Variable chaining where later variable references earlier one in projection (defineVariable13, defineVariable14)
- ✅ Nested variable scopes via nested select expressions (defineVariable15)
- ✅ Dynamic variable names and values computed from expressions (defineVariable19, dvParametersDontColide)
- ✅ Real-world ConceptMap traversal example (dvConceptMapExample)
- ✅ Error when accessing variable out of its expression scope (defineVariable9, defineVariable12, defineVariable16, dvUsageOutsideScopeThrows)
- ✅ Error when referencing undefined variable (defineVariable10)
- ✅ Error when redefining variable in same scope (dvRedefiningVariableThrowsError)
- ✅ Error when overwriting system-defined variable (dvCantOverwriteSystemVar)

**Gaps:**
- ❌ No test verifying output collection equals input collection (pass-through behavior)

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| defineVariable1 | N/A | ✅ | ✅ | ✅ | ✅ | ✅ |
| defineVariable10 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| defineVariable12 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| defineVariable13 | N/A | ✅ | ✅ | ✅ | ✅ | ✅ |
| defineVariable14 | N/A | ✅ | ✅ | ✅ | ✅ | ✅ |
| defineVariable15 | N/A | ✅ | ✅ | ✅ | ✅ | ✅ |
| defineVariable16 | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ |
| defineVariable19 | N/A | ✅ | ✅ | ✅ | ✅ | ✅ |
| defineVariable2 | N/A | ❌ | ✅ | ✅ | ✅ | ✅ |
| defineVariable3 | N/A | ❌ | ✅ | ✅ | ✅ | ✅ |
| defineVariable4 | N/A | ❌ | ✅ | ✅ | ✅ | ✅ |
| defineVariable5 | N/A | ❌ | ✅ | ✅ | ✅ | ✅ |
| defineVariable6 | N/A | ❌ | ✅ | ✅ | ✅ | ✅ |
| defineVariable7 | N/A | ❌ | ✅ | ✅ | ✅ | ✅ |
| defineVariable8 | N/A | ✅ | ✅ | ✅ | ✅ | ✅ |
| defineVariable9 | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ |
| dvCantOverwriteSystemVar | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| dvConceptMapExample | N/A | ✅ | ✅ | ✅ | ✅ | ✅ |
| dvParametersDontColide | N/A | ✅ | ✅ | ✅ | ✅ | ✅ |
| dvRedefiningVariableThrowsError | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| dvUsageOutsideScopeThrows | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ |

**Summary:** 103/126 (82%) — 21 tests × 6 engines

9 test(s) fail in only one engine, suggesting engine-specific implementation issues rather than problems with the tests or specification. 8 additional test(s) are not yet implemented in some engines.
