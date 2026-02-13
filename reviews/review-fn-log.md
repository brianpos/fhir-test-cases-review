## Review `log(base) : Decimal`
Name: log
Date: 2026-02-11
Test Count: 5

### Specification Extract 
Header in specification: log(base : Decimal) : Decimal

Returns the logarithm base `base` of the input number.

Accepts Decimal input types. Integer and Long types are also accepted via implicit conversion to Decimal. 

If the input is 0 or negative, the evaluation will end and signal an error to the calling environment.
If the base argument is 0 or negative, the evaluation will end and signal an error to the calling environment.

If `base` is empty, the result is empty.

If the input collection is empty, the result is empty.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

### Example(s) from Specification
``` fhirpath
16.log(2) // 4.0
100.0.log(10.0) // 2.0
```

### Coverage
5 tests found for `log` (testLog1, testLog2, testLogEmpty, testLogEmpty2, testLogEmpty3).

**Covered:**
- ✅ Returns logarithm with given base (testLog1, testLog2)
- ✅ Accepts Integer input via implicit conversion to Decimal (testLog1)
- ✅ Accepts Decimal input (testLog2)
- ✅ Empty input returns empty (testLogEmpty)
- ✅ Empty base returns empty (testLogEmpty3)
- ✅ Both input and base empty returns empty (testLogEmpty2)

**Gaps:**
- ❌ Input is 0 or negative signals error
- ❌ Base is 0 or negative signals error
- ❌ Multiple items in input collection signals error
- ❌ Long type input via implicit conversion

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testLog1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLog2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLogEmpty | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLogEmpty2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLogEmpty3 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 29/30 (97%) — 5 tests × 6 engines

testLogEmpty3 fails in 1 engine (5/6), suggesting an engine-specific bug with empty base handling.
