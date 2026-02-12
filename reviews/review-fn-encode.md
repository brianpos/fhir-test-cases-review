## Review `encode(format) : String`
Name: encode
Date: 2026-02-11
Test Count: 4

### Specification Extract 
Header in specification: encode(format : String) : String

The encode function takes a singleton string and returns the result of encoding that string in the given format. The format parameter defines the encoding format. Available formats are:

|hex |The string is encoded using hexadecimal characters (base 16) in lowercase |
|=|=|
|base64 |The string is encoded using standard base64 encoding, using A-Z, a-z, 0-9, +, and /, output padded with = |
|urlbase64 |The string is encoded using url base 64 encoding, using A-Z, a-z, 0-9, -, and _, output padded with = |
|ascii | The string has any character above character code 127 replaced with `?`. *This is a lossy encoding, and not reversible via `decode`*

Base64 encodings are described in [RFC4648](https://tools.ietf.org/html/rfc4648#section-4).

If the input is empty, the result is empty.

If no format is specified, the result is empty.

### Example(s) from Specification
_No examples found in specification._

### Coverage
4 tests found for `encode` (testEncodeBase64A, testEncodeHex, testEncodeBase64B, testEncodeUrlBase64).

**Covered:**
- ✅ Encoding to base64 format (testEncodeBase64A, testEncodeBase64B)
- ✅ Encoding to hex format (testEncodeHex)
- ✅ Encoding to urlbase64 format (testEncodeUrlBase64)

**Gaps:**
- ❌ No test for ascii encoding format
- ❌ No test for empty input returning empty
- ❌ No test for missing format parameter returning empty

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testEncodeBase64A | N/A | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEncodeBase64B | N/A | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEncodeHex | N/A | ✅ | ✅ | ✅ | ✅ | ✅ |
| testEncodeUrlBase64 | N/A | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 20/24 (83%) — 4 tests × 6 engines

4 test(s) are not implemented in some engines, but all implemented tests pass.
