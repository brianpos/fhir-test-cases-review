## Review `convertsToString() : Boolean`
Name: convertsToString
Date: 2026-02-11
Test Count: 6

### Specification Extract 
Header in specification: convertsToString() : Boolean

If the input collection contains a single item, this function will return `true` if:

* the item is a String
* the item is an Integer, Decimal, Date, Time, or DateTime
* the item is a Boolean
* the item is a Quantity

If the item is not one of the above types, the result is `false`.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

If the input collection is empty, the result is empty.

### Example(s) from Specification
_No examples found in specification._

### Coverage
6 tests found for `convertsToString` (testIntegerLiteralConvertsToString, testNegativeIntegerLiteralConvertsToString, testDecimalLiteralConvertsToString, testStringLiteralConvertsToString, testBooleanLiteralConvertsToString, testQuantityLiteralConvertsToString).

**Covered:**
- ✅ String item returns true (testStringLiteralConvertsToString)
- ✅ Integer item returns true (testIntegerLiteralConvertsToString, testNegativeIntegerLiteralConvertsToString)
- ✅ Decimal item returns true (testDecimalLiteralConvertsToString)
- ✅ Boolean item returns true (testBooleanLiteralConvertsToString)
- ✅ Quantity item returns true (testQuantityLiteralConvertsToString)

**Gaps:**
- ❌ Date item returns true — not tested
- ❌ Time item returns true — not tested
- ❌ DateTime item returns true — not tested
- ❌ Non-convertible type returns false
- ❌ Multiple items in input signal an error
- ❌ Empty input collection returns empty

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testIntegerLiteralConvertsToString | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNegativeIntegerLiteralConvertsToString | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDecimalLiteralConvertsToString | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringLiteralConvertsToString | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testBooleanLiteralConvertsToString | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testQuantityLiteralConvertsToString | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 36/36 (100%) — 6 tests × 6 engines
