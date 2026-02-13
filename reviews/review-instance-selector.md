## Review Instance Selector / Object Creation — STU
Name: Instance Selector
Date: 2026-02-11
Test Count: 0

### Specification Extract 
Header in specification: Instance Selector/Object Creation

> **Note:** The contents of this section are Standard for Trial Use (STU)

*Although the instance selector is not a function, it is closely related to the `select` function in that this statement is
used to convert the input collection into a different output collection. Its sub-expression format is:*

> ```
> «typename» { element : value, element : value, ...  } : «typename»
> ```
> `«typename»` is the name of the type to create (optionally prefixed with a namespace)<br/>
> `element` is the name *(identifier)* of an element of the type being created<br/>
> `value` is any fhirpath expression (including literals) to set to the associated `element`

Creates a new object of type `«typename»` and returns that to the output collection. 
Any elements listed within the parentheses are set as children on the newly created object.

If any of child element's `value` is evaluated to an empty collection, then that element will not be added to the object.

To create an empty object requires the use of `{ : }` to differentiate it from the empty set.

If the input collection contains multiple items, the evaluation of the expression will end and signal an error to the calling environment.
However element selectors can return multiples, provided that the element in that objects structure supports it. 
If not the engine MAY throw an error.

If the input collection is empty, the result is empty.

Some examples of creating data using static instance selectors:


Instance Selectors are usually used to manipulate existing elements into another datatype:


**Note:** Primitive types can be created and set using a special element name `value` if specifically required.
The evaluating fhirpath engine is responsible for performing any type conversions from fhirpath primitives to the target object/type system as required.

### Example(s) from Specification
``` fhirpath
// create a static coding
Coding { system : 'http://example.org/demo', code : 'c1' }

// create an simple identifier, explicitly defining the FHIR namespace
FHIR.Identifier { system : 'http://example.org/demo', value : 'N0001231' }

// create an MRN identifier similar to the one in the patient example at https://hl7.org/fhir/patient-example.json.html
Identifier { 
  type : CodeableConcept { coding: Coding { system: 'http://terminology.hl7.org/CodeSystem/v2-0203', code: 'MR' } },
  system : 'urn:oid:1.2.36.146.595.217.0.1',
  value : '12345',
  period : Period { start: @2001-05-06 }
}

// create an empty Period
Period {:}
```

``` fhirpath
// Convert the patient gender from a code into a coding
Patient.select( 
  Coding { system: 'http://terminology.hl7.org/CodeSystem/v2-0203', code: gender }
)

// Convert a set of concepts from a code system into Codings
CodeSystem.concept.select(Coding { system: %resource.url, code: code, display: display })
```

``` fhirpath
code { value: 'final' }
```

### Coverage
0 tests found for `Instance Selector`.

**Covered:**
- (none)

**Gaps:**
- ❌ Creates new object of specified type
- ❌ Child elements set from value expressions
- ❌ Empty value expression omits element from object
- ❌ Empty object creation with {:} syntax
- ❌ Multiple items in input signals error
- ❌ Element selectors returning multiples for supported elements
- ❌ Empty input returns empty
- ❌ Namespace-prefixed type names (e.g. FHIR.Identifier)
- ❌ Nested instance selectors
- ❌ Primitive type creation with special value element name
- ❌ Usage within select for data transformation

### Test Results

| Test | Aidbox | fhirpath.js-4.8.3 | Firely-5.12.2 | Helios-0.1.32 | Ignixa-0.0.151 | Java-6.7.8 |
|------|------|------|------|------|------|------|

**Summary:** 0/0 (0%) — 0 tests × 6 engines