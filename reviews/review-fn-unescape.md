## Review `unescape(target) : String`
Name: unescape
Date: 2026-02-11
Test Count: 2

### Specification Extract 
Header in specification: unescape(target : String) : String

The unescape function takes a singleton string and unescapes it for a given target. The available targets are specified in the escape function description.

If the input is empty, the result is empty.

If no target is specified, the result is empty.

### Example(s) from Specification
_No examples found in specification._

### Coverage

2 tests found for `unescape` (testUnescapeHtml, testUnescapeJson).

**Covered:**
- ✅ HTML unescaping of entities (testUnescapeHtml)
- ✅ JSON unescaping of escaped characters (testUnescapeJson)

**Gaps:**
- ❌ No test for empty input returning empty
- ❌ No test for missing/unspecified target returning empty

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testUnescapeHtml | N/A | N/A | ✅ | ✅ | ✅ | ✅ |
| testUnescapeJson | N/A | N/A | ✅ | ✅ | ✅ | ✅ |

**Summary:** 8/12 (67%) — 2 tests × 6 engines

2 test(s) are not implemented in some engines, but all implemented tests pass.
