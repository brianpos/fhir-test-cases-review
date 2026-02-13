## Review `where(criteria) : collection`
Name: where
Date: 2026-02-11
Test Count: 5

### Specification Extract 
Header in specification: where(criteria : ($this, $index) => Boolean) : collection

> This is a [scoped function](#scoped-functions): The `criteria` argument is evaluated for each item (setting `$this` and `$index` before each iteration); those that return `true` are included in the output collection.

Returns a collection containing only those items in the input collection for which the stated `criteria` expression evaluates to `true`. Items for which the expression evaluates to `false` or empty (`{ }`) are not included in the result.

If the input collection is empty (`{ }`), the result is empty.

If the result of evaluating the condition is other than a single boolean value, the evaluation will end and signal an error to the calling environment, consistent with singleton evaluation of collections behavior.

The following example returns the list of `telecom` elements that have a `use` element with the value of `'official'`:

### Example(s) from Specification
``` fhirpath
Patient.telecom.where(use = 'official')
```

### Coverage
5 tests found for `where` (testDollarThis1, testDollarThis2, testWhere2, testWhere3, testWhere4).

**Covered:**
- ✅ Returns items where criteria evaluates to true (testWhere2, testDollarThis2)
- ✅ Excludes items where criteria evaluates to false or finds no match (testWhere3, testDollarThis1)
- ✅ $this implicit scoping in criteria expression (testDollarThis1, testDollarThis2)
- ✅ Explicit $this reference in criteria (testWhere4)

**Gaps:**
- ❌ $index parameter usage in criteria expression
- ❌ Empty input returns empty
- ❌ Non-boolean criteria result signals error
- ❌ Items where criteria evaluates to empty are excluded

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testDollarThis1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDollarThis2 | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| testWhere2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testWhere3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testWhere4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 29/30 (97%) — 5 tests × 6 engines

testDollarThis2 fails in 1 engine, suggesting an engine-specific bug.
