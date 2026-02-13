## Review `dayOf() : Integer`
Name: dayOf
Date: 2026-02-11
Test Count: 0

### Specification Extract 
Header in specification: dayOf(): Integer

If the input collection contains a single Date or DateTime, this function will return the day component.

If the input collection is empty, or the day is not present in the value, the result is empty.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

### Example(s) from Specification
``` fhirpath
@2014-01-05T10:30:00.000.dayOf() // 5
```

### Coverage
0 tests found for `dayOf`.

**Covered:**
- (none)

**Gaps:**
- ❌ Returns day component from a Date input
- ❌ Returns day component from a DateTime input
- ❌ Empty collection or day not present in value returns empty
- ❌ Multiple items in input signal an error

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|

**Summary:** 0/0 (0%) — 0 tests × 6 engines