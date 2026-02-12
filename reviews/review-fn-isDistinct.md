## Review `isDistinct() : Boolean`
Name: isDistinct
Date: 2026-02-11
Test Count: 3

### Specification Extract 
Header in specification: isDistinct() : Boolean

Returns `true` if all the items in the input collection are distinct. To determine whether two items are distinct, the [equals](#equals) (`=`) operator is used, as defined below.

Conceptually, this function is shorthand for a comparison of the `count()` of the input collection against the `count()` of the `distinct()` of the input collection:


This means that if the input collection is empty (`{ }`), the result is `true`.

### Example(s) from Specification
``` fhirpath
X.count() = X.distinct().count()
```

### Coverage
3 tests found for `isDistinct` (testDistinct1, testDistinct2, testDistinct3).

**Covered:**
- ✅ All-distinct collection returns true (testDistinct1, testDistinct2)
- ✅ Non-distinct collection returns false (testDistinct3)

**Gaps:**
- ❌ Empty input collection returning true

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testDistinct1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDistinct2 | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| testDistinct3 | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |

**Summary:** 16/18 (89%) — 3 tests × 6 engines

2 test(s) fail in only one engine, suggesting engine-specific implementation issues rather than problems with the tests or specification.
