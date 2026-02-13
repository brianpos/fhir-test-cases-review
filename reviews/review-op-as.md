## Review Type cast keyword / `as(type) : collection`
Name: as
Date: 2026-02-11
Test Count: 11

### Specification Extract 
Header in specification: as _type specifier_

If the left operand is a collection with a single item and the second operand is an identifier, this operator returns the value of the left operand if it is of the type specified in the second operand, or a subclass thereof. If the identifier cannot be resolved to a valid type identifier, the evaluator will throw an error. If there is more than one item in the input collection, the evaluator will throw an error. Otherwise, this operator returns the empty collection.

A _type specifier_ is an identifier that must resolve to the name of a type in a model. Type specifiers can have qualifiers, e.g. `FHIR.Patient`, where the qualifier is the name of the model.

### Example(s) from Specification
``` fhirpath
Observation.component.where(value as Quantity > 30 'mg')
```

### Coverage
11 tests found for `as` (testPolymorphismAsA, testPolymorphismAsAFunction, testPolymorphismAsB, testPolymorphismAsBFunction, testFHIRPathAsFunction11, testFHIRPathAsFunction12, testFHIRPathAsFunction13, testFHIRPathAsFunction14, testFHIRPathAsFunction15, testFHIRPathAsFunction21, testFHIRPathAsFunction23).

**Covered:**
- ✅ Returns value when left operand matches specified type (testPolymorphismAsA, testPolymorphismAsAFunction, testFHIRPathAsFunction12, testFHIRPathAsFunction14)
- ✅ Returns empty collection when left operand is not of specified type (testPolymorphismAsB, testPolymorphismAsBFunction, testFHIRPathAsFunction11, testFHIRPathAsFunction13, testFHIRPathAsFunction15)
- ✅ Error when identifier cannot be resolved to valid type (testFHIRPathAsFunction23)
- ✅ Error when more than one item in input collection (testFHIRPathAsFunction21)
- ✅ Both keyword syntax (as) and function syntax (.as()) supported (testPolymorphismAsA vs testPolymorphismAsAFunction)
- ✅ Primitive type discrimination between code, string, id types (testFHIRPathAsFunction11, testFHIRPathAsFunction12, testFHIRPathAsFunction13, testFHIRPathAsFunction14, testFHIRPathAsFunction15)

**Gaps:**
- ❌ Subclass type matching -- returning value when left operand is a subclass of specified type
- ❌ Qualified type specifiers with model qualifier (e.g. FHIR.Patient)

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testPolymorphismAsA | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| testPolymorphismAsAFunction | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| testPolymorphismAsB | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testPolymorphismAsBFunction | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testFHIRPathAsFunction11 | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ |
| testFHIRPathAsFunction12 | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| testFHIRPathAsFunction13 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testFHIRPathAsFunction14 | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| testFHIRPathAsFunction15 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testFHIRPathAsFunction21 | ❌ | ✅ | ❌ | ✅ | ❌ | ✅ |
| testFHIRPathAsFunction23 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 57/66 (86%) — 11 tests × 6 engines

testFHIRPathAsFunction21 (multi-item error) fails on 3/6 engines, suggesting disagreement on error handling semantics. testFHIRPathAsFunction11 (code as string) fails on 2 engines.
