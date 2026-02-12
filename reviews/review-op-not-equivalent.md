## Review Not Equivalent
Name: !~
Date: 2026-02-11
Test Count: 22

### Specification Extract 
Header in specification: !~ (Not Equivalent)

The converse of the equivalent operator, returning `true` if equivalent returns `false` and `false` is equivalent returns `true`. In other words, `A !~ B` is short-hand for `(A ~ B).not()`.

### Example(s) from Specification
_No examples found in specification._

### Coverage
22 tests found for `!~` (testNotEquivalent1, testNotEquivalent2, testNotEquivalent3, testNotEquivalent4, testNotEquivalent5, testNotEquivalent6, testNotEquivalent7, testNotEquivalent8, testNotEquivalent9, testNotEquivalent10, testNotEquivalent11, testNotEquivalent12, testNotEquivalent13, testNotEquivalent14, testNotEquivalent15, testNotEquivalent16, testNotEquivalent17, testNotEquivalent18, testNotEquivalent19, testNotEquivalent20, testNotEquivalent21, testNotEquivalent22).

**Covered:**
- ✅ Integer !~ comparisons (testNotEquivalent1, testNotEquivalent4, testNotEquivalent11, testNotEquivalent12)
- ✅ String !~ with case-insensitive matching (testNotEquivalent5, testNotEquivalent6, testNotEquivalent7)
- ✅ Decimal !~ including trailing zeroes (testNotEquivalent8, testNotEquivalent9, testNotEquivalent10, testNotEquivalent13)
- ✅ Date !~ comparisons including different precisions (testNotEquivalent14, testNotEquivalent15, testNotEquivalent16)
- ✅ DateTime !~ with trailing zeroes (testNotEquivalent17, testNotEquivalent18)
- ✅ Empty collection equivalence (testNotEquivalent2, testNotEquivalent3)
- ✅ Collection !~ comparisons with order independence (testNotEquivalent19, testNotEquivalent20, testNotEquivalent21)
- ✅ Quantity !~ with unit mismatch (testNotEquivalent22)

**Gaps:**
- ❌ No test for boolean !~ comparisons
- ❌ No test for quantity !~ with equivalent but different units (e.g. `1000 'g' !~ 1 'kg'`)

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testNotEquivalent1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNotEquivalent10 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNotEquivalent11 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNotEquivalent12 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNotEquivalent13 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNotEquivalent14 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNotEquivalent15 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNotEquivalent16 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNotEquivalent17 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNotEquivalent18 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNotEquivalent19 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNotEquivalent2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNotEquivalent20 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNotEquivalent21 | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| testNotEquivalent22 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNotEquivalent3 | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| testNotEquivalent4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNotEquivalent5 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNotEquivalent6 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNotEquivalent7 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNotEquivalent8 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNotEquivalent9 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 128/132 (97%) — 22 tests × 6 engines

2 test(s) fail in only one engine, suggesting engine-specific implementation issues rather than problems with the tests or specification. 1 test(s) fail in multiple (but not all) engines, which may indicate differing interpretations of the specification.
