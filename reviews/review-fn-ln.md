## Review `ln() : Decimal`
Name: ln
Date: 2026-02-11
Test Count: 3

### Specification Extract 
Header in specification: ln() : Decimal

Returns the natural logarithm of the input (i.e. the logarithm base _e_).

Accepts Decimal input types. Integer and Long types are also accepted via implicit conversion to Decimal. 

If the input collection is empty, the result is empty.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

### Example(s) from Specification
``` fhirpath
1.ln() // 0.0
1.0.ln() // 0.0
```

### Coverage
3 tests found for `ln` (testLn1, testLn2, testLnEmpty).

**Covered:**
- ✅ Natural logarithm of 1 returns 0.0 for both Integer and Decimal input (testLn1, testLn2)
- ✅ Empty input collection returns empty (testLnEmpty)

**Gaps:**
- ❌ Multiple items in input collection signaling error
- ❌ Non-trivial logarithm values (e.g., values other than 1)

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testLn1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLn2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLnEmpty | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 18/18 (100%) — 3 tests × 6 engines

All tests pass across all engines.
