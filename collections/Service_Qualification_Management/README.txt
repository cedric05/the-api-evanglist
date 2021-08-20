## TMF API Reference: TMF645 - Service Qualification

 Version 4.0 

 Service Qualification API is one of Pre-Ordering Management API Family. Service Qualification API goal is to provide service technical eligibility. Since v4 the API is split in 2 resources to distinguish specific service qualification request to be performed on a described configurated service (or a list of configured services) from a retrieval of services eligible for a given context. The API allows to manage synchronous as asynchronous eligibility response (eligibility provided in POST response or later with an id and state provided ).  

### CheckServiceQualification Resource 

 This resource is use to check a configured service eligibility (or a list of service). A qualification result is provided in response. Requested could ask for unavailability reason and/or for alternate proposal 

### TMF645 performs the following operations on the check service qualification resource :
- Retrieve a checkServiceQualification or a collection of checkServiceQualification depending on filter criteria
- Partial update of a checkServiceQualification 
- Create a checkServiceQualification (including default values and creation rules)
- Delete a checkServiceQualification (for administration purposes)
- Manage notification on checkServiceQualification

### Query Service Qualification resource

 Query Service Qualification is used to retrieve a list of service eligible in a given request provided by requester (via searchCriteria).

### TMF645 performs the following operations on a query service qualification resource:

- Retrieval a queryServiceQualification or a list of queryServiceQualification
- Partial update of a queryServiceQualification
- Creation of a queryServiceQualification
- Deletion of a queryServiceQualification
- Notification on queryServiceQualification

 Copyright (c) TM Forum 2019. All Rights Reserved