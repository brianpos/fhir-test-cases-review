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
- ✅ Filtering by same type with unqualified, qualified, and backtick-quoted type names (testType20, testType21, testType23)
- ✅ Primitive type discrimination: code vs string vs id (testFHIRPathAsFunction16, testFHIRPathAsFunction17, testFHIRPathAsFunction18, testFHIRPathAsFunction19, testFHIRPathAsFunction20)
- ✅ Complex type filtering with HumanName (testFHIRPathAsFunction22)
- ✅ Error on unknown/invalid type name (testFHIRPathAsFunction24)

**Gaps:**
- ❌ Empty input collection returns empty
- ❌ Subclass/subtype filtering (returning items that are a subclass of the given type)

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testFHIRPathAsFunction16 | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ |
| testFHIRPathAsFunction17 | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| testFHIRPathAsFunction18 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testFHIRPathAsFunction19 | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| testFHIRPathAsFunction20 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testFHIRPathAsFunction22 | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| testFHIRPathAsFunction24 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testType20 | ✅ | ✅ | N/A | ✅ | ✅ | ✅ |
| testType21 | ✅ | ✅ | N/A | ✅ | ✅ | ✅ |
| testType23 | ❌ | ✅ | N/A | ✅ | ✅ | ✅ |

**Summary:** 51/60 (85%) — 10 tests × 6 engines

4 test(s) fail in only one engine, suggesting engine-specific implementation issues rather than problems with the tests or specification. 1 test(s) fail in multiple (but not all) engines, which may indicate differing interpretations of the specification. 2 additional test(s) are not yet implemented in some engines.
