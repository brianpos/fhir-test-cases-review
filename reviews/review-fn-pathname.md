## Review `pathname([short]) : collection` — STU
Name: pathname
Date: 2026-02-11
Test Count: 0

### Specification Extract 
Header in specification: pathname([short : Boolean]) : collection

<!-- FHIR-45314 -->

> **Note:** The contents of this section are Standard for Trial Use (STU)

Returns the direct path of each item of the input collection within the input resource (`%rootResource` in FHIR implementations),
using only element names and indexers. *Such that if you used that result on the input resource, you would get that node, and only that node.*

If an item in the input collection was derived from computation (e.g. via `substring(..)`, `&`, or mathematical operations) rather than navigation it is excluded from the result.
Items that are outside the input resource, such as those navigated to via resolve() are also excluded from the result, however if resolve()
references a resource contained within the input Resource then it is included (such as with FHIR bundles, or contained resources).

The optional `short` parameter permits excluding array indexers if an element is known to not be an array, either in the model, or in the specific instance at runtime.

If the input collection is empty `({ })`, the result is empty.

This function could be used to populate fields in a FHIR OperationOutcome.issue.expression field, or assist in debugging complex expressions using it in conjunction with trace.

For example, validating a FHIR QuestionnaireResponse (against a Questionnaire) could use the following expression to calculate the location of an invalid answer:


would return the following string *(which is also a valid fhirpath expression)* if only 1 node was at that location in the input QuestionnaireResponse.


Another example could be the FHIR Observation invariant `obs-7` that roughly checks if components are duplicating codings captured at the top level:
*(not an exact copy of the invariant, but a part of it)*


would return the following strings: (simplifying finding the specific component(s) that were duplicated)

### Example(s) from Specification
``` fhirpath
item.item.item.where(linkId = 'i508').item.where(linkId='i534').answer.value.pathname()
```

``` fhirpath
'QuestionnaireResponse.item[2].item[8].item[1].item[1].answer[0].value[0]'
```

``` fhirpath
// trace out the pathname of the components that have duplicated codings
component.code.where(coding.intersect(%resource.code.coding).trace('component', pathname()).exists()).empty()
```

``` fhirpath
'Observation.component[0].code[0].coding[0]'
'Observation.component[23].code[0].coding[0]'
```

### Coverage
0 tests found for `pathname`.

**Covered:**
- (none)

**Gaps:**
- ❌ Returns direct path of each item within input resource using element names and indexers
- ❌ Items derived from computation (substring, &, math) are excluded from result
- ❌ Items outside input resource via resolve() are excluded, except contained resources
- ❌ Optional short parameter excludes array indexers for non-array elements
- ❌ Empty input collection returns empty

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|

**Summary:** 0/0 (0%) — 0 tests × 6 engines