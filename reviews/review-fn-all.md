## Review `all(criteria) : Boolean`
Name: all
Date: 2026-02-11
Test Count: 2

### Specification Extract 
Header in specification: all(criteria : ($this, $index) => Boolean) : Boolean

> This is a [scoped function](#scoped-functions): The `criteria` argument is evaluated for each item (setting `$this` and `$index` before each iteration); if all return `true` then the function returns `true`, otherwise `false`. An empty input collection returns `true`.

Returns `true` if for every item in the input collection, `criteria` evaluates to `true`. Otherwise, the result is `false`. If the input collection is empty (`{ }`), the result is `true`.


This example returns `true` if all of the `generalPractitioner` elements are of type `Practitioner`.

### Example(s) from Specification
``` fhirpath
generalPractitioner.all($this.resolve() is Practitioner)
```

### Coverage
2 tests found for `all` (testAllTrue3, testAllTrue4).

**Covered:**
- ✅ Returns true when all items satisfy criteria (testAllTrue3)
- ✅ Returns false when not all items satisfy criteria (testAllTrue4)

**Gaps:**
- ❌ Empty input collection returns true
- ❌ $index variable usage not tested
- ❌ Criteria returning empty/null (three-valued logic) not tested

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testAllTrue3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testAllTrue4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 12/12 (100%) — 2 tests × 6 engines
- Overall pass rate: 12/12 (100%)
- Tests: 2
- All engines pass all tests — fully consistent.
