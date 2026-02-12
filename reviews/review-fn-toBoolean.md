## Review `toBoolean() : Boolean`
Name: toBoolean
Date: 2026-02-11
Test Count: 5

### Specification Extract 
Header in specification: toBoolean() : Boolean

If the input collection contains a single item, this function will return a single boolean if:

* the item is a Boolean
* the item is an Integer and is equal to one of the **possible** integer **representations** of Boolean values
* the item is a Decimal that is equal to one of the **possible** decimal **representations** of Boolean values
* the item is a String that is equal to one of the **possible** string **representations** of Boolean values

If the item is not one the above types, or the item is a String, Integer, or Decimal, but is not equal to one of the possible values convertible to a Boolean, the result is empty.

The following table describes the **possible** type **representations**:

| Type | Representation | Result |
| -| - | - |
| **String** | `'true'`, `'t'`, `'yes'`, `'y'`, `'1'`, `'1.0'` | `true` |
| | `'false'`, `'f'`, `'no'`, `'n'`, `'0'`, `'0.0'` | `false` |
| **Integer** | `1` | `true` |
| | `0` | `false` |
| **Decimal** | `1.0` *(or decimal equivalent)* |`true` |
| | `0.0` *(or decimal equivalent)* | `false` |

Note for the purposes of string representations, case is ignored (so that both `'T'` and `'t'` are considered `true`).

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

If the input collection is empty, the result is empty.

### Example(s) from Specification
_No examples found in specification._

### Coverage

5 tests found for `toBoolean` (testIntegerLiteralToBoolean, testIntegerLiteralToBooleanEmpty, testIntegerLiteralToBooleanFalse, testStringTrueToBoolean, testStringFalseToBoolean).

**Covered:**
- ✅ Integer 1 converts to true and Integer 0 converts to false (testIntegerLiteralToBoolean, testIntegerLiteralToBooleanFalse)
- ✅ Non-convertible integer (2) returns empty (testIntegerLiteralToBooleanEmpty)
- ✅ String 'true' and 'false' convert to corresponding booleans (testStringTrueToBoolean, testStringFalseToBoolean)

**Gaps:**
- ❌ Decimal representations (1.0 → true, 0.0 → false) are not tested
- ❌ Additional string representations ('t', 'yes', 'y', '1', '1.0', 'f', 'no', 'n', '0', '0.0') are not tested
- ❌ Case insensitivity of string representations is not tested
- ❌ Boolean input returning itself is not tested
- ❌ Empty input collection returning empty is not tested
- ❌ Multiple items in input collection signaling an error is not tested

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testIntegerLiteralToBoolean | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testIntegerLiteralToBooleanEmpty | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testIntegerLiteralToBooleanFalse | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringFalseToBoolean | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringTrueToBoolean | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 30/30 (100%) — 5 tests × 6 engines

All tests pass across all engines.
