## Review `split(separator) : collection`
Name: split
Date: 2026-02-11
Test Count: 4

### Specification Extract 
Header in specification: split(separator: String) : collection

The split function splits a singleton input string into a list of strings, using the given separator.

If the input is empty, the result is empty.

If the input string does not contain any appearances of the separator, the result is the input string.

The following example illustrates the behavior of the `.split` operator:

### Example(s) from Specification
``` fhirpath
('A,B,C').split(',') // { 'A', 'B', 'C' }
('ABC').split(',') // { 'ABC' }
'A,,C'.split(',') // { 'A', '', 'C' }
```

### Coverage
4 tests found for `split` (testSplit1, testSplit2, testSplit3, testSplit4).

**Covered:**
- ✅ Splits singleton string into list using given separator (testSplit1)
- ✅ Handles consecutive separators producing empty strings in result (testSplit2)
- ✅ Multi-character separator support (testSplit3, testSplit4)
- ✅ Split and join roundtrip preserves original string (testSplit2, testSplit4)

**Gaps:**
- ❌ Empty input returns empty
- ❌ Input with no separator appearances returns input string unchanged

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testSplit1 | N/A | ✅ | ✅ | ✅ | ✅ | ✅ |
| testSplit2 | N/A | ✅ | ✅ | ✅ | ✅ | ✅ |
| testSplit3 | N/A | ✅ | ✅ | ✅ | ✅ | ✅ |
| testSplit4 | N/A | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 20/24 (83%) — 4 tests × 6 engines

One engine (Aidbox) does not support split(), accounting for all non-passing results. All tests pass in the 5 engines that support the function.
