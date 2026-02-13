## Review `toString() : String`
Name: toString
Date: 2026-02-11
Test Count: 11

### Specification Extract 
Header in specification: toString() : String

If the input collection contains a single item, this function will return a single String if:

* the item in the input collection is a String
* the item in the input collection is an Integer, Decimal, Date, Time, DateTime, or Quantity the output will contain its String representation *(as shown in the table below)*
* the item is a Boolean, where `true` results in `'true'` and `false` in `'false'`.

If the item is not one of the above types, the result is empty.

The String representation uses the following formats:

|Type |Representation|Examples|
|-|-|-|
|**Boolean** |`true` or `false`| `true.toString()` returns `true`|
|**Integer** |`(-)?#0`| `42.toString()` returns `42`|
|**Decimal** |`(-)?#0.0#`| `3.14.toString()` returns `3.14`|
|**Quantity** |`(-)?#0.0# (('«unit»')|(«unit»))` | `(53 'km').toString()` returns `53 'km'` *(ucum units include quotes)*<br/>`(4 days).toString()` returns `4 days` *(calendar duration units don't include quotes)*|
|**Date** |`yyyy-MM-DD`| `@2020-01-01.toString()` returns `2020-01-01`|
|**DateTime** |`yyyy-MM-DDThh:mm:ss.fff(+|-)hh:mm`| `@2020-01-01T10:00:00.000+10:00.toString()` returns `2020-01-01T10:00:00.000+10:00` and `@2025-11-01.toString()` returns `2025-11-01`|
|**Time** |`hh:mm:ss.fff`| `@T10:30:00.000.toString()` returns `10:30:00.000`<br/>`@T11:45.toString()` returns `11:45`|

Note that for partial dates and times, the result will only be specified to the level of precision in the value being converted.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

If the input collection is empty, the result is empty.

### Example(s) from Specification
_No examples found in specification._

### Coverage
11 tests found for `toString` (testIntegerLiteralToString, testNegativeIntegerLiteralToString, testDecimalLiteralToString, testStringLiteralToString, testBooleanLiteralToString, testQuantityLiteralWkToString, testQuantityLiteralWeekToString, testToString1, testToString3, testToString4, testToString5).

**Covered:**
- ✅ Integer to String conversion including negative values (testIntegerLiteralToString, testNegativeIntegerLiteralToString, testToString1, testToString3)
- ✅ Decimal to String conversion (testDecimalLiteralToString, testToString4)
- ✅ String identity conversion (testStringLiteralToString)
- ✅ Boolean true to String 'true' (testBooleanLiteralToString)
- ✅ Quantity to String with UCUM and calendar duration units (testQuantityLiteralWkToString, testQuantityLiteralWeekToString)
- ✅ Date to String conversion (testToString5)

**Gaps:**
- ❌ Time to String conversion is not tested
- ❌ DateTime (with time component) to String conversion is not tested
- ❌ Boolean `false` converting to `'false'` is not tested
- ❌ Empty input collection returning empty is not tested
- ❌ Multiple items in input collection signaling an error is not tested

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testIntegerLiteralToString | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNegativeIntegerLiteralToString | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDecimalLiteralToString | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| testStringLiteralToString | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testBooleanLiteralToString | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testQuantityLiteralWkToString | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testQuantityLiteralWeekToString | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ |
| testToString1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testToString3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testToString4 | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| testToString5 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 61/66 (92%) — 11 tests × 6 engines

3 test(s) fail in only one engine, suggesting engine-specific implementation issues rather than problems with the tests or specification. 1 test(s) fail in multiple (but not all) engines, which may indicate differing interpretations of the specification.
