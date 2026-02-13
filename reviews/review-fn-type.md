## Review `type() : collection`
Name: type
Date: 2026-02-11
Test Count: 10

### Specification Extract 
Header in specification: type() : collection

The `type` function returns the type information for each item of the input collection, using concrete subtypes of `TypeInfo`.

> Note: using `X.ofType(Y)` or `X as Y` to filter content is better supported than using `X.type().name = 'Y'`.

If the input collection is empty (`{ }`), or access to type information is unavailable, the result is empty.

For primitive types such as `String` and `Integer`, the result is a `SimpleTypeInfo`:


Results in:


*Note: The base type for primitives is defined as `System.Any`.*

For complex types such as a FHIR CodeableConcept, the result is a `ClassInfo`:


Results in:

### Example(s) from Specification
``` fhirpath
('John' | 'Mary').type()
```

``` typescript
{
  SimpleTypeInfo { namespace: 'System', name: 'String', baseType: 'System.Any' },
  SimpleTypeInfo { namespace: 'System', name: 'String', baseType: 'System.Any' }
}
```

``` fhirpath
Patient.maritalStatus.type()
```

``` typescript
{
  ClassInfo { namespace: 'FHIR', name: 'CodeableConcept', baseType: 'FHIR.Element' }
}
```

### Coverage
10 tests found for `type` (testType1, testType1a, testType2, testType2a, testType3, testType4, testType9, testType10, testType15, testType16).

**Covered:**
- ✅ System primitive types return namespace 'System' (testType1, testType2, testType3)
- ✅ Correct type name for Integer, String, Boolean (testType1a, testType2a, testType4)
- ✅ FHIR element types return namespace 'FHIR' and correct name (testType9, testType10)
- ✅ FHIR resource type returns namespace 'FHIR' and resource name (testType15, testType16)

**Gaps:**
- ❌ No test for empty input returning empty
- ❌ No test for complex types returning ClassInfo (e.g. CodeableConcept)
- ❌ No test for multi-item collections (e.g. ('John' | 'Mary').type())
- ❌ No test for baseType property of TypeInfo

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testType1 | ❌ | ✅ | N/A | ✅ | ✅ | ✅ |
| testType1a | ❌ | ✅ | N/A | ✅ | ✅ | ✅ |
| testType2 | ❌ | ✅ | N/A | ✅ | ✅ | ✅ |
| testType2a | ❌ | ✅ | N/A | ✅ | ✅ | ✅ |
| testType3 | ❌ | ✅ | N/A | ✅ | ✅ | ✅ |
| testType4 | ❌ | ✅ | N/A | ✅ | ✅ | ✅ |
| testType9 | ✅ | ✅ | N/A | ✅ | ✅ | ❌ |
| testType10 | ✅ | ✅ | N/A | ✅ | ✅ | ❌ |
| testType15 | ✅ | ✅ | N/A | ✅ | ✅ | ❌ |
| testType16 | ✅ | ✅ | N/A | ✅ | ✅ | ✅ |

**Summary:** 41/60 (68%) — 10 tests × 6 engines

9 test(s) fail in only one engine, suggesting engine-specific implementation issues rather than problems with the tests or specification. 1 additional test(s) are not yet implemented in some engines.
