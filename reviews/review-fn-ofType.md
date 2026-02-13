## Review `ofType(type) : collection`
Name: ofType
Date: 2026-02-11
Test Count: 10

### Specification Extract 
Header in specification: ofType(type : _type specifier_) : collection

Returns a collection that contains all items in the input collection that are of the given type or a subclass thereof. If the input collection is empty (`{ }`), the result is empty. The `type` argument is an identifier that must resolve to the name of a type in a model. For implementations with compile-time typing, this requires special-case handling when processing the argument to treat it as type specifier rather than an identifier expression:


In the above example, the symbol `Patient` must be treated as a type identifier rather than a reference to a Patient in context.

### Example(s) from Specification
``` fhirpath
Bundle.entry.resource.ofType(Patient)
```

### Coverage
10 tests found for `ofType` (testType20, testType21, testType23, testFHIRPathAsFunction16, testFHIRPathAsFunction17, testFHIRPathAsFunction18, testFHIRPathAsFunction19, testFHIRPathAsFunction20, testFHIRPathAsFunction22, testFHIRPathAsFunction24).

**Covered:**
- ✅ Returns items matching the given type (testType20, testFHIRPathAsFunction17, testFHIRPathAsFunction19)
- ✅ Returns empty when items do not match the given type (testFHIRPathAsFunction18, testFHIRPathAsFunction20)
- ✅ Type argument resolves to a type name in a model (testType20, testType21, testType23)
- ✅ Qualified type names with namespace prefix (testType21, testType23)
- ✅ Subtype filtering behavior — code is not a subclass of string (testFHIRPathAsFunction16, testFHIRPathAsFunction17)
- ✅ Complex type matching with HumanName (testFHIRPathAsFunction22)
- ✅ Error signaled for invalid/unknown type name (testFHIRPathAsFunction24)
- ✅ Backtick-quoted type identifiers in qualified names (testType23)

**Gaps:**
- ❌ Empty input collection returns empty
- ❌ Compile-time typing special-case handling for type specifier vs identifier expression

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testType20 | ✅ | ✅ | N/A | ✅ | ✅ | ✅ |
| testType21 | ✅ | ✅ | N/A | ✅ | ✅ | ✅ |
| testType23 | ❌ | ✅ | N/A | ✅ | ✅ | ✅ |
| testFHIRPathAsFunction16 | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ |
| testFHIRPathAsFunction17 | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| testFHIRPathAsFunction18 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testFHIRPathAsFunction19 | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| testFHIRPathAsFunction20 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testFHIRPathAsFunction22 | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| testFHIRPathAsFunction24 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 51/60 (85%) — 10 tests × 6 engines

Multiple tests fail in 1-2 engines each, suggesting engine-specific bugs in type resolution. testFHIRPathAsFunction16 (code vs string subtyping) fails in 2 engines, reflecting a contested area of type hierarchy interpretation.
