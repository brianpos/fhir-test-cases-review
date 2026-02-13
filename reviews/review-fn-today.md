## Review `today() : Date`
Name: today
Date: 2026-02-11
Test Count: 2

### Specification Extract 
Header in specification: today() : Date

Returns the current date.

### Example(s) from Specification
_No examples found in specification._

### Coverage
2 tests found for `today` (testToday1, testToday2).

**Covered:**
- ✅ Returns the current date, comparable with other dates (testToday1)
- ✅ Return type is Date with YYYY-MM-DD format (10 characters) (testToday2)

**Gaps:**
- ❌ Deterministic evaluation: today() returns same value within a single expression

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testToday1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testToday2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 12/12 (100%) — 2 tests × 6 engines
