## Review `exists([criteria]) : Boolean`
Name: exists
Date: 2026-02-11
Test Count: 5

### Specification Extract 
Header in specification: exists([criteria : ($this, $index) => any]) : Boolean

> This is a [scoped function](#scoped-functions): The `criteria` argument is evaluated for each item (setting `$this` and `$index` before each iteration); if any return `true` then the function returns `true`, otherwise `false`.

Returns `true` if the input collection has any items (optionally filtered by the criteria), and `false` otherwise.
This is the opposite of `empty()`, and as such is a shorthand for `empty().not()`. If the input collection is empty (`{ }`), the result is `false`.

Using the optional criteria can be considered a shorthand for `where(criteria).exists()`.

Note that a common term for this function is _any_.

The following examples illustrate some potential uses of the `exists()` function:


The first example returns `true` if the `Patient` has any `name` elements.

The second example returns `true` if the `Patient` has any `identifier` elements that have a `use` element equal to `'official'`.

The third example returns `true` if the `Patient` has any `telecom` elements that have a `system` element equal to `'phone'` and a `use` element equal to `'mobile'`.

And finally, the fourth example returns `true` if the `Patient` has any `generalPractitioner` elements of type `Practitioner`.

### Example(s) from Specification
``` fhirpath
Patient.name.exists()
Patient.identifier.exists(use = 'official')
Patient.telecom.exists(system = 'phone' and use = 'mobile')
Patient.generalPractitioner.exists(resolve() is Practitioner)
```

### Coverage
5 tests found for `exists` (testExists1, testExists2, testExists3, testExists4, testExists5).

**Covered:**
- ✅ Returns true for non-empty collection without criteria (testExists1, testExists5)
- ✅ Returns false when criteria is not satisfied by any item (testExists2)
- ✅ Returns true when criteria is satisfied by at least one item (testExists3)
- ✅ Criteria with compound conditions using and/or operators (testExists4)

**Gaps:**
- ❌ Empty input collection returns false
- ❌ $index parameter usage in criteria
- ❌ Equivalence to where(criteria).exists() not explicitly demonstrated

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testExists1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testExists2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testExists3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testExists4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testExists5 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 30/30 (100%) — 5 tests × 6 engines
