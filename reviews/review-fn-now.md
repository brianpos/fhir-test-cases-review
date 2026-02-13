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
- ✅ Returns the current date and time, comparable with date values (testNow1)
- ✅ Result includes time component beyond just date (testNow2)

**Gaps:**
- ❌ Result includes timezone offset
- ❌ Deterministic evaluation — returns same value within a given expression

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testNow1 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testNow2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 11/12 (92%) — 2 tests × 6 engines

testNow1 fails in 1 engine (5/6 pass), suggesting an engine-specific bug with date/DateTime comparison involving now().
