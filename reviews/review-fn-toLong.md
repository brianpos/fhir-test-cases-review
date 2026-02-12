## Review `toLong() : Long` — STU
Name: toLong
Date: 2026-02-11
Test Count: 0

### Specification Extract 
Header in specification: toLong() : Long

> **Note:** The contents of this section are Standard for Trial Use (STU)

If the input collection contains a single item, this function will return a single integer if:

* the item is an Integer or Long
* the item is a String and is convertible to a 64 bit integer
* the item is a Boolean, where `true` results in a 1 and `false` results in a 0.

If the item is not one the above types, the result is empty.

If the item is a String, but the string is not convertible to a 64 bit integer (using the regex format `(\+|-)?\d+`), the result is empty.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

If the input collection is empty, the result is empty.

### Example(s) from Specification
_No examples found in specification._

### Coverage
0 tests found for `toLong`.

**Covered:**
(none)

**Gaps:**
- ❌ All specification requirements lack test coverage

### Test Results

No tests exist for this function yet. Test results will be added once tests are created.
