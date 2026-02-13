## Review `toTime() : Time`
Name: toTime
Date: 2026-02-11
Test Count: 0

### Specification Extract 
Header in specification: toTime() : Time

If the input collection contains a single item, this function will return a single time if:

* the item is a Time
* the item is a String and is convertible to a Time

If the item is not one of the above types, the result is empty.

If the item is a String, but the string is not convertible to a Time (using the format `hh:mm:ss.fff(+\|-)hh:mm`), the result is empty.

If the item contains a partial time (e.g. `'10:00'`), the result is a partial time.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

If the input collection is empty, the result is empty.

### Example(s) from Specification
_No examples found in specification._

### Coverage
0 tests found for `toTime`.

**Covered:**
- (none)

**Gaps:**
- ❌ Time input returns itself
- ❌ Convertible string returns Time
- ❌ Non-matching type returns empty
- ❌ Non-convertible string returns empty
- ❌ Partial time string produces partial time result
- ❌ Multiple items in input signals an error
- ❌ Empty input collection returns empty

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|

**Summary:** 0/0 (0%) — 0 tests × 6 engines