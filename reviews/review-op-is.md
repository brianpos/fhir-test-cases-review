## Review Type test keyword / `is(type) : Boolean`
Name: is
Date: 2026-02-11
Test Count: 47

### Specification Extract 
Header in specification: is _type specifier_

If the left operand is a collection with a single item and the second operand is a type identifier, this operator returns `true` if the type of the left operand is the type specified in the second operand, or a subclass thereof. If the input value is not of the type, this operator returns `false`. If the identifier cannot be resolved to a valid type identifier, the evaluator will throw an error. If the input collections contains more than one item, the evaluator will throw an error. In all other cases this operator returns `false`.

A _type specifier_ is an identifier that must resolve to the name of a type in a model. Type specifiers can have qualifiers, e.g. `FHIR.Patient`, where the qualifier is the name of the model.


This example returns `true` if all Observation resources in the bundle have a status of finished.

### Example(s) from Specification
``` fhirpath
Bundle.entry.resource.all($this is Observation implies status = 'finished')
```

### Coverage
47 tests found for `is` (testPolymorphismIsA1, testPolymorphismIsA2, testPolymorphismIsA3, testPolymorphismIsB, testIntegerLiteralIsInteger, testIntegerLiteralIsSystemInteger, testStringLiteralIsNotInteger, testBooleanLiteralIsNotInteger, testDateIsNotInteger, testIntegerLiteralIsNotDecimal, testDecimalLiteralIsDecimal, testStringIntegerLiteralIsNotDecimal, testStringDecimalLiteralIsNotDecimal, testBooleanLiteralIsNotDecimal, testIntegerLiteralIsNotQuantity, testDecimalLiteralIsNotQuantity, testStringIntegerLiteralIsNotQuantity, testStringDecimalLiteralIsNotSystemQuantity, testBooleanLiteralIsNotSystemQuantity, testIntegerLiteralIsNotString, testType5, testType6, testType7, testType8, testType11, testType12, testType13, testType14, testType17, testType18, testType19, testType22, testTypeA1, testTypeA2, testTypeA3, testTypeA4, testTypeA, testFHIRPathIsFunction1, testFHIRPathIsFunction2, testFHIRPathIsFunction3, testFHIRPathIsFunction4, testFHIRPathIsFunction5, testFHIRPathIsFunction6, testFHIRPathIsFunction7, testFHIRPathIsFunction8, testFHIRPathIsFunction9, testFHIRPathIsFunction10).

**Covered:**
- ✅ Type test on FHIR resource values with function syntax `is()` and keyword syntax `is` (testPolymorphismIsA1, testPolymorphismIsA2, testPolymorphismIsB)
- ✅ System type literals: Integer, Decimal, String, Boolean, Date (testIntegerLiteralIsInteger, testDecimalLiteralIsDecimal, testType5, testType7, testIntegerLiteralIsNotString, testStringLiteralIsNotInteger, testBooleanLiteralIsNotInteger, testDateIsNotInteger)
- ✅ Qualified type names: System.Integer, System.Boolean, FHIR.Patient, FHIR.boolean (testIntegerLiteralIsSystemInteger, testType6, testType8, testType18, testType13)
- ✅ FHIR vs System type distinction (testType11, testType12, testType14, testType22)
- ✅ Backtick-quoted type names (testType19)
- ✅ Subtype checking: uuid is uri, code is string, Age is Quantity (testTypeA4, testFHIRPathIsFunction2, testFHIRPathIsFunction8, testFHIRPathIsFunction9)
- ✅ Negative subtype checks: id is not code, url is not uri declared type, Duration is not Age (testFHIRPathIsFunction3, testFHIRPathIsFunction5, testFHIRPathIsFunction7, testFHIRPathIsFunction10)
- ✅ Various FHIR element types via Parameters (testTypeA1, testTypeA2, testTypeA3, testTypeA)
- ✅ Quantity-related negative checks for non-Quantity types (testIntegerLiteralIsNotQuantity, testDecimalLiteralIsNotQuantity, testStringIntegerLiteralIsNotQuantity, testStringDecimalLiteralIsNotSystemQuantity, testBooleanLiteralIsNotSystemQuantity)
- ✅ Decimal-related negative checks (testIntegerLiteralIsNotDecimal, testStringIntegerLiteralIsNotDecimal, testStringDecimalLiteralIsNotDecimal, testBooleanLiteralIsNotDecimal)
- ✅ Resource-level type check (testType17)

**Gaps:**
- ❌ No test for empty collection input returning `false`
- ❌ No test for multi-item collection input throwing an error
- ❌ No test for unresolvable type identifier throwing an error

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testBooleanLiteralIsNotDecimal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testBooleanLiteralIsNotInteger | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testBooleanLiteralIsNotSystemQuantity | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDateIsNotInteger | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDecimalLiteralIsDecimal | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| testDecimalLiteralIsNotQuantity | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testFHIRPathIsFunction1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testFHIRPathIsFunction10 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testFHIRPathIsFunction2 | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| testFHIRPathIsFunction3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testFHIRPathIsFunction4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testFHIRPathIsFunction5 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testFHIRPathIsFunction6 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testFHIRPathIsFunction7 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testFHIRPathIsFunction8 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testFHIRPathIsFunction9 | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| testIntegerLiteralIsInteger | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testIntegerLiteralIsNotDecimal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testIntegerLiteralIsNotQuantity | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testIntegerLiteralIsNotString | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testIntegerLiteralIsSystemInteger | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testPolymorphismIsA1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testPolymorphismIsA2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testPolymorphismIsA3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testPolymorphismIsB | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringDecimalLiteralIsNotDecimal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringDecimalLiteralIsNotSystemQuantity | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringIntegerLiteralIsNotDecimal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringIntegerLiteralIsNotQuantity | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringLiteralIsNotInteger | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testType11 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testType12 | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ |
| testType13 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testType14 | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ |
| testType17 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testType18 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testType19 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testType22 | ❌ | ❌ | ✅ | ✅ | ✅ | ❌ |
| testType5 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testType6 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testType7 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testType8 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testTypeA | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testTypeA1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testTypeA2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testTypeA3 | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| testTypeA4 | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ |

**Summary:** 268/282 (95%) — 47 tests × 6 engines

5 test(s) fail in only one engine, suggesting engine-specific implementation issues rather than problems with the tests or specification. 4 test(s) fail in multiple (but not all) engines, which may indicate differing interpretations of the specification.
