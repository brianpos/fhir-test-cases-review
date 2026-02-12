## Overview
This project provides an AI generated (and human reviewed) analysis of the FHIR unit tests - specifically for the FHIRPath R5 content
It was reviewed using Claude Opus 4.6 via the copilot CLI.

The Test coverage summary was generated from the CI content for the next version of fhirpath, specifically at this branch:
* https://github.com/HL7/FHIRPath/tree/BP-2026-block-jan
* https://github.com/HL7/FHIRPath/blob/BP-2026-block-jan/functions-review.md

Which is published at:
https://build.fhir.org/ig/HL7/FHIRPath/branches/BP-2026-block-jan

The unit tests (cloned locally) are from:
https://github.com/FHIR/fhir-test-cases/tree/master/r5/fhirpath

> The `# Checks` column in the summary tables reports the number of unit tests in the test file that are directly focusing on testing the specific feature, and the number after (in brackets) it is the percentage of those that pass when evaluated on the fhirpath-lab's test engine, results available here:
https://dev.fhirpath-lab.com/FhirPath-engines

> The `Reviewed` column has a check if the review filename has no gaps reported in it, and all tests pass over all engines, indicating that the feature is very mature and well supported.

> **Note:** There may be some tests included here and in the lab screens that aren't in the HL7 repo yet while I work on updating the project.
> Specifically i've update the local files to include a new attribute on each test that indicates which feature the test covers, and some additional descriptions.
> This will be contributed soon.


## Test Coverage Summary

### 5.1 Existence

| Name | Description | Section | # Checks | Reviewed | Filename |
|------|-------------|---------|----------|----------|----------|
| empty | `empty() : Boolean` | 5.1.1 | 1 (100%) |  | review-fn-empty.md |
| exists | `exists([criteria]) : Boolean` | 5.1.2 | 5 (100%) |  | review-fn-exists.md |
| all | `all(criteria) : Boolean` | 5.1.3 | 2 (100%) |  | review-fn-all.md |
| allTrue | `allTrue() : Boolean` | 5.1.4 | 3 (94%) |  | review-fn-allTrue.md |
| anyTrue | `anyTrue() : Boolean` | 5.1.5 | 0 |  | review-fn-anyTrue.md |
| allFalse | `allFalse() : Boolean` | 5.1.6 | 0 |  | review-fn-allFalse.md |
| anyFalse | `anyFalse() : Boolean` | 5.1.7 | 0 |  | review-fn-anyFalse.md |
| subsetOf | `subsetOf(other) : Boolean` | 5.1.8 | 3 (94%) |  | review-fn-subsetOf.md |
| supersetOf | `supersetOf(other) : Boolean` | 5.1.9 | 2 (100%) |  | review-fn-supersetOf.md |
| count | `count() : Integer` | 5.1.10 | 5 (100%) |  | review-fn-count.md |
| distinct | `distinct() : collection` | 5.1.11 | 4 (83%) |  | review-fn-distinct.md |
| isDistinct | `isDistinct() : Boolean` | 5.1.12 | 3 (89%) |  | review-fn-isDistinct.md |

### 5.2 Filtering and projection

| Name | Description | Section | # Checks | Reviewed | Filename |
|------|-------------|---------|----------|----------|----------|
| where | `where(criteria) : collection` | 5.2.1 | 5 (97%) |  | review-fn-where.md |
| select | `select(projection) : collection` | 5.2.2 | 3 (89%) |  | review-fn-select.md |
| Instance Selector | Instance Selector / Object Creation — STU | 5.2.3 | 0 |  | review-instance-selector.md |
| sort | `sort([keySelector]) : collection` | 5.2.4 | 10 (50%) |  | review-fn-sort.md |
| repeat | `repeat(projection) : collection` | 5.2.5 | 3 (94%) |  | review-fn-repeat.md |
| repeatAll | `repeatAll(projection) : collection` — STU | 5.2.6 | 0 |  | review-fn-repeatAll.md |
| ofType | `ofType(type) : collection` | 5.2.7 | 10 (85%) |  | review-fn-ofType.md |
| coalesce | `coalesce(value, ...) : collection` — STU | 5.2.8 | 0 |  | review-fn-coalesce.md |

### 5.3 Subsetting

| Name | Description | Section | # Checks | Reviewed | Filename |
|------|-------------|---------|----------|----------|----------|
| [] | `[index] : any` (indexer) | 5.3.1 | 2 (92%) |  | review-indexer.md |
| single | `single() : any` | 5.3.2 | 2 (100%) |  | review-fn-single.md |
| first | `first() : any` | 5.3.3 | 1 (83%) |  | review-fn-first.md |
| last | `last() : any` | 5.3.4 | 1 (83%) |  | review-fn-last.md |
| tail | `tail() : collection` | 5.3.5 | 2 (83%) |  | review-fn-tail.md |
| skip | `skip(num) : collection` | 5.3.6 | 7 (79%) |  | review-fn-skip.md |
| take | `take(num) : collection` | 5.3.7 | 7 (95%) |  | review-fn-take.md |
| intersect | `intersect(other) : collection` | 5.3.8 | 4 (100%) |  | review-fn-intersect.md |
| exclude | `exclude(other) : collection` | 5.3.9 | 4 (100%) |  | review-fn-exclude.md |

### 5.4 Combining

| Name | Description | Section | # Checks | Reviewed | Filename |
|------|-------------|---------|----------|----------|----------|
| union | `union(other) : collection` | 5.4.1 | 5 (93%) |  | review-fn-union.md |
| combine | `combine(other) : collection` | 5.4.2 | 5 (93%) |  | review-fn-combine.md |

### 5.5 Conversion

| Name | Description | Section | # Checks | Reviewed | Filename |
|------|-------------|---------|----------|----------|----------|
| iif | `iif(criterion, true-result, [otherwise])` | 5.5.1 | 19 (87%) |  | review-fn-iif.md |
| toBoolean | `toBoolean() : Boolean` | 5.5.2.1 | 5 (100%) |  | review-fn-toBoolean.md |
| convertsToBoolean | `convertsToBoolean() : Boolean` | 5.5.2.2 | 10 (95%) |  | review-fn-convertsToBoolean.md |
| toInteger | `toInteger() : Integer` | 5.5.3.1 | 12 (94%) |  | review-fn-toInteger.md |
| convertsToInteger | `convertsToInteger() : Boolean` | 5.5.3.2 | 5 (100%) |  | review-fn-convertsToInteger.md |
| toLong | `toLong() : Long` — STU | 5.5.3.3 | 0 |  | review-fn-toLong.md |
| convertsToLong | `convertsToLong() : Boolean` — STU | 5.5.3.4 | 0 |  | review-fn-convertsToLong.md |
| toDate | `toDate([format]) : Date` | 5.5.4.2 | 0 |  | review-fn-toDate.md |
| convertsToDate | `convertsToDate([format]) : Boolean` | 5.5.4.3 | 3 (100%) |  | review-fn-convertsToDate.md |
| toDateTime | `toDateTime([format]) : DateTime` | 5.5.5.1 | 0 |  | review-fn-toDateTime.md |
| convertsToDateTime | `convertsToDateTime([format]) : Boolean` | 5.5.5.2 | 9 (100%) |  | review-fn-convertsToDateTime.md |
| toDecimal | `toDecimal() : Decimal` | 5.5.6.1 | 8 (100%) |  | review-fn-toDecimal.md |
| convertsToDecimal | `convertsToDecimal() : Boolean` | 5.5.6.2 | 6 (100%) |  | review-fn-convertsToDecimal.md |
| toQuantity | `toQuantity([unit]) : Quantity` | 5.5.7.1 | 9 (83%) |  | review-fn-toQuantity.md |
| convertsToQuantity | `convertsToQuantity([unit]) : Boolean` | 5.5.7.2 | 9 (96%) |  | review-fn-convertsToQuantity.md |
| toString | `toString() : String` | 5.5.8.1 | 11 (92%) |  | review-fn-toString.md |
| convertsToString | `convertsToString() : Boolean` | 5.5.8.2 | 6 (100%) |  | review-fn-convertsToString.md |
| toTime | `toTime() : Time` | 5.5.9.1 | 0 |  | review-fn-toTime.md |
| convertsToTime | `convertsToTime() : Boolean` | 5.5.9.2 | 4 (96%) |  | review-fn-convertsToTime.md |

### 5.6 String Manipulation

| Name | Description | Section | # Checks | Reviewed | Filename |
|------|-------------|---------|----------|----------|----------|
| indexOf | `indexOf(substring) : Integer` | 5.6.1 | 6 (97%) |  | review-fn-indexOf.md |
| lastIndexOf | `lastIndexOf(substring) : Integer` — STU | 5.6.2 | 0 |  | review-fn-lastIndexOf.md |
| substring | `substring(start, [length]) : String` | 5.6.3 | 12 (96%) |  | review-fn-substring.md |
| startsWith | `startsWith(prefix) : Boolean` | 5.6.4 | 14 (99%) |  | review-fn-startsWith.md |
| endsWith | `endsWith(suffix) : Boolean` | 5.6.5 | 12 (99%) |  | review-fn-endsWith.md |
| contains | `contains(substring) : Boolean` ¹ | 5.6.6 | 21 (98%) |  | review-fn-contains.md |
| upper | `upper() : String` | 5.6.7 | 2 (100%) |  | review-fn-upper.md |
| lower | `lower() : String` | 5.6.8 | 2 (100%) |  | review-fn-lower.md |
| replace | `replace(pattern, substitution) : String` | 5.6.9 | 6 (94%) |  | review-fn-replace.md |
| matches | `matches(regex, [flags]) : Boolean` | 5.6.10 | 11 (94%) |  | review-fn-matches.md |
| matchesFull | `matchesFull(regex, [flags]) : Boolean` — STU | 5.6.11 | 5 (50%) |  | review-fn-matchesFull.md |
| replaceMatches | `replaceMatches(regex, substitution, [flags]) : String` | 5.6.12 | 7 (88%) |  | review-fn-replaceMatches.md |
| length | `length() : Integer` | 5.6.13 | 6 (100%) |  | review-fn-length.md |
| toChars | `toChars() : collection` | 5.6.14 | 1 (100%) |  | review-fn-toChars.md |

> ¹ `contains` count of 21 is shared between the string function (5.6.6) and collection operator (6.4.3)

### 5.7 Additional String Functions (STU)

| Name | Description | Section | # Checks | Reviewed | Filename |
|------|-------------|---------|----------|----------|----------|
| encode | `encode(format) : String` | 5.7.1 | 4 (83%) |  | review-fn-encode.md |
| decode | `decode(format) : String` | 5.7.2 | 4 (83%) |  | review-fn-decode.md |
| escape | `escape(target) : String` | 5.7.3 | 2 (67%) |  | review-fn-escape.md |
| unescape | `unescape(target) : String` | 5.7.4 | 2 (67%) |  | review-fn-unescape.md |
| trim | `trim() : String` | 5.7.5 | 6 (83%) |  | review-fn-trim.md |
| split | `split(separator) : collection` | 5.7.6 | 4 (83%) |  | review-fn-split.md |
| join | `join([separator]) : String` | 5.7.7 | 1 (100%) |  | review-fn-join.md |

### 5.8 Math (STU)

| Name | Description | Section | # Checks | Reviewed | Filename |
|------|-------------|---------|----------|----------|----------|
| abs | `abs() : Integer \| Decimal \| Quantity` | 5.8.1 | 4 (96%) |  | review-fn-abs.md |
| ceiling | `ceiling() : Integer \| Quantity` | 5.8.2 | 4 (92%) |  | review-fn-ceiling.md |
| exp | `exp() : Decimal` | 5.8.3 | 3 (100%) |  | review-fn-exp.md |
| floor | `floor() : Integer \| Quantity` | 5.8.4 | 4 (92%) |  | review-fn-floor.md |
| ln | `ln() : Decimal` | 5.8.5 | 3 (100%) |  | review-fn-ln.md |
| log | `log(base) : Decimal` | 5.8.6 | 5 (97%) |  | review-fn-log.md |
| power | `power(exponent) : Decimal` | 5.8.7 | 6 (97%) |  | review-fn-power.md |
| round | `round([precision]) : Decimal \| Quantity` | 5.8.8 | 3 (100%) |  | review-fn-round.md |
| sqrt | `sqrt() : Decimal` | 5.8.9 | 3 (100%) |  | review-fn-sqrt.md |
| truncate | `truncate() : Integer \| Quantity` | 5.8.10 | 4 (96%) |  | review-fn-truncate.md |

### 5.9 Tree Navigation

| Name | Description | Section | # Checks | Reviewed | Filename |
|------|-------------|---------|----------|----------|----------|
| children | `children() : collection` | 5.9.1 | 1 (100%) |  | review-fn-children.md |
| descendants | `descendants() : collection` | 5.9.2 | 1 (83%) |  | review-fn-descendants.md |

### 5.10 Utility Functions

| Name | Description | Section | # Checks | Reviewed | Filename |
|------|-------------|---------|----------|----------|----------|
| trace | `trace(name, [projection]) : collection` | 5.10.1 | 2 (100%) |  | review-fn-trace.md |
| pathname | `pathname([short]) : collection` — STU | 5.10.2 | 0 |  | review-fn-pathname.md |
| now | `now() : DateTime` | 5.10.3.1 | 2 (92%) |  | review-fn-now.md |
| timeOfDay | `timeOfDay() : Time` | 5.10.3.2 | 0 |  | review-fn-timeOfDay.md |
| today | `today() : Date` | 5.10.3.3 | 2 (100%) | ✅ | review-fn-today.md |
| defineVariable | `defineVariable(name, [projection]) : collection` — STU | 5.10.4 | 21 (82%) |  | review-fn-defineVariable.md |
| lowBoundary | `lowBoundary([precision]) : Decimal \| Date \| DateTime \| Time` — STU | 5.10.5 | 28 (56%) |  | review-fn-lowBoundary.md |
| highBoundary | `highBoundary([precision]) : Decimal \| Date \| DateTime \| Time` — STU | 5.10.6 | 24 (58%) |  | review-fn-highBoundary.md |
| precision | `precision() : Integer` — STU | 5.10.7 | 6 (47%) |  | review-fn-precision.md |

### 5.10.8 Date/DateTime/Time Components (STU)

| Name | Description | Section | # Checks | Reviewed | Filename |
|------|-------------|---------|----------|----------|----------|
| yearOf | `yearOf() : Integer` | 5.10.8.1 | 0 |  | review-fn-yearOf.md |
| monthOf | `monthOf() : Integer` | 5.10.8.2 | 0 |  | review-fn-monthOf.md |
| dayOf | `dayOf() : Integer` | 5.10.8.3 | 0 |  | review-fn-dayOf.md |
| hourOf | `hourOf() : Integer` | 5.10.8.4 | 0 |  | review-fn-hourOf.md |
| minuteOf | `minuteOf() : Integer` | 5.10.8.5 | 0 |  | review-fn-minuteOf.md |
| secondOf | `secondOf() : Integer` | 5.10.8.6 | 0 |  | review-fn-secondOf.md |
| millisecondOf | `millisecondOf() : Integer` | 5.10.8.7 | 0 |  | review-fn-millisecondOf.md |
| timezoneOffsetOf | `timezoneOffsetOf() : Decimal` | 5.10.8.8 | 0 |  | review-fn-timezoneOffsetOf.md |
| dateOf | `dateOf() : Date` | 5.10.8.9 | 0 |  | review-fn-dateOf.md |
| timeOf | `timeOf() : Time` | 5.10.8.10 | 0 |  | review-fn-timeOf.md |

### 5.11 Date/Time Interval Functions (STU)

| Name | Description | Section | # Checks | Reviewed | Filename |
|------|-------------|---------|----------|----------|----------|
| duration | `duration(value, precision) : Integer` | 5.11.1 | 0 |  | review-fn-duration.md |
| difference | `difference(value, precision) : Integer` | 5.11.2 | 0 |  | review-fn-difference.md |

### 6.1 Equality

| Name | Description | Section | # Checks | Reviewed | Filename |
|------|-------------|---------|----------|----------|----------|
| = | Equals | 6.1.1 | 39 (93%) |  | review-op-equals.md |
| ~ | Equivalent | 6.1.2 | 27 (93%) |  | review-op-equivalent.md |
| != | Not Equals | 6.1.3 | 36 (94%) |  | review-op-not-equals.md |
| !~ | Not Equivalent | 6.1.4 | 22 (97%) |  | review-op-not-equivalent.md |

### 6.2 Comparison

| Name | Description | Section | # Checks | Reviewed | Filename |
|------|-------------|---------|----------|----------|----------|
| > | Greater Than | 6.2.1 | 41 (97%) |  | review-op-greater-than.md |
| < | Less Than | 6.2.2 | 39 (97%) |  | review-op-less-than.md |
| <= | Less or Equal | 6.2.3 | 32 (98%) |  | review-op-less-or-equal.md |
| >= | Greater or Equal | 6.2.4 | 32 (98%) |  | review-op-greater-or-equal.md |
| comparable | `comparable(other) : Boolean` — STU | 6.2.5 | 3 (83%) |  | review-op-comparable.md |

### 6.3 Types

| Name | Description | Section | # Checks | Reviewed | Filename |
|------|-------------|---------|----------|----------|----------|
| is | Type test keyword / `is(type) : Boolean` | 6.3.1–6.3.2 | 47 (95%) |  | review-op-is.md |
| as | Type cast keyword / `as(type) : collection` | 6.3.3–6.3.4 | 11 (86%) |  | review-op-as.md |

### 6.4 Collections

| Name | Description | Section | # Checks | Reviewed | Filename |
|------|-------------|---------|----------|----------|----------|
| \| | Union operator | 6.4.1 | 5 (93%) |  | review-op-union.md |
| in | Membership | 6.4.2 | 8 (96%) |  | review-op-in.md |
| contains | Containership ¹ | 6.4.3 | 21 (98%) |  | review-op-contains.md |

> ¹ `contains` count of 21 is shared between the string function (5.6.6) and collection operator (6.4.3)

### 6.5 Boolean Logic

| Name | Description | Section | # Checks | Reviewed | Filename |
|------|-------------|---------|----------|----------|----------|
| and | Conjunction | 6.5.1 | 10 (100%) | ✅ | review-op-and.md |
| or | Disjunction | 6.5.2 | 9 (100%) |  | review-op-or.md |
| not | `not() : Boolean` | 6.5.3 | 8 (100%) |  | review-op-not.md |
| xor | Exclusive Or | 6.5.4 | 9 (100%) |  | review-op-xor.md |
| implies | Implication | 6.5.5 | 9 (100%) |  | review-op-implies.md |

### 6.6 Math

| Name | Description | Section | # Checks | Reviewed | Filename |
|------|-------------|---------|----------|----------|----------|
| * | Multiplication | 6.6.1 | 8 (98%) |  | review-op-multiply.md |
| / | Division | 6.6.2 | 12 (93%) |  | review-op-divide.md |
| + | Addition / string concatenation | 6.6.3 | 35 (82%) |  | review-op-add.md |
| - | Subtraction | 6.6.4 | 12 (88%) |  | review-op-subtract.md |
| div | Truncated division | 6.6.5 | 10 (97%) |  | review-op-div.md |
| mod | Modulo | 6.6.6 | 10 (97%) |  | review-op-mod.md |
| & | String concatenation | 6.6.7 | 5 (80%) |  | review-op-concat.md |

### 6.7 Date/Time Arithmetic

> Date/time `+` and `-` are covered by the Math operators above (6.6.3, 6.6.4) — no separate testing attribute.

### 6.8 Unary Operators (STU)

| Name | Description | Section | # Checks | Reviewed | Filename |
|------|-------------|---------|----------|----------|----------|
| polarity | Unary `+` (positive) / `-` (negation) | 6.8.1–6.8.2 | 3 (89%) |  | review-polarity.md |

### 6.9 Operator precedence

| Name | Description | Section | # Checks | Reviewed | Filename |
|------|-------------|---------|----------|----------|----------|
| precedence | Operator precedence rules | 6.9 | 6 (86%) |  | review-precedence.md |

### 7 Aggregates (STU)

| Name | Description | Section | # Checks | Reviewed | Filename |
|------|-------------|---------|----------|----------|----------|
| aggregate | `aggregate(aggregator, [init]) : collection` | 7.1 | 4 (83%) |  | review-fn-aggregate.md |
| sum | `sum() : Integer \| Decimal \| Quantity` — STU | 7.2 | 0 |  | review-fn-sum.md |
| min | `min() : any` — STU | 7.3 | 0 |  | review-fn-min.md |
| max | `max() : any` — STU | 7.4 | 0 |  | review-fn-max.md |
| avg | `avg() : Decimal \| Quantity` — STU | 7.5 | 0 |  | review-fn-avg.md |

### 10.2 Reflection

| Name | Description | Section | # Checks | Reviewed | Filename |
|------|-------------|---------|----------|----------|----------|
| type | `type() : collection` | 10.2.2 | 10 (68%) |  | review-fn-type.md |


