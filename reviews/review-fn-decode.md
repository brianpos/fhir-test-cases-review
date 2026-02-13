## Review `decode(format) : String`
Name: decode
Date: 2026-02-11
Test Count: 4

### Specification Extract 
Header in specification: decode(format : String) : String

The decode function takes a singleton encoded string and returns the result of decoding that string according to the given format. The format parameter defines the encoding format. Available formats are listed in the encode function (excluding 'ascii').

If the input is empty, the result is empty.

If no format is specified, the result is empty.

### Example(s) from Specification
_No examples found in specification._

### Coverage
4 tests found for `decode` (testDecodeBase64A, testDecodeHex, testDecodeBase64B, testDecodeUrlBase64).

**Covered:**
- ✅ Decoding base64 encoded strings (testDecodeBase64A, testDecodeBase64B)
- ✅ Decoding hex encoded string (testDecodeHex)
- ✅ Decoding urlbase64 encoded string (testDecodeUrlBase64)

**Gaps:**
- ❌ No test for empty input returning empty
- ❌ No test for missing format parameter returning empty

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testDecodeBase64A | N/A | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDecodeHex | N/A | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDecodeBase64B | N/A | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDecodeUrlBase64 | N/A | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 20/24 (83%) — 4 tests × 6 engines

4 test(s) are not implemented in some engines, but all implemented tests pass.
