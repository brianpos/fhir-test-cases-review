## Review String concatenation
Name: &
Date: 2026-02-11
Test Count: 5

### Specification Extract 
Header in specification: &amp; (String concatenation)

For strings, will concatenate the strings, where an empty operand is taken to be the empty string. This differs from `+` on two strings, which will result in an empty collection when one of the operands is empty. This operator is specifically included to simplify treating an empty collection as an empty string, a common use case in string manipulation.

### Example(s) from Specification
``` fhirpath
'ABC' + 'DEF' // 'ABCDEF'
'ABC' + { } + 'DEF' // { }
'ABC' & 'DEF' // 'ABCDEF'
'ABC' & { } & 'DEF' // 'ABCDEF'
```

### Coverage

5 tests found for `&` (testConcatenate1, testConcatenate2, testConcatenate3, testConcatenate4, testConcatenate5).

**Covered:**
- ✅ String concatenation (testConcatenate1)
- ✅ Empty operand treated as empty string (testConcatenate2, testConcatenate3, testConcatenate5)
- ✅ Multi-item collection operand behavior (testConcatenate4)

**Gaps:**
(none)

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testConcatenate1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testConcatenate2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testConcatenate3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testConcatenate4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testConcatenate5 | N/A | N/A | N/A | N/A | N/A | N/A |

**Summary:** 24/30 (80%) — 5 tests × 6 engines

1 test(s) are not implemented in some engines, but all implemented tests pass.
