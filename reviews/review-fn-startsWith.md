## Review `startsWith(prefix) : Boolean`
Name: startsWith
Date: 2026-02-11
Test Count: 14

### Specification Extract 
Header in specification: startsWith(prefix : String) : Boolean

Returns `true` when the input string starts with the given `prefix`.

If `prefix` is the empty string (`''`), the result is `true`.

If the input collection is empty, the result is empty.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

### Example(s) from Specification
``` fhirpath
'abcdefg'.startsWith('abc') // true
'abcdefg'.startsWith('xyz') // false
```

### Coverage
14 tests found for `startsWith` (testStartsWith1, testStartsWith2, testStartsWith3, testStartsWith4, testStartsWith5, testStartsWith6, testStartsWith7, testStartsWith8, testStartsWith9, testStartsWith10, testStartsWith11, testStartsWith12, testStartsWith12a, testStartsWithNonString1).

**Covered:**
- ✅ Prefix matching returning true and false (testStartsWith1, testStartsWith2, testStartsWith3, testStartsWith4)
- ✅ Exact full-string match and prefix longer than input (testStartsWith5, testStartsWith6)
- ✅ Empty prefix returns true (testStartsWith7, testStartsWith10)
- ✅ Empty input collection returns empty (testStartsWith8, testStartsWith9, testStartsWith11)
- ✅ Dynamic prefix via nested expression in select context (testStartsWith12)
- ✅ Semantic error on non-string input type and on non-literal argument outside select (testStartsWith12a, testStartsWithNonString1)

**Gaps:**
- ❌ Error on multiple items in input collection

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testStartsWith1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStartsWith2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStartsWith3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStartsWith4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStartsWith5 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStartsWith6 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStartsWith7 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStartsWith8 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStartsWith9 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStartsWith10 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStartsWith11 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStartsWith12 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStartsWith12a | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testStartsWithNonString1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 83/84 (99%) — 14 tests × 6 engines

1 test(s) fail in only one engine, suggesting engine-specific implementation issues rather than problems with the tests or specification.
