## Review `power(exponent) : Decimal`
Name: power
Date: 2026-02-11
Test Count: 6

### Specification Extract 
Header in specification: power(exponent : Integer | Decimal) : Decimal

Raises a number to the `exponent` power.

Accepts input types of Decimal, Integer or Long.

The result is always a Decimal, because raising an Integer to a negative power (such as -1) produces a Decimal result.

If the power cannot be represented (such as -1 raised to the 0.5), the result is empty.

If the input is empty, or exponent is empty, the result is empty.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

### Example(s) from Specification
``` fhirpath
2.power(3) // 8
2.5.power(2) // 6.25
2.power(-1) // 0.5
(-1).power(0.5) // empty ({ })
```

### Coverage
6 tests found for `power` (testPower1, testPower2, testPower3, testPowerEmpty, testPowerEmpty2, testPowerEmpty3).

**Covered:**
- ✅ Integer and Decimal base raised to positive exponent (testPower1, testPower2)
- ✅ Unrepresentable result returns empty, e.g. (-1).power(0.5) (testPower3)
- ✅ Empty input and/or empty exponent returns empty (testPowerEmpty, testPowerEmpty2, testPowerEmpty3)

**Gaps:**
- ❌ Negative exponent producing Decimal result (e.g. 2.power(-1) = 0.5)
- ❌ Error on multiple items in input collection

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testPower1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testPower2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testPower3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testPowerEmpty | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testPowerEmpty2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testPowerEmpty3 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 35/36 (97%) — 6 tests × 6 engines

1 test(s) fail in only one engine, suggesting engine-specific implementation issues rather than problems with the tests or specification.
