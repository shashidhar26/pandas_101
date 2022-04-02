# API design in python

## APIs

API is a set of definitions and protocols for building and integrating application software, sometimes referred to as a contract between an information provider and an information user—establishing the content required from the consumer(the call) and the content required by the producer (the response). Read more about APIs [here](https://www.redhat.com/en/topics/api/what-are-application-programming-interfaces). There could be APIs for private use, limited use and public use. While APIs are made to be used beyond private use, security constraints need to be addressed like who can access it and how. Remote APIs are those which interact over a communication network (usually web APIs). While all web APIs are remote APIs, the vice-versa need not be true (there could be other remote APIs that do not need to be web APIs). 

Implementing remote APIs would mean the information users and information providers need to agree on some standards for how they can be used. Usually, the request messages for the API are http based. And the responses could be a XML or JSON file. These formats are usually chosen because many apps can easily manipulate the received information easily to be presented in a way that is desired by the user. 

## Remote API standards
*NB: The information here has been copied from [here](https://www.redhat.com/en/topics/api/what-are-application-programming-interfaces#soap-vs-rest) - due credit to the original authors. It is only for my quick understanding.*

As web APIs have spread, a protocol specification was developed to help standardize information exchange: Simple Object Access Protocol, more casually known as SOAP. APIs designed with SOAP use XML for their message format and receive requests through HTTP or SMTP. SOAP makes it easier for apps running in different environments or written in different languages to share information

Another specification is Representational State Transfer (REST). Web APIs that adhere to the REST architectural constraints are called RESTful APIs. REST differs from SOAP in a fundamental way: SOAP is a protocol, whereas REST is an architectural style. This means that there’s no official standard for RESTful web APIs. As defined in Roy Fielding’s dissertation “Architectural Styles and the Design of Network-based Software Architectures,” APIs are RESTful as long as they comply with the 6 guiding constraints of a RESTful system:

- Client-server architecture: REST architecture is composed of clients, servers, and resources, and it handles requests through HTTP.
- Statelessness: No client content is stored on the server between requests. Information about the session state is, instead, held with the client.
- Cacheability: Caching can eliminate the need for some client-server interactions.
- Layered system: Client-server interactions can be mediated by additional layers. These layers could offer additional features like load balancing, shared caches, or security.
- Code on demand (optional): Servers can extend the functionality of a client by transferring executable code.
- Uniform interface: This constraint is core to the design of RESTful APIs and includes 4 facets:
  - Resource identification in requests: Resources are identified in requests and are separate from the representations returned to the client.
  - Resource manipulation through representations: Clients receive files that represent resources. These representations must have enough information to allow modification or deletion.
  - Self-descriptive messages: Each message returned to a client contains enough information to describe how the client should process the information.
  - Hypermedia as the engine of application state: After accessing a resource, the REST client should be able to discover through hyperlinks all other actions that are currently available.

In recent years, the OpenAPI specification has emerged as a common standard for defining REST APIs. OpenAPI establishes a language-agnostic way for developers to build REST API interfaces so that users can understand them with minimal guesswork. 

Read more on architecture frameworks [here](https://www.redhat.com/en/topics/api/what-are-application-programming-interfaces#soas-vs-microservices)