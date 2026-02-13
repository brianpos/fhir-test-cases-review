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
- ✅ not() returns false when input is true (testLiteralNotTrue)
- ✅ not() returns true when input is false (testLiteralNotFalse)
- ✅ not() on empty returns empty (testLiteralNotOnEmpty)
- ✅ not() used with empty() to test non-empty collection (testCollectionNotEmpty, testNotEmpty)
- ✅ Singleton evaluation: single non-boolean node converts to true for not() (testIntegerBooleanNotTrue, testIntegerBooleanNotFalse)
- ✅ Multiple items input signals error per singleton evaluation (testNotInvalid)

**Gaps:**
- (none)

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
