## Review `toChars() : collection`
Name: toChars
Date: 2026-02-11
Test Count: 1

### Specification Extract 
Header in specification: toChars() : collection

Returns the list of characters in the input string as individual single-character strings. If the input collection is empty (`{ }`), the result is empty.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

### Example(s) from Specification
``` fhirpath
'abc'.toChars() // { 'a', 'b', 'c' }
```

``` fhirpath
'\u0065\u0301'.toChars() // { 'e', '\u0301' } - the combining form of 'é' returns two characters
```

### Coverage

1 tests found for `toChars` (testToChars1).

**Covered:**
- ✅ Basic string split into individual characters (testToChars1)

**Gaps:**
- ❌ Empty input collection returning empty is not tested
- ❌ Multiple items in input collection signaling an error is not tested
- ❌ Unicode combining character handling (e.g. `'\u0065\u0301'.toChars()`) is not tested

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testToChars1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 6/6 (100%) — 1 tests × 6 engines

All tests pass across all engines.
