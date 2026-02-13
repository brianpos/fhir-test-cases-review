## Review `not() : Boolean`
Name: not
Date: 2026-02-11
Test Count: 8

### Specification Extract 
Header in specification: not() : Boolean

Returns `true` if the input collection evaluates to `false`, and `false` if it evaluates to `true`. Otherwise, the result is empty (`{ }`):

|not |
|-|
|**true** |`false` |
|**false** |`true` |
|**empty** |empty (`{ }`) |

### Example(s) from Specification
_No examples found in specification._

### Coverage
8 tests found for `not` (testCollectionNotEmpty, testNotEmpty, testLiteralNotOnEmpty, testLiteralNotTrue, testLiteralNotFalse, testIntegerBooleanNotTrue, testIntegerBooleanNotFalse, testNotInvalid).

**Covered:**
- ✅ `not()` on true returns false (testLiteralNotTrue)
- ✅ `not()` on false returns true (testLiteralNotFalse)
- ✅ `not()` on empty returns empty (testLiteralNotOnEmpty)
- ✅ `not()` on boolean resource values (testCollectionNotEmpty, testNotEmpty)
- ✅ `not()` on integer with implicit boolean conversion (testIntegerBooleanNotTrue, testIntegerBooleanNotFalse)
- ✅ `not()` on multi-item collection throws error (testNotInvalid)

**Gaps:**
(none)

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testCollectionNotEmpty | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNotEmpty | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLiteralNotOnEmpty | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLiteralNotTrue | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLiteralNotFalse | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testIntegerBooleanNotTrue | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testIntegerBooleanNotFalse | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNotInvalid | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 48/48 (100%) — 8 tests × 6 engines

All tests pass across all engines.
