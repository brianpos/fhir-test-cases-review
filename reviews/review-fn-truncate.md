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
- ✅ Returns integer portion of Decimal input (testTruncate1, testTruncate2)
- ✅ Negative decimal truncation toward zero (testTruncate3)
- ✅ Empty input returns empty (testTruncateEmpty)

**Gaps:**
- ❌ No tests for Quantity input (result should be Quantity with same units and integer value)
- ❌ No tests for multiple items in input collection (should signal error)

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testTruncate1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testTruncate2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testTruncate3 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testTruncateEmpty | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 23/24 (96%) — 4 tests × 6 engines

1 test(s) fail in only one engine, suggesting engine-specific implementation issues rather than problems with the tests or specification.
