## Review `escape(target) : String`
Name: escape
Date: 2026-02-11
Test Count: 2

### Specification Extract 
Header in specification: escape(target : String) : String

The escape function takes a singleton string and escapes it for a given target, as specified in the following table:

|html |The string is escaped such that it can appear as valid HTML content (at least open bracket (`<`), ampersand (`&`), and quotes (`"`), but ideally anything with a character encoding above 127) |
|=|=|
|json |The string is escaped such that it can appear as a valid JSON string (quotes (`"`) are escaped as (`\"`)); additional escape characters are described in the [String](#string) escape section|

If the input is empty, the result is empty.

If no target is specified, the result is empty.

### Example(s) from Specification
_No examples found in specification._

### Coverage
2 tests found for `escape` (testEscapeHtml, testEscapeJson).

**Covered:**
- ✅ HTML escaping of < and " characters (testEscapeHtml)
- ✅ JSON escaping of " characters (testEscapeJson)

**Gaps:**
- ❌ HTML escaping of & character
- ❌ HTML escaping of characters with encoding above 127
- ❌ Empty input returns empty
- ❌ No target specified returns empty

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testEscapeHtml | N/A | N/A | ✅ | ✅ | ✅ | ✅ |
| testEscapeJson | N/A | N/A | ✅ | ✅ | ✅ | ✅ |

**Summary:** 8/12 (67%) — 2 tests × 6 engines

Two engines do not produce results for escape tests, suggesting the escape function is not yet widely implemented.
