## Review `now() : DateTime`
Name: now
Date: 2026-02-11
Test Count: 2

### Specification Extract 
Header in specification: now() : DateTime

Returns the current date and time, including timezone offset.

### Example(s) from Specification
_No examples found in specification._

### Coverage
2 tests found for `now` (testNow1, testNow2).

**Covered:**
- ✅ Returns a DateTime usable in comparisons and with length > 10 indicating timezone inclusion (testNow1, testNow2)

**Gaps:**
- ❌ No direct assertion that result includes timezone offset

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testNow1 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNow2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 11/12 (92%) — 2 tests × 6 engines

1 test(s) fail in only one engine, suggesting engine-specific implementation issues rather than problems with the tests or specification.
