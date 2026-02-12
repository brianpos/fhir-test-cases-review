## Review `sort([keySelector]) : collection`
Name: sort
Date: 2026-02-11
Test Count: 10

### Specification Extract 
Header in specification: sort([keySelector: ($this) => any [asc | desc] [, keySelector: ($this) => any [asc | desc], ...]]) : collection

> **Note:** The contents of this section are Standard for Trial Use (STU)

> This is a [scoped function](#scoped-functions): Each `keySelector` argument is evaluated for each item being compared (setting `$this` to the item for each evaluation). The results are compared to determine sort order. If there are multiple `keySelector` arguments, subsequent selectors are only evaluated for items where the previous `keySelector` comparison resulted in equality (i.e., the sort order hasn't been determined yet). This allows for multi-level sorting with minimal evaluations. <br/>As this function is used to modify the order of the collection the `$index` variable is undefined in this context, it could be anywhere during any evaluation depending on algorithms selected.

Returns a collection containing the items in the input collection, sorted according to the specified key selector expressions. The function takes a variable number of key selector parameters, each of which can be optionally qualified with `asc` (ascending) or `desc` (descending). If no qualifier is provided, `asc` is the default.

If no key selector parameters are provided, the sort uses the default ordering for the type of data in the input collection, using the same comparison semantics as defined for the equals (`=`) and comparison operators (`>`, `>=`, `<`, `<=`).

Each key selector expression is evaluated for each item in the input collection using singleton evaluation semantics. If the key selector expression evaluates to a collection with more than one item, the evaluation will end and signal an error to the calling environment.

comparing values returned by the no key selector using the same comparison semantics as defined for the equals (`=`) and comparison operators (`>`, `>=`, `<`, `<=`).

An empty value is considered lower than all other values, meaning they will appear before others when sorted ascending.

When comparing two items, if the values for the first key selector are equal, the comparison proceeds to the next key selector, and so on until all key selectors have been evaluated or a difference is found.

Attempting to sort items with incompatible types will result in an error. Values that would result in comparison errors must be filtered from the collection prior to sorting.

If the input collection is empty (`{ }`), the result is empty.

The following examples illustrate the use of the `sort()` function:

### Example(s) from Specification
``` fhirpath
(3 | 1 | 2).sort() // (1 | 2 | 3) - natural numeric ordering
(3 | 1 | 2).sort($this) // (1 | 2 | 3) - explicit ascending
(3 | 1 | 2).sort($this desc) // (3 | 2 | 1) - descending
('c' | 'a' | 'b').sort() // ('a' | 'b' | 'c') - default string ordering
('c' | 'a' | 'b').sort($this desc) // ('c' | 'b' | 'a') - descending
Patient.name.sort(family desc, given.first()) // sort by family name descending, then by first given name ascending
Patient.telecom.sort(system, use desc) // sort by system ascending, then by use descending
```

### Coverage

10 tests found for `sort` (testSort1, testSort2, testSort3, testSort4, testSort5, testSort6, testSort7, testSort8, testSort9, testSort10).

**Covered:**
- ✅ Default numeric ordering without key selector (testSort1, testSort2)
- ✅ Explicit $this key selector ascending (testSort3, testSort4)
- ✅ Descending sort via negation (testSort5, testSort8)
- ✅ String sorting ascending and descending (testSort6, testSort7)
- ✅ Sorting actual resource data by field (testSort9)
- ✅ Multi-key descending sort on complex resource (testSort10)

**Gaps:**
- ❌ Empty input collection returns empty
- ❌ Empty values sorted before others (lowest value ordering)
- ❌ Error on incompatible types in collection
- ❌ Error when key selector returns multiple items

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testSort1 | N/A | N/A | N/A | ✅ | ✅ | ✅ |
| testSort10 | N/A | N/A | N/A | ✅ | ✅ | ✅ |
| testSort2 | N/A | N/A | N/A | ✅ | ✅ | ✅ |
| testSort3 | N/A | N/A | N/A | ✅ | ✅ | ✅ |
| testSort4 | N/A | N/A | N/A | ✅ | ✅ | ✅ |
| testSort5 | N/A | N/A | N/A | ✅ | ✅ | ✅ |
| testSort6 | N/A | N/A | N/A | ✅ | ✅ | ✅ |
| testSort7 | N/A | N/A | N/A | ✅ | ✅ | ✅ |
| testSort8 | N/A | N/A | N/A | ✅ | ✅ | ✅ |
| testSort9 | N/A | N/A | N/A | ✅ | ✅ | ✅ |

**Summary:** 30/60 (50%) — 10 tests × 6 engines

10 test(s) are not implemented in some engines, but all implemented tests pass.
