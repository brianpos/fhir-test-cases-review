## Review `dateOf() : Date`
Name: dateOf
Date: 2026-02-11
Test Count: 0

### Specification Extract 
Header in specification: dateOf(): Date

If the input collection contains a single Date or DateTime, this function will return the date component (up to the precision present in the input value).

If the input collection is empty, the result is empty.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

### Example(s) from Specification
``` fhirpath
@2012-01-01T12:30:00.000-07:00.dateOf() // @2012-01-01
```

### Coverage
0 tests found for `dateOf`.

**Covered:**
- (none)

**Gaps:**
- ❌ Returns date component from a Date input up to precision present
- ❌ Returns date component from a DateTime input up to precision present
- ❌ Empty input collection returns empty
- ❌ Multiple items in input signal an error

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|

**Summary:** 0/0 (0%) — 0 tests × 6 engines