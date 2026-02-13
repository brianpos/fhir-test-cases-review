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
- ✅ Returns true when value matches specified type using function syntax (testPolymorphismIsA1)
- ✅ Returns true when value matches specified type using keyword syntax (testPolymorphismIsA2)
- ✅ Empty input returns empty via singleton evaluation (testPolymorphismIsA3)
- ✅ Returns false when value does not match specified type (testPolymorphismIsB)
- ✅ System primitive type checking: Integer, Decimal, Boolean, String, Quantity (testIntegerLiteralIsInteger, testDecimalLiteralIsDecimal, testType5, testIntegerLiteralIsNotString, testIntegerLiteralIsNotQuantity)
- ✅ Qualified type specifiers with System prefix (testIntegerLiteralIsSystemInteger, testType6, testType8, testDecimalLiteralIsNotQuantity)
- ✅ Qualified type specifiers with FHIR prefix (testType13, testType18, testType19, testTypeA1, testTypeA2, testTypeA3)
- ✅ FHIR vs System type distinction (testType11, testType12, testType14, testType22)
- ✅ Backtick-quoted type names (testType19)
- ✅ Negative type checks across different types (testStringLiteralIsNotInteger, testBooleanLiteralIsNotInteger, testDateIsNotInteger, testIntegerLiteralIsNotDecimal, testStringIntegerLiteralIsNotDecimal, testStringDecimalLiteralIsNotDecimal, testBooleanLiteralIsNotDecimal, testStringIntegerLiteralIsNotQuantity, testStringDecimalLiteralIsNotSystemQuantity, testBooleanLiteralIsNotSystemQuantity)
- ✅ Subclass type matching: value is parent type (testTypeA4, testFHIRPathIsFunction9)
- ✅ FHIR element type hierarchy - code is string, uri vs url (testFHIRPathIsFunction1, testFHIRPathIsFunction2, testFHIRPathIsFunction4, testFHIRPathIsFunction5, testFHIRPathIsFunction6, testFHIRPathIsFunction7)
- ✅ Extension value type checking including Age, Quantity, Duration (testFHIRPathIsFunction8, testFHIRPathIsFunction9, testFHIRPathIsFunction10)
- ✅ Resource-level type checking (testType17, testType18)
- ✅ Parameters value type checking for various FHIR types (testTypeA1, testTypeA2, testTypeA3, testTypeA)

**Gaps:**
- ❌ Error when type identifier cannot be resolved to a valid type
- ❌ Error when input collection contains more than one item

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testPolymorphismIsA1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testPolymorphismIsA2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testPolymorphismIsA3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testPolymorphismIsB | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testIntegerLiteralIsInteger | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testIntegerLiteralIsSystemInteger | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringLiteralIsNotInteger | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testBooleanLiteralIsNotInteger | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDateIsNotInteger | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testIntegerLiteralIsNotDecimal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDecimalLiteralIsDecimal | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| testStringIntegerLiteralIsNotDecimal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringDecimalLiteralIsNotDecimal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testBooleanLiteralIsNotDecimal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testIntegerLiteralIsNotQuantity | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDecimalLiteralIsNotQuantity | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringIntegerLiteralIsNotQuantity | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringDecimalLiteralIsNotSystemQuantity | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testBooleanLiteralIsNotSystemQuantity | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testIntegerLiteralIsNotString | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testType5 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testType6 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testType7 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testType8 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testType11 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testType12 | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ |
| testType13 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testType14 | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ |
| testType17 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testType18 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testType19 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testType22 | ❌ | ❌ | ✅ | ✅ | ✅ | ❌ |
| testTypeA1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testTypeA2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testTypeA3 | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| testTypeA4 | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ |
| testTypeA | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testFHIRPathIsFunction1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testFHIRPathIsFunction2 | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| testFHIRPathIsFunction3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testFHIRPathIsFunction4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testFHIRPathIsFunction5 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testFHIRPathIsFunction6 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testFHIRPathIsFunction7 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testFHIRPathIsFunction8 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testFHIRPathIsFunction9 | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| testFHIRPathIsFunction10 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 268/282 (95%) — 47 tests × 6 engines

Several tests show multi-engine failures around FHIR vs System type distinction: testType22 (Patient.is(System.Patient)) fails on 3/6 engines, testType12 and testType14 fail on 2/6 engines. testTypeA4 (uuid is uri subtype) fails on 2 engines, indicating differences in type hierarchy implementation.
