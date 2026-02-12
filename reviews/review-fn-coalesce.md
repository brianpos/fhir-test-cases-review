## Review `coalesce(value, ...) : collection` — STU
Name: coalesce
Date: 2026-02-11
Test Count: 0

### Specification Extract 
Header in specification: coalesce(value : collection, [value : collection, ...]) : collection

> **Note:** The contents of this section are Standard for Trial Use (STU)

The `coalesce` function takes a variable number of arguments, each of which is a collection. It returns the first non-empty collection from the arguments. If all arguments are empty collections, the result is an empty collection.

Note that short-circuit behaviour is expected in this function. In other words, arguments after the first non-empty argument are not evaluated. For implementations, this means delaying evaluation of the arguments (as is done with `iif`).


Note that this function is useful for providing fallback options, and is more concise than using `iif` to check each collection in turn.

Such as selecting specific telecom elements based on their use, and falling back to the first available telecom element if none of the specific uses are present:


Another common case is to select a specific coding in a CodeableConcept if it is available, otherwise whatever coding is available.

### Example(s) from Specification
```fhirpath
Patient.coalesce(name.where(use='official'), name.where(use='usual'), name.first()).text // preferentially select name via use
Patient.name.select(coalesce(family & ' ' & given.join(', '), text, 'unknown')) // select is required to process each name separately
coalesce(Patient.identifier.where(system = 'http://example.org/identifier').value.first(), 'unknown')
```

```fhirpath
iif( telecom.where(use='mobile').exists(), telecom.where(use='mobile'),
    iif( telecom.where(use='home').exists(), telecom.where(use='home'),
        iif( telecom.where(use='work').exists(), telecom.where(use='work'),
          telecom))).first()
// could equivalently be written as:
coalesce(telecom.where(use='mobile'), telecom.where(use='home'), telecom.where(use='work'), telecom).first()
```

``` fhirpath
iif( code.coding.where(system='http://snomed.info/sct').exists(),
        code.coding.where(system='http://snomed.info/sct')),
            code.coding)
    .first().code
// could equivalently be written as:
coalesce(code.coding.where(system='http://snomed.info/sct'), code.coding).first().code
```

### Coverage
0 tests found for `coalesce`.

**Covered:**
(none)

**Gaps:**
- ❌ All specification requirements lack test coverage
