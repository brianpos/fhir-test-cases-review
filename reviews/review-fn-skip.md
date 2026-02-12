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
- ✅ Skipping items from a collection (testDollarOrderAllowed, testSkip1, testSkip2, testSkip3)
- ✅ Skipping past end of collection returns empty (testDollarOrderAllowedA, testSkip4)
- ✅ Semantic error on unordered collection in strict mode (testDollarOrderNotAllowed)

**Gaps:**
- ❌ num <= 0 returns input collection unchanged
- ❌ Empty input collection returns empty

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

3 test(s) fail in only one engine, suggesting engine-specific implementation issues rather than problems with the tests or specification. 1 test(s) fail in multiple (but not all) engines, which may indicate differing interpretations of the specification.
