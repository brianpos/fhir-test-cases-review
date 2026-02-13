## Review `avg() : Decimal | Quantity` — STU
Name: avg
Date: 2026-02-11
Test Count: 0

### Specification Extract 
Header in specification: avg() : Decimal | Quantity

Returns the average of all items in the input collection (in the same type).

Accepts input collections with items of type: Decimal or Quantity.

When used with Integer or Long, the arguments will be implicitly converted to Decimal before evaluation.

All items in the input collection SHALL be the same type, otherwise an exception is thrown.

If the input collection is empty (`{ }`), the result is empty.

The following examples illustrate the behavior of the `avg` function:

### Example(s) from Specification
``` fhirpath
( 5.5 | 4.7 | 4.8 ).avg() // 5.0
( 5.5 'cm' | 4.7 'cm' | 4.8 'cm' ).avg() // 5.0 'cm'
```

### Coverage
0 tests found for `avg`.

**Covered:**
- (none)

**Gaps:**
- ❌ Returns average of all items in input collection not tested
- ❌ Accepts Decimal input type not tested
- ❌ Accepts Quantity input type not tested
- ❌ Integer and Long arguments implicitly converted to Decimal not tested
- ❌ All items must be same type, otherwise exception not tested
- ❌ Empty input returns empty not tested

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|

**Summary:** 0/0 (0%) — 0 tests × 6 engines
