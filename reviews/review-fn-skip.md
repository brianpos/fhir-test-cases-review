## Review `skip(num) : collection`
Name: skip
Date: 2026-02-11
Test Count: 7

### Specification Extract 
Header in specification: skip(num : Integer) : collection

Returns a collection containing all but the first `num` items in the input collection. Will return an empty collection if there are no items remaining after the indicated number of items have been skipped, or if the input collection is empty. If `num` is less than or equal to zero, the input collection is simply returned.

### Example(s) from Specification
_No examples found in specification._

### Coverage
7 tests found for `skip` (testDollarOrderAllowed, testDollarOrderAllowedA, testDollarOrderNotAllowed, testSkip1, testSkip2, testSkip3, testSkip4).

**Covered:**
- ✅ Returns all but the first num items in the collection (testDollarOrderAllowed, testSkip1, testSkip2, testSkip3)
- ✅ Returns empty collection when no items remaining after skip (testDollarOrderAllowedA, testSkip4)
- ✅ Ordering requirement in strict mode tested (testDollarOrderNotAllowed)

**Gaps:**
- ❌ Empty input collection returns empty
- ❌ num less than or equal to zero returns input collection unchanged

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testDollarOrderAllowed | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| testDollarOrderAllowedA | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDollarOrderNotAllowed | N/A | ❌ | ❌ | ❌ | ❌ | ❌ |
| testSkip1 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testSkip2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testSkip3 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testSkip4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 33/42 (79%) — 7 tests × 6 engines

testDollarOrderNotAllowed fails in most engines (0/5 pass), suggesting the strict-mode semantic error expectation is not widely implemented. testDollarOrderAllowed, testSkip1, and testSkip3 each fail in 1 engine, suggesting engine-specific bugs.
