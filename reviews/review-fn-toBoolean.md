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
- ✅ Integer 1 converts to true (testIntegerLiteralToBoolean)
- ✅ Integer 0 converts to false (testIntegerLiteralToBooleanFalse)
- ✅ Non-convertible integer returns empty (testIntegerLiteralToBooleanEmpty)
- ✅ String 'true' converts to true (testStringTrueToBoolean)
- ✅ String 'false' converts to false (testStringFalseToBoolean)

**Gaps:**
- ❌ Boolean input returns itself unchanged
- ❌ Decimal 1.0 converts to true
- ❌ Decimal 0.0 converts to false
- ❌ Non-convertible decimal returns empty
- ❌ String representations 't', 'yes', 'y', '1', '1.0' convert to true
- ❌ String representations 'f', 'no', 'n', '0', '0.0' convert to false
- ❌ Case-insensitive string matching (e.g., 'TRUE', 'T', 'Yes')
- ❌ Non-convertible string returns empty
- ❌ Non-convertible type (e.g., Date) returns empty
- ❌ Multiple items in input signals an error
- ❌ Empty input collection returns empty

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testIntegerLiteralToBoolean | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testIntegerLiteralToBooleanEmpty | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testIntegerLiteralToBooleanFalse | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringTrueToBoolean | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStringFalseToBoolean | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 30/30 (100%) — 5 tests × 6 engines
