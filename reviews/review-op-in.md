## Review Membership
Name: in
Date: 2026-02-11
Test Count: 8

### Specification Extract 
Header in specification: in (membership) : Boolean

If the left operand is a collection with a single item, this operator returns `true` if the item is in the right operand using equality semantics. If the left-hand side of the operator is empty, the result is empty, if the right-hand side is empty, the result is `false`. If the left operand has multiple items, an exception is thrown.

The following example returns `true` if `'Joe'` is in the list of given names for the Patient:

### Example(s) from Specification
``` fhirpath
'Joe' in Patient.name.given
```

### Coverage
8 tests found for `in` (testIn1, testIn2, testIn3, testIn4, testIn5, testInEmptyCollection, testInEmptyValue, testInEmptyBoth).

**Covered:**
- ✅ Single item found in collection (testIn1, testIn3)
- ✅ Single item not found in collection (testIn2, testIn4)
- ✅ Multi-item left operand throws error (testIn5)
- ✅ Empty left operand returns empty (testInEmptyValue, testInEmptyBoth)
- ✅ Empty right operand returns false (testInEmptyCollection)

**Gaps:**
- ❌ No test verifying equality semantics (not equivalence) for membership, e.g. case-sensitive string matching

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testIn1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testIn2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testIn3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testIn4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testIn5 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testInEmptyBoth | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| testInEmptyCollection | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testInEmptyValue | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |

**Summary:** 46/48 (96%) — 8 tests × 6 engines

2 test(s) fail in only one engine, suggesting engine-specific implementation issues rather than problems with the tests or specification.
