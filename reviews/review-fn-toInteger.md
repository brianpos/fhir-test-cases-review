## Review `toInteger() : Integer`
Name: toInteger
Date: 2026-02-11
Test Count: 12

### Specification Extract 
Header in specification: toInteger() : Integer

If the input collection contains a single item, this function will return a single integer if:

* the item is an Integer
* the item is a String and is convertible to an integer
* the item is a Boolean, where `true` results in a 1 and `false` results in a 0.

If the item is not one the above types, the result is empty.

If the item is a String, but the string is not convertible to an integer (using the regex format `(\+|-)?\d+`), the result is empty.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

If the input collection is empty, the result is empty.

### Example(s) from Specification
_No examples found in specification._

### Coverage
12 tests found for `toInteger` (testIntegerLiteralToInteger, testStringIntegerLiteralToInteger, testDecimalLiteralToInteger, testDecimalLiteralToIntegerIsEmpty, testBooleanLiteralToInteger, testToInteger1, testToInteger2, testToInteger3, testToInteger4, testToInteger5, testToDecimal2, testToString2).

**Covered:**
- ✅ Integer identity conversion (testIntegerLiteralToInteger)
- ✅ String to Integer for valid strings including positive, negative, and zero (testStringIntegerLiteralToInteger, testToInteger1, testToInteger2, testToInteger3, testToDecimal2, testToString2)
- ✅ Boolean true converts to 1 (testBooleanLiteralToInteger)
- ✅ Non-convertible strings return empty, including decimal strings and alphabetic strings (testDecimalLiteralToInteger, testDecimalLiteralToIntegerIsEmpty, testToInteger4, testToInteger5)

**Gaps:**
- ❌ Boolean `false` converting to `0` is not tested
- ❌ Empty input collection returning empty is not tested
- ❌ Multiple items in input collection signaling an error is not tested

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testIntegerLiteralToInteger | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringIntegerLiteralToInteger | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDecimalLiteralToInteger | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDecimalLiteralToIntegerIsEmpty | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testBooleanLiteralToInteger | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testToInteger1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testToInteger2 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testToInteger3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testToInteger4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testToInteger5 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testToDecimal2 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testToString2 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 68/72 (94%) — 12 tests × 6 engines

4 test(s) fail in only one engine, suggesting engine-specific implementation issues rather than problems with the tests or specification.
