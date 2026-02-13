## Review Unary `+` (positive) / `-` (negation)
Name: polarity
Date: 2026-02-11
Test Count: 3

### Specification Extract 
Header in specification: Unary operators (`+` and `-`)

> **Note:** The contents of this section are Standard for Trial Use (STU)

The unary operators support a single item input operand of type Integer, Long, Decimal, or Quantity. The output type is the same as the input type.
Using with any incompatible type will end and signal an error to the calling environment.

The `+` operator returns the value of its operand unchanged.

The `-` operator will negate the numeric value. If the value is a Quantity, the unit remains unchanged.

> **Note:** The CQL language describes the `-` operator as unary negation.

If the result of negating the number cannot be represented, the result is empty (`{ }`).

If the input collection is empty, the result is empty (`{ }`).

examples:

### Example(s) from Specification
``` fhirpath
+5 // a simple literal 5 numeric value
-4 // a simple negative value
-Account.balance.amount // The negated account balance
```

### Coverage
3 tests found for `polarity` (testPolarityPrecedence, testLiteralIntegerLessThanPolarityTrue, testLiteralIntegerLessThanPolarityFalse).

**Covered:**
- ✅ Unary negation applied to expression result (testPolarityPrecedence)
- ✅ Unary + with integer literal (testLiteralIntegerLessThanPolarityTrue)
- ✅ Unary - with integer literal (testLiteralIntegerLessThanPolarityFalse)

**Gaps:**
- ❌ Unary + returns operand unchanged explicitly verified (e.g. +5 = 5)
- ❌ Unary - with Decimal type
- ❌ Unary - with Quantity type (unit remains unchanged)
- ❌ Unary operators with Long type
- ❌ Incompatible type signals error
- ❌ Empty input returns empty
- ❌ Result that cannot be represented returns empty

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testPolarityPrecedence | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLiteralIntegerLessThanPolarityTrue | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testLiteralIntegerLessThanPolarityFalse | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 16/18 (89%) — 3 tests × 6 engines

2 of 3 tests fail in the same single engine, suggesting an engine-specific bug with unary operator handling.
