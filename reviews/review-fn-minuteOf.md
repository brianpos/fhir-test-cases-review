## Review `minuteOf() : Integer`
Name: minuteOf
Date: 2026-02-11
Test Count: 0

### Specification Extract 
Header in specification: minuteOf(): Integer

If the input collection contains a single DateTime or Time, this function will return the minute component.

If the input collection is empty, or the minute is not present in the value, the result is empty.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

### Example(s) from Specification
``` fhirpath
@2012-01-01T12:30:40.002-07:00.minuteOf() // 30
```

### Coverage
0 tests found for `minuteOf`.

**Covered:**
- (none)

**Gaps:**
- ❌ Single DateTime input returns the minute component
- ❌ Single Time input returns the minute component
- ❌ Empty input returns empty
- ❌ Minute not present in value returns empty
- ❌ Multiple items in input collection signals error

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|

**Summary:** 0/0 (0%) — 0 tests × 6 engines