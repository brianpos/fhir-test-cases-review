## Review `exp() : Decimal`
Name: exp
Date: 2026-02-11
Test Count: 3

### Specification Extract 
Header in specification: exp() : Decimal

Returns _e_ raised to the power of the input.

Accepts Decimal input types. Integer and Long types are also accepted via implicit conversion to Decimal. 

If the input collection is empty, the result is empty.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

### Example(s) from Specification
``` fhirpath
0.exp() // 1.0
(-0.0).exp() // 1.0
```

### Coverage
3 tests found for `exp` (testExp1, testExp2, testExp3).

**Covered:**
- ✅ Returns e raised to the power of input for zero (testExp1)
- ✅ Handles negative zero input (testExp2)
- ✅ Empty input returns empty (testExp3)

**Gaps:**
- ❌ Positive non-zero exponent (e.g., e^1 ≈ 2.718)
- ❌ Negative exponent
- ❌ Integer and Long implicit conversion to Decimal
- ❌ Multiple items in input signals error

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testExp1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testExp2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testExp3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 18/18 (100%) — 3 tests × 6 engines
