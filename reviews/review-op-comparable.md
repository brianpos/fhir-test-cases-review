## Review `comparable(other) : Boolean` — STU
Name: comparable
Date: 2026-02-11
Test Count: 3

### Specification Extract 
Header in specification: comparable(other : Quantity) : Boolean

> **Note:** The contents of this section are Standard for Trial Use (STU)

Returns `true` if the input Quantity can be compared with the `other` Quantity and their relationship to each other determined.
Comparable means that both have values, and the units are the same (irrespective of the system), or both have `code` and `system` values,
and the `system` is recognized by the FHIRPath implementation, and the codes are comparable within that system
(e.g. `'d'` (days) and `'h'` (hours), or `'[in_i]'` (inches) and `'cm'` (centimeters)).

If either or both inputs are empty, or either input is not a single Quantity value, the result is empty (`{ }`).


This function can be used to guard comparison operations to prevent returning empty results when the quantities are not comparable:

### Example(s) from Specification
``` fhirpath
1 'mg'.comparable(2 'mg') // true - these types are comparable
1 'm'.comparable(20 'cm') // true - these types are both metric distance measures
2 '1'.comparable(3) // true - the integer will implicitly convert to a Quantity with unit `'1'` which is the same system/code so is comparable
1.comparable(2) // true - these will both convert to quantities with the same system/code, hence are comparable
```

``` fhirpath
iif(Observation.value.comparable(2 'mg'), Observation.value < 2 'mg', {})
```

### Coverage

3 tests found for `comparable` (Comparable1, Comparable2, Comparable3).

**Covered:**
- ✅ Comparable quantities with same dimension but different units (Comparable1)
- ✅ Non-comparable quantities with different dimensions (Comparable2, Comparable3)

**Gaps:**
- ❌ No test for same unit comparison (e.g. 1 'mg'.comparable(2 'mg'))
- ❌ No test for empty input returning empty
- ❌ No test for non-Quantity input returning empty
- ❌ No test for integer implicit conversion to Quantity (e.g. 1.comparable(2))

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| Comparable1 | N/A | ✅ | ✅ | ✅ | ✅ | ✅ |
| Comparable2 | N/A | ✅ | ✅ | ✅ | ✅ | ✅ |
| Comparable3 | N/A | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 15/18 (83%) — 3 tests × 6 engines

3 test(s) are not implemented in some engines, but all implemented tests pass.
