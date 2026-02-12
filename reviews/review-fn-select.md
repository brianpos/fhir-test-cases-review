## Review `select(projection) : collection`
Name: select
Date: 2026-02-11
Test Count: 3

### Specification Extract 
Header in specification: select(projection: ($this, $index) => any) : collection

> This is a [scoped function](#scoped-functions): The `projection` argument is evaluated for each item (setting `$this` and `$index` before each iteration); and the results are included in the output collection.

Evaluates the `projection` expression for each item in the input collection. The result of each evaluation is added to the output collection. If the evaluation results in a collection with multiple items, all items are added to the output collection (collections resulting from evaluation of `projection` are _flattened_). This means that if the evaluation for an item results in the empty collection (`{ }`), no item is added to the result, and that if the input collection is empty (`{ }`), the result is empty as well.


This example results in a collection with only the patient resources from the bundle.


This example results in a collection with all the telecom elements with system of `phone` for all the patients in the bundle.


This example returns a collection containing, for each "usual" name for the Patient, the concatenation of the first given and family names.

### Example(s) from Specification
``` fhirpath
Bundle.entry.select(resource as Patient)
```

``` fhirpath
Bundle.entry.select((resource as Patient).telecom.where(system = 'phone'))
```

``` fhirpath
Patient.name.where(use = 'usual').select(given.first() + ' ' + family)
```

### Coverage

3 tests found for `select` (testSelect1, testSelect2, testSelect3).

**Covered:**
- ✅ Basic projection selecting child elements and unions (testSelect1, testSelect2)
- ✅ Projection with boolean predicate expression (testSelect3)

**Gaps:**
- ❌ Empty input collection returns empty
- ❌ Flattening behavior when projection returns nested collections
- ❌ Use of $index variable in projection

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testSelect1 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testSelect2 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testSelect3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 16/18 (89%) — 3 tests × 6 engines

2 test(s) fail in only one engine, suggesting engine-specific implementation issues rather than problems with the tests or specification.
