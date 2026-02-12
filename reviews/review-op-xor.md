## Review Exclusive Or
Name: xor
Date: 2026-02-11
Test Count: 9

### Specification Extract 
Header in specification: xor

Returns `true` if exactly one of the operands evaluates to `true`, `false` if either both operands evaluate to `true` or both operands evaluate to `false`, and the empty collection (`{ }`) otherwise:

|xor |true |false |empty |
| - | - | - | - |
|**true** |`false` |`true` |empty (`{ }`) |
|**false** |`true` |`false` |empty (`{ }`) |
|**empty** |empty (`{ }`) |empty (`{ }`) |empty (`{ }`) |

### Example(s) from Specification
_No examples found in specification._

### Coverage

9 tests found for `xor` (testBooleanLogicXOr1, testBooleanLogicXOr2, testBooleanLogicXOr3, testBooleanLogicXOr4, testBooleanLogicXOr5, testBooleanLogicXOr6, testBooleanLogicXOr7, testBooleanLogicXOr8, testBooleanLogicXOr9).

**Covered:**
- ✅ Complete truth table: true/true, true/false, true/empty, false/true, false/false, false/empty, empty/true, empty/false, empty/empty (testBooleanLogicXOr1, testBooleanLogicXOr2, testBooleanLogicXOr3, testBooleanLogicXOr4, testBooleanLogicXOr5, testBooleanLogicXOr6, testBooleanLogicXOr7, testBooleanLogicXOr8, testBooleanLogicXOr9)

**Gaps:**
- ❌ No test with non-boolean operands requiring implicit boolean conversion

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testBooleanLogicXOr1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testBooleanLogicXOr2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testBooleanLogicXOr3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testBooleanLogicXOr4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testBooleanLogicXOr5 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testBooleanLogicXOr6 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testBooleanLogicXOr7 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testBooleanLogicXOr8 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testBooleanLogicXOr9 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 54/54 (100%) — 9 tests × 6 engines

All tests pass across all engines.
