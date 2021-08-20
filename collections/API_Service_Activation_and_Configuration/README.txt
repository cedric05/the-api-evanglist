## TMF API Reference: TMF640 - Service Activation and Configuration

 Version 4.0 

Service Activation and Configuration API goal is to provide the ability to activate and configure Service. This API features Monitor pattern allowing to manage service configuration/activation asynchronous request (server side will provide monitor as POST/PATCH response) 

### TMF640 performs the following Operations on service resource :
- Retrieve a service or a collection of services depending on filter criteria
- Partial update of an service
- Create a service (including default values and creation rules)
- Delete a service (for administration purposes)
- Manage notification of events

### Monitor Resource

Monitor resource is used to track and log activation and/or configuration request

### TMF640 provides following operation on Monitor resource:

- Retrieval of a monitor or a collection of monitor

Copyright © TM Forum 2019; All Rights Reserved