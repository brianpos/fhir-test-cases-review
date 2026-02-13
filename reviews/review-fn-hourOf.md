## Review `hourOf() : Integer`
Name: hourOf
Date: 2026-02-11
Test Count: 0

### Specification Extract 
Header in specification: hourOf(): Integer

If the input collection contains a single DateTime or Time, this function will return the hour component.

If the input collection is empty, or the hour is not present in the value, the result is empty.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

### Example(s) from Specification
``` fhirpath
@2012-01-01T03:30:40.002-07:00.hourOf() // 3
@2012-01-01T16:30:40.002-07:00.hourOf() // 16
```

### Coverage
0 tests found for `hourOf`.

**Covered:**
- (none)

**Gaps:**
- ❌ Returns hour component from DateTime or Time value
- ❌ Empty input or hour not present in value returns empty
- ❌ Multiple items in input signals error

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|

**Summary:** 0/0 (0%) — 0 tests × 6 engines