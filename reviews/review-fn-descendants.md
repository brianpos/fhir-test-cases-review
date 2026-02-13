## Review `descendants() : collection`
Name: descendants
Date: 2026-02-11
Test Count: 1

### Specification Extract 
Header in specification: descendants() : collection

Returns a collection with all descendant nodes of all items in the input collection. The result does not include the items in the input collection themselves. This function is a shorthand for `repeat(children())`. Note that the ordering of the children is undefined and using functions like `first()` on the result may return different results on different platforms.

> **Note:** Many of these functions will result in a set of items of different underlying types. It may be necessary to use [`ofType()`](#fn-oftype) as described in the previous section to maintain type safety. See [Type safety and strict evaluation](#type-safety-and-strict-evaluation) for more information about type safe use of FHIRPath expressions.

### Example(s) from Specification
_No examples found in specification._

### Coverage
1 tests found for `descendants` (testRepeat3).

**Covered:**
- ✅ Returns descendant nodes from input collection allowing property navigation (testRepeat3)

**Gaps:**
- ❌ Result does not include the items in the input collection themselves
- ❌ Equivalence with repeat(children()) not verified
- ❌ Behavior with multiple items in input collection
- ❌ Ordering of children is undefined (not explicitly tested)

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testRepeat3 | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |

**Summary:** 5/6 (83%) — 1 tests × 6 engines

The single test fails in 1 engine, suggesting an engine-specific bug in descendants() traversal.
