## Review `sum() : Integer | Decimal | Quantity` — STU
Name: sum
Date: 2026-02-11
Test Count: 0

### Specification Extract 
Header in specification: sum() : Integer | Long | Decimal | Quantity

Returns the sum of all items in the input collection (in the same type).

Accepts input collections with items of type: Integer, Long, Decimal or Quantity.

All items in the input collection SHALL be the same type, otherwise an exception is thrown.

If the input collection is empty (`{ }`), the result is empty.

The following examples illustrate the behavior of the `sum` function:

### Example(s) from Specification
``` fhirpath
( 1.0 | 2.0 | 3.0 | 4.0 | 5.0 ).sum() // 15.0
( 1.0 'mg' | 2.0 'mg' | 3.0 'mg' | 4.0 'mg' | 5.0 'mg' ).sum() // 15.0 'mg'
```

### Coverage
0 tests found for `sum`.

**Covered:**
- (none)

**Gaps:**
- ❌ Returns sum of all items in input collection
- ❌ Accepts Integer, Long, Decimal, and Quantity input types
- ❌ All items must be the same type or exception is thrown
- ❌ Empty input returns empty

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|

**Summary:** 0/0 (0%) — 0 tests × 6 engines