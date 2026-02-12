## Review `round([precision]) : Decimal | Quantity`
Name: round
Date: 2026-02-11
Test Count: 3

### Specification Extract 
Header in specification: round([precision : Integer]) : Decimal | Quantity

> [Discussion on this topic](https://chat.fhir.org/#narrow/stream/179266-fhirpath/topic/round.28.29.20for.20negative.20numbers) If you have specific proposals or feedback please log a change request.

Rounds the input to the nearest whole number using a traditional round (i.e. to the nearest whole number), meaning that a decimal value greater than or equal to 0.5 and less than 1.0 will round to 1, and a decimal value less than or equal to -0.5 and greater than -1.0 will round to -1. If specified, the precision argument determines the decimal place at which the rounding will occur. If not specified, the rounding will default to 0 decimal places.

If specified, the number of digits of precision must be >= 0 or the evaluation will end and signal an error to the calling environment.

Accepts input types of Decimal, or Quantity.

When used with a Decimal input type, the result is an Decimal.<br/>
When used with a Quantity, the result is a Quantity with the same units.

When used with Integer or Long, the arguments will be implicitly converted to Decimal before evaluation.

If the input collection is empty, the result is empty.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

### Example(s) from Specification
``` fhirpath
1.round() // 1
3.14159.round(3) // 3.142
```

### Coverage

3 tests found for `round` (testRound1, testRound2, testRoundEmpty).

**Covered:**
- ✅ Rounding without precision argument (testRound1)
- ✅ Rounding with explicit precision argument (testRound2)
- ✅ Empty input returns empty (testRoundEmpty)

**Gaps:**
- ❌ Rounding at 0.5 boundary (e.g. 1.5.round() = 2, 2.5.round() = 3)
- ❌ Negative number rounding
- ❌ Quantity input type returns Quantity with same units
- ❌ Error when precision argument is negative
- ❌ Error on multiple items in input collection

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testRound1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testRound2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testRoundEmpty | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 18/18 (100%) — 3 tests × 6 engines

All tests pass across all engines.
