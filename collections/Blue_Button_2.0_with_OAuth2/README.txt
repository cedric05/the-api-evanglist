**D R A F T -- D R A F T -- D R A F T -- D R A F T -- D R A F T -- D R A F
    T**

The Centers for Medicare & Medicaid Services (CMS) Blue Button 2.0 API is a
    developer-friendly, standards-based, data API that enables Medicare
    beneficiaries to connect their Medicare claims data to the applications,
    services, and research programs they trust.

Claims information that extends as far back as 2015 can be accessed using the
    HL7 Fast Healthcare interoperability Resource (FHIR) specification.

Fast Healthcare Interoperability Resources (FHIR, pronounced "Fire") defines
    a set of "resources" that represent granular clinical concepts. The
    resources can be managed in isolation, or aggregated into complex documents.
    Technically, FHIR is designed for the web; the resources are based on simple
    XML or JSON structures, with an http-based RESTful protocol where each
    resource has predictable URL. Where possible, open internet standards are
    used for data representation and OAuth2 is used to control access to secure
    FHIR resources..

The **CMS Blue Button 2.0 API** is keyed by a unique Patient id. This id is
    used to apply filter parameters in requests and searches to limit the
    information returned to that of the logged in user.

In FHIR terms the **Medicare Beneficiary** is the "**Patient**." In order to
    be  consistent with the FHIR specification we will use the term Patient
    throughout this documentation to refer to the Medicare Beneficiary.

This is the frist version of our OpenAPI3 definiiton document that attempts to
    import fhir json schema from an external file in the fhir sub-directory.