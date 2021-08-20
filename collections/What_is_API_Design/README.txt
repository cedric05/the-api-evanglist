API design is the architectural patterns and details used to describe the surface area of each individual. The design of an API describes what an API delivers as a set of resources or capabilities, providing a functional representation of an interface that can be used in applications and integrations. 

## Protocols
Protocols play a significant role in defining what is API design, and how it is applied to each API, including but not limited to these protocols:

- **HTTP** - Utilizing the Hypertext Transfer Protocol (HTTP) for a transport and design constraint.
- **TCP** - Utilizing the Transmission Control Protocol (TCP) for a transport and design constraint.
- **MQTT** - Utilizing the Message Queuing Telemetry Transport (MQTT) for a transport and design constraint.

## Patterns
Overlapping with protocols, API design is often defined by a handful of leading patterns that define the functionality of each API being delivered:

- **REST** - Applying the Representational state transfer (REST) pattern to the design of each API being delivered.
- **Hypermedia** - Reflecting the functionality of the web by introducing hypermedia design patterns to an API being delivered.
- **GraphQL** - Adopting a more data centered approach the design of an API by going with a GraphQL design pattern.

## Specifications
Open source API specifications are often used to guide, define, and validate API design, helping provide a human and machine readable definition for each API. 

- **[OpenAPI](https://api-evangelist.postman.co/workspace/What-Is---API~bc3b587a-4a38-4276-a234-c39f3b677d9b/documentation/35240-1013ffce-f79d-40d0-9074-87f104aa26b1)** - Used for describing HTTP APIs, webhooks, and the models used as part of requests and responses.
- **[AsyncAPI](https://api-evangelist.postman.co/workspace/What-Is---API~bc3b587a-4a38-4276-a234-c39f3b677d9b/documentation/35240-1f941c2c-fd36-47d1-91df-b5a5cf1d3c4e)** - Used for describing HTTP, TCP, MQTT, AMQP, and the channels as well as models used as part of events and messages.
- **[JSON Schema](https://api-evangelist.postman.co/workspace/What-Is---API~bc3b587a-4a38-4276-a234-c39f3b677d9b/documentation/35240-d37bf459-77e8-4fd1-8916-95ca2b3a8b41)** - Used to define the models that are used across OpenAPI and AsyncAPI, helping define the payload of each API.

## Applying
Each protocol and pattern will bring its set of considerations when it comes to describing the surface area of your API, and which specification or standard you apply as part of the API design process. Much of the API design guidance on the web is HTTP or REST API centered, while this guidance intends to support design across multiple protocols, patterns, and using relevant specifications.