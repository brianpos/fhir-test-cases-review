## Review `monthOf() : Integer`
Name: monthOf
Date: 2026-02-11
Test Count: 0

### Specification Extract 
Header in specification: monthOf(): Integer

If the input collection contains a single Date or DateTime, this function will return the month component.

If the input collection is empty, or the month is not present in the value, the result is empty.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.


If the component isn't present in the value, then the result is empty

### Example(s) from Specification
``` fhirpath
@2014-01-05T10:30:00.000.monthOf() // 1
```

``` fhirpath
@2012.monthOf() // {} an empty collection
```

### Coverage
0 tests found for `monthOf`.

**Covered:**
- (none)

**Gaps:**
- ❌ Single Date or DateTime input returns the month component
- ❌ Empty input or month not present in value returns empty
- ❌ Multiple items in input signals error

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|

**Summary:** 0/0 (0%) — 0 tests × 6 engines