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
- ✅ Basic splitting by single-character separator (testSplit1)
- ✅ Preserving empty segments between consecutive separators (testSplit2)
- ✅ Multi-character separator splitting and round-trip with join (testSplit3, testSplit4)

**Gaps:**
- ❌ Empty input returns empty
- ❌ No separator match returns input string unchanged (e.g. 'ABC'.split(','))

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testSplit1 | N/A | ✅ | ✅ | ✅ | ✅ | ✅ |
| testSplit2 | N/A | ✅ | ✅ | ✅ | ✅ | ✅ |
| testSplit3 | N/A | ✅ | ✅ | ✅ | ✅ | ✅ |
| testSplit4 | N/A | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 20/24 (83%) — 4 tests × 6 engines

4 test(s) are not implemented in some engines, but all implemented tests pass.
