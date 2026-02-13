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
- ✅ Returns true when all items in collection are distinct (testDistinct1, testDistinct2)
- ✅ Returns false when items are not distinct (testDistinct3)

**Gaps:**
- ❌ Empty input returns true
- ❌ Uses equals operator for distinctness comparison (no test with types where equals semantics matter)
- ❌ Single item collection returns true

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testDistinct1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testDistinct2 | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| testDistinct3 | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |

**Summary:** 16/18 (89%) — 3 tests × 6 engines

testDistinct2 and testDistinct3 each fail in 1 engine (5/6), suggesting engine-specific bugs with descendants() or linkId traversal rather than isDistinct itself.
