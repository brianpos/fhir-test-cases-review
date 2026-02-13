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
- ✅ true xor true = false (testBooleanLogicXOr1)
- ✅ true xor false = true (testBooleanLogicXOr2)
- ✅ true xor empty = empty (testBooleanLogicXOr3)
- ✅ false xor true = true (testBooleanLogicXOr4)
- ✅ false xor false = false (testBooleanLogicXOr5)
- ✅ false xor empty = empty (testBooleanLogicXOr6)
- ✅ empty xor true = empty (testBooleanLogicXOr7)
- ✅ empty xor false = empty (testBooleanLogicXOr8)
- ✅ empty xor empty = empty (testBooleanLogicXOr9)

**Gaps:**
- (none)

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
