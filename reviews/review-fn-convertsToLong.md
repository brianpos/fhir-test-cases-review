## Review `convertsToLong() : Boolean` — STU
Name: convertsToLong
Date: 2026-02-11
Test Count: 0

### Specification Extract 
Header in specification: convertsToLong() : Boolean

If the input collection contains a single item, this function will return `true` if:

* the item is an Integer or Long
* the item is a String and is convertible to a Long
* the item is a Boolean

If the item is not one of the above types, or the item is a String, but is not convertible to an Integer (using the regex format `(\+|-)?\d+`), the result is `false`.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.

If the input collection is empty, the result is empty.

### Example(s) from Specification
_No examples found in specification._

### Coverage

0 tests found for `convertsToLong`.

**Covered:**
(none)

**Gaps:**
- ❌ All specification requirements lack test coverage
