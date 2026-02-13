## Review `timeOf() : Time`
Name: timeOf
Date: 2026-02-11
Test Count: 0

### Specification Extract 
Header in specification: timeOf(): Time

If the input collection contains a single DateTime, this function will return the time component.

If the input collection is empty, or the time is not present in the value, the result is empty.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

### Example(s) from Specification
``` fhirpath
@2012-01-01T12:30:00.000-07:00.timeOf() // @T12:30:00.000
```

### Coverage
0 tests found for `timeOf`.

**Covered:**
- (none)

**Gaps:**
- ❌ Single DateTime input returns the time component
- ❌ Empty input collection returns empty
- ❌ DateTime without time component returns empty
- ❌ Multiple items in input signals an error

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|

**Summary:** 0/0 (0%) — 0 tests × 6 engines