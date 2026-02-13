## Review `convertsToLong() : Boolean` — STU
Name: convertsToLong
Date: 2026-02-11
Test Count: 0

### Specification Extract 
Header in specification: convertsToLong() : Boolean

If the input collection contains a single item, this function will return `true` if:

* the item is an Integer or Long
* the item is a String and is convertible to a Long
* the item is a Boolean

If the item is not one of the above types, or the item is a String, but is not convertible to an Integer (using the regex format `(\+|-)?\d+`), the result is `false`.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

If the input collection is empty, the result is empty.

### Example(s) from Specification
_No examples found in specification._

### Coverage
0 tests found for `convertsToLong`.

**Covered:**
- (none)

**Gaps:**
- ❌ Integer or Long item returns true not tested
- ❌ Convertible string returns true not tested
- ❌ Boolean item returns true not tested
- ❌ Non-convertible string returns false not tested
- ❌ Multiple items in input signal an error not tested
- ❌ Empty input collection returns empty not tested

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|

**Summary:** 0/0 (0%) — 0 tests × 6 engines
