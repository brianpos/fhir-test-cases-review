## Review `indexOf(substring) : Integer`
Name: indexOf
Date: 2026-02-11
Test Count: 6

### Specification Extract 
Header in specification: indexOf(substring : String) : Integer

Returns the 0-based index of the first position `substring` is found in the input string, or -1 if it is not found. <span class="fhir-highlight">The index is measured in characters (Unicode scalar values).</span>

If `substring` is an empty string (`''`), the function returns 0.

If the input or `substring` is empty (`{ }`), the result is empty (`{ }`).

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

### Example(s) from Specification
``` fhirpath
'abcdefg'.indexOf('bc') // 1
'abcdefg'.indexOf('x') // -1
'abcdefg'.indexOf('abcdefg') // 0
```

### Coverage
6 tests found for `indexOf` (testIndexOf1, testIndexOf2, testIndexOf3, testIndexOf5, testIndexOf4, testIndexOf6).

**Covered:**
- ✅ Returns 0-based index of first position substring is found (testIndexOf1)
- ✅ Returns -1 if substring is not found (testIndexOf2)
- ✅ Empty string substring returns 0 (testIndexOf3)
- ✅ If substring is empty collection, result is empty (testIndexOf5)
- ✅ If input is empty collection, result is empty (testIndexOf4)
- ✅ Both input and substring empty collections return empty (testIndexOf6)

**Gaps:**
- ❌ Index measured in Unicode scalar values (no test with multi-byte or combining characters)
- ❌ Multiple items in input collection signals error
- ❌ Finding first occurrence when substring appears multiple times in the string

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testIndexOf1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testIndexOf2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testIndexOf3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testIndexOf5 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testIndexOf4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testIndexOf6 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 35/36 (97%) — 6 tests × 6 engines

testIndexOf5 fails in 1 engine (5/6), suggesting an engine-specific bug with empty-collection substring handling.
