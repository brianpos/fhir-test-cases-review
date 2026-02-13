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
- ✅ Integer not-equivalent returning false for same values (testNotEquivalent1)
- ✅ Empty collections are equivalent, so !~ returns false (testNotEquivalent2)
- ✅ Empty vs non-empty returns true (testNotEquivalent3)
- ✅ Different integers return true (testNotEquivalent4)
- ✅ String not-equivalent is case-insensitive (testNotEquivalent5, testNotEquivalent6, testNotEquivalent7)
- ✅ Decimal not-equivalent (testNotEquivalent8, testNotEquivalent9)
- ✅ Decimal trailing zeros treated as equivalent (testNotEquivalent10, testNotEquivalent11, testNotEquivalent12)
- ✅ Decimal division precision in not-equivalent (testNotEquivalent13)
- ✅ Date not-equivalent (testNotEquivalent14, testNotEquivalent15)
- ✅ Date vs DateTime with different precisions returns true for not-equivalent (testNotEquivalent16)
- ✅ DateTime trailing zero seconds treated as equivalent (testNotEquivalent17, testNotEquivalent18)
- ✅ Collection not-equivalent comparing same collections (testNotEquivalent19)
- ✅ Collection not-equivalent is order-independent (testNotEquivalent20, testNotEquivalent21)
- ✅ Quantity not-equivalent with different units (testNotEquivalent22)

**Gaps:**
- (none)

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testNotEquivalent1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNotEquivalent2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNotEquivalent3 | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| testNotEquivalent4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNotEquivalent5 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNotEquivalent6 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNotEquivalent7 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNotEquivalent8 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNotEquivalent9 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
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
| testNotEquivalent20 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNotEquivalent21 | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| testNotEquivalent22 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 128/132 (97%) — 22 tests × 6 engines

3 of 22 tests fail in 1-2 engines each — empty vs non-empty equivalence, decimal division precision, and collection order independence, suggesting engine-specific bugs.
