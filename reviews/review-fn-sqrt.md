## Review `sqrt() : Decimal`
Name: sqrt
Date: 2026-02-11
Test Count: 3

### Specification Extract 
Header in specification: sqrt() : Decimal

Returns the square root of the input number.

Accepts Decimal input types. Integer and Long types are also accepted via implicit conversion to Decimal. 

If the square root cannot be represented (such as the square root of -1), the result is empty.

If the input collection is empty, the result is empty.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

Note that this function is equivalent to raising a number of the power of 0.5 using the power() function.

### Example(s) from Specification
``` fhirpath
81.sqrt() // 9.0
(-1).sqrt() // empty
```

### Coverage

3 tests found for `sqrt` (testSqrt1, testSqrt2, testSqrtEmpty).

**Covered:**
- ✅ Basic square root of integer (testSqrt1)
- ✅ Negative input returns empty (testSqrt2)
- ✅ Empty input returns empty (testSqrtEmpty)

**Gaps:**
- ❌ Error on multiple items in input collection
- ❌ Decimal input type (e.g. 6.25.sqrt() = 2.5)

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testSqrt1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testSqrt2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testSqrtEmpty | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 18/18 (100%) — 3 tests × 6 engines

All tests pass across all engines.
