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
- ✅ Integer input returns itself (testIntegerLiteralToInteger)
- ✅ String integer converts to Integer (testStringIntegerLiteralToInteger, testToInteger1)
- ✅ Negative string converts to Integer (testToInteger2, testToDecimal2, testToString2)
- ✅ Zero string converts to Integer (testToInteger3)
- ✅ Boolean true converts to 1 (testBooleanLiteralToInteger)
- ✅ String with decimal point is not convertible, returns empty (testDecimalLiteralToInteger, testDecimalLiteralToIntegerIsEmpty, testToInteger4)
- ✅ Non-convertible string returns empty (testToInteger5)

**Gaps:**
- ❌ Boolean false converts to 0
- ❌ String with '+' prefix converts to Integer
- ❌ Non-matching type (e.g., Date, Quantity) returns empty
- ❌ Multiple items in input signals an error
- ❌ Empty input collection returns empty

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

Aidbox fails 4 tests — empty-collection comparison syntax (testDecimalLiteralToInteger) and negative integer string parsing (testToInteger2, testToDecimal2, testToString2).
