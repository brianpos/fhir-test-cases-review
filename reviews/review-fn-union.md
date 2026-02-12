## Review `union(other) : collection`
Name: union
Date: 2026-02-11
Test Count: 5

### Specification Extract 
Header in specification: union(other : collection) : collection

Merge the two collections into a single collection, eliminating any duplicate values (using [equals](#equals) (`=`) to determine equality). There is no expectation of order in the resulting collection.

In other words, this function returns the distinct list of items from both inputs. For example, consider two lists of integers `A: 1, 1, 2, 3` and `B: 2, 3`:


This function can also be invoked using the `|` operator.

e.g. `x.union(y)` is synonymous with `x | y`

e.g. `name.select(use.union(given))` is the same as `name.select(use | given)`, noting that the union function does not introduce an iteration context, in this example the select introduces the iteration context on the name element.

### Example(s) from Specification
``` fhirpath
A.union( B ) // 1, 2, 3
A.union( { } ) // 1, 2, 3
```

### Coverage

5 tests found for `union` (testUnion4, testUnion5, testUnion8, testUnion10, testUnion11).

**Covered:**
- ✅ Merging collections via chained and nested unions (testUnion4, testUnion5)
- ✅ Duplicate elimination using equals semantics (testUnion8)
- ✅ union does not introduce iteration context within select (testUnion10, testUnion11)

**Gaps:**
- ❌ No test for union with empty collection (e.g. A.union({}) returns distinct items from A)
- ❌ No test verifying equivalence with | operator (x.union(y) synonymous with x | y)
- ❌ No test verifying order independence of result

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testUnion10 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testUnion11 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testUnion4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testUnion5 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testUnion8 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 28/30 (93%) — 5 tests × 6 engines

2 test(s) fail in only one engine, suggesting engine-specific implementation issues rather than problems with the tests or specification.
