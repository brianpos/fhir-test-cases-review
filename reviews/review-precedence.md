## Review Operator precedence rules
Name: precedence
Date: 2026-02-11
Test Count: 6

### Specification Extract 
Header in specification: Operator precedence

Precedence of operations, in order from high to low:


As customary, precedence may be established explicitly using parentheses (`( )`).

As an example, consider the following expression:


Because the invocation operator (`.`) has a higher precedence than the unary negation (`-`), the unary negation will be applied to the result of the combine of 7 and 3, resulting in an error (because unary negation cannot be applied to a list):


Use parentheses to ensure the unary negation applies to the `7`:

### Example(s) from Specification
``` txt
#01 . (path/function invocation)
#02 [] (indexer)
#03 unary + and -
#04: *, /, div, mod
#05: +, -, &
#06: is, as
#07: |
#08: >, <, >=, <=
#09: =, ~, !=, !~
#10: in, contains
#11: and
#12: xor, or
#13: implies
```

``` fhirpath
-7.combine(3)
```

``` fhirpath
-(7.combine(3)) // ERROR
```

``` fhirpath
(-7).combine(3) // { -7, 3 }
```

### Coverage
6 tests found for `precedence` (testPrecedence1, testPrecedence2, testPrecedence3, testPrecedence4, testPrecedence5, testPrecedence6).

**Covered:**
- ✅ Invocation (.) has higher precedence than unary - (testPrecedence1)
- ✅ Multiplication has higher precedence than addition (testPrecedence2)
- ✅ is/as type testing has higher precedence than comparison operators (testPrecedence3)
- ✅ is type testing has higher precedence than union | (testPrecedence4)
- ✅ in/contains has higher precedence than and (testPrecedence5)
- ✅ Complex nested precedence with and, in, exists (testPrecedence6)

**Gaps:**
- ❌ Precedence of [] (indexer) relative to other operators
- ❌ Precedence of div and mod relative to + and -
- ❌ Precedence of & (string concatenation) relative to other operators
- ❌ Precedence of >=, <= relative to = and ~
- ❌ Precedence of !=, !~ operators
- ❌ Precedence of contains operator
- ❌ Precedence of xor relative to or
- ❌ Precedence of implies (lowest precedence)
- ❌ Parentheses explicitly overriding precedence

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|
| testPrecedence1 | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ |
| testPrecedence2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testPrecedence3 | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| testPrecedence4 | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| testPrecedence5 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| testPrecedence6 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Summary:** 31/36 (86%) — 6 tests × 6 engines

3 of 6 tests fail in 1-2 engines each — invocation vs unary precedence, comparison vs is/as, and union vs is, suggesting engine-specific bugs in precedence handling.
