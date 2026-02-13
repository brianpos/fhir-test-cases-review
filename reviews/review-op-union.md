## Review Union operator
Name: |
Date: 2026-02-11
Test Count: 5

### Specification Extract 
Header in specification: | (union collections)

Merge the two collections into a single collection, eliminating any duplicate values (using [equals](#equals) (`=`)) to determine equality). There is no expectation of order in the resulting collection.

See the [union](#unionother-collection) function for more detail.

### Example(s) from Specification
_No examples found in specification._

### Coverage
5 tests found for `|` (testUnion1, testUnion2, testUnion3, testUnion9, testUnion12).

**Covered:**
- ✅ Union of distinct items preserves all (testUnion1)
- ✅ Duplicate elimination using equals semantics (testUnion2, testUnion3)
- ✅ Union on resource element paths (testUnion9)
- ✅ Union of mixed types (boolean and string) (testUnion12)

**Gaps:**
- ❌ No test for union with empty collection (e.g. `1 | {}` should yield `1`)
- ❌ No test confirming no expectation of order in result

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testUnion1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testUnion2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testUnion3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testUnion9 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testUnion12 | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 28/30 (93%) — 5 tests × 6 engines

2 test(s) fail in only one engine, suggesting engine-specific implementation issues rather than problems with the tests or specification.
