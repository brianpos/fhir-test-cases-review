## Review `truncate() : Integer | Quantity`
Name: truncate
Date: 2026-02-11
Test Count: 4

### Specification Extract 
Header in specification: truncate() : Integer | Quantity

Returns the integer portion of the input.

Accepts input types of Decimal or Quantity.

When used with a Decimal input type, the result is an Integer.<br/>
When used with a Quantity, the result is a Quantity with the same units and the value *(Decimal)* set to the integer result calculated.

If the input collection is empty, the result is empty.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.


> Note: We may consider a TruncateLong() function to handle Long output types.

### Example(s) from Specification
``` fhirpath
101.truncate() // 101
1.00000001.truncate() // 1
(-1.56).truncate() // -1
```

### Coverage
4 tests found for `truncate` (testTruncate1, testTruncate2, testTruncate3, testTruncateEmpty).

**Covered:**
- ✅ Returns integer portion of whole number Decimal (testTruncate1)
- ✅ Returns integer portion of fractional Decimal (testTruncate2)
- ✅ Truncation of negative Decimal toward zero (testTruncate3)
- ✅ Empty input returns empty (testTruncateEmpty)

**Gaps:**
- ❌ Quantity input returning Quantity with same units and integer value
- ❌ Multiple items in input collection signals error

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testTruncate1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testTruncate2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testTruncate3 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testTruncateEmpty | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 23/24 (96%) — 4 tests × 6 engines

testTruncate3 (negative decimal truncation) fails in 1 engine, suggesting an engine-specific bug with negative number handling.
