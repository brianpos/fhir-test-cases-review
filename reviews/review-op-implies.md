## Review Implication
Name: implies
Date: 2026-02-11
Test Count: 9

### Specification Extract 
Header in specification: implies

If the left operand evaluates to `true`, this operator returns the boolean evaluation of the right operand. If the left operand evaluates to `false`, this operator returns `true`. Otherwise, this operator returns `true` if the right operand evaluates to `true`, and the empty collection (`{ }`) otherwise.

|implies |true |false |empty |
| - | - | - | - |
|**true** |`true` |`false` |empty (`{ }`) |
|**false** |`true` |`true` |`true` |
|**empty** |`true` |empty (`{ }`) |empty (`{ }`) |

The implies operator is useful for testing conditionals. For example, if a given name is present, then a family name must be as well:


Note carefully that if the left side of an implies evaluates to empty, the result of the operation is the right side. This is often not the intended result, so the use of operators that ensure a value (such as `~`, instead of `=`) is recommended for testing boolean conditions, as illustrated in the following examples:

Note that implies may use short-circuit evaluation in the case that the first operand evaluates to `false`.

### Example(s) from Specification
``` fhirpath
Patient.name.given.exists() implies Patient.name.family.exists()
CareTeam.onBehalfOf.exists() implies (CareTeam.member.resolve() is Practitioner)
StructureDefinition.contextInvariant.exists() implies StructureDefinition.type = 'Extension'
```

``` fhirpath
Medication.status ~ 'active' implies form.exists()

// if using the following expression in a constraint, it won't have the expected behavior of only requiring form if status was active.
// (using equal '=' would evaluate and return the right argument if the left argument (status) is missing from the input)
Medication.status = 'active' implies form.exists() // bad constraint expression

// More complex conditions
(type ~ 'incident' and severity ~ 'high') implies reviewDate.exists()

// Works with boolean too, but not special-cased
wasNotGiven ~ true implies reasonNotGiven.exists()
```

### Coverage

9 tests found for `implies` (testBooleanImplies1, testBooleanImplies2, testBooleanImplies3, testBooleanImplies4, testBooleanImplies5, testBooleanImplies6, testBooleanImplies7, testBooleanImplies8, testBooleanImplies9).

**Covered:**
- ✅ Complete truth table: true/true, true/false, true/empty, false/true, false/false, false/empty, empty/true, empty/false, empty/empty (testBooleanImplies1, testBooleanImplies2, testBooleanImplies3, testBooleanImplies4, testBooleanImplies5, testBooleanImplies6, testBooleanImplies7, testBooleanImplies8, testBooleanImplies9)

**Gaps:**
- ❌ No test for short-circuit evaluation when left operand is `false`
- ❌ No test with non-boolean operands requiring implicit boolean conversion

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testBooleanImplies1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testBooleanImplies2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testBooleanImplies3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testBooleanImplies4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testBooleanImplies5 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testBooleanImplies6 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testBooleanImplies7 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testBooleanImplies8 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testBooleanImplies9 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 54/54 (100%) — 9 tests × 6 engines

All tests pass across all engines.
