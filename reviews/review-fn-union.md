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
- ✅ Merges collections into a single collection (testUnion4, testUnion5)
- ✅ Eliminates duplicate values (testUnion8)
- ✅ Union does not introduce iteration context when used inside select (testUnion10, testUnion11)

**Gaps:**
- ❌ Union with empty collection returns distinct items from non-empty collection
- ❌ | operator as synonym for union function
- ❌ Equality determination uses equals (=) semantics for deduplication

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testUnion4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testUnion5 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testUnion8 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testUnion10 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testUnion11 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 28/30 (93%) — 5 tests × 6 engines

testUnion10 and testUnion11 each fail in 1 engine, suggesting an engine-specific bug with iteration context handling.
