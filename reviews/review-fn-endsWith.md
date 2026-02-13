## Review `endsWith(suffix) : Boolean`
Name: endsWith
Date: 2026-02-11
Test Count: 12

### Specification Extract 
Header in specification: endsWith(suffix : String) : Boolean

Returns `true` when the input string ends with the given `suffix`.

If `suffix` is the empty string (`''`), the result is `true`.

If the input collection is empty, the result is empty.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

### Example(s) from Specification
``` fhirpath
'abcdefg'.endsWith('efg') // true
'abcdefg'.endsWith('abc') // false
```

### Coverage
12 tests found for `endsWith` (testEndsWith1, testEndsWith2, testEndsWith3, testEndsWith4, testEndsWith5, testEndsWith6, testEndsWith7, testEndsWith8, testEndsWith9, testEndsWith10, testEndsWith10a, testEndsWithNonString1).

**Covered:**
- ✅ Returns true when string ends with given suffix (testEndsWith2, testEndsWith3)
- ✅ Returns false when string does not end with suffix (testEndsWith1, testEndsWith4)
- ✅ Full string matches as suffix (testEndsWith5)
- ✅ Returns false when suffix is longer than input (testEndsWith6)
- ✅ Empty suffix returns true (testEndsWith7)
- ✅ Empty input collection returns empty (testEndsWith8, testEndsWith9)
- ✅ Works within select context with computed suffix (testEndsWith10)
- ✅ Semantic error when suffix argument evaluates to collection (testEndsWith10a)
- ✅ Non-string input signals error (testEndsWithNonString1)

**Gaps:**
- ❌ Multiple items in input collection signals error

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testEndsWith1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEndsWith2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEndsWith3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEndsWith4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEndsWith5 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEndsWith6 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEndsWith7 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEndsWith8 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEndsWith9 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEndsWith10 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEndsWith10a | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEndsWithNonString1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 71/72 (99%) — 12 tests × 6 engines

testEndsWith10a fails in 1 engine, suggesting an engine-specific bug with computed suffix arguments.
