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
- ✅ Invocation `.` binds tighter than unary `-` (testPrecedence1)
- ✅ `*` binds tighter than `+` (testPrecedence2)
- ✅ `>` binds tighter than `is` (testPrecedence3)
- ✅ `is` binds tighter than `|` (testPrecedence4)
- ✅ `and` binds tighter than `in` is not the case — `in` binds tighter than `and` (testPrecedence5)
- ✅ Complex nested precedence with `and`, `in`, `|`, `.` in real-world expression (testPrecedence6)

**Gaps:**
- ❌ No test for `div`/`mod` precedence vs `+`/`-` (level #04 vs #05)
- ❌ No test for `as` precedence (level #06)
- ❌ No test for `xor`/`or` vs `implies` precedence (level #12 vs #13)

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

1 test(s) fail in only one engine, suggesting engine-specific implementation issues rather than problems with the tests or specification. 2 test(s) fail in multiple (but not all) engines, which may indicate differing interpretations of the specification.
