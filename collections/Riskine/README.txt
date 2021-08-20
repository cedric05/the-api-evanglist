## Financial Advisory via API  

Welcome to the riskine API! The API is behind every riskine solution. It is the core of riskine's intelligence. We encapsulate different parts of financial advisory into microservices, based on user data, statistical data, external data, realtime data, algorithms, knowledge graphs, and AI. They are combined and fused together to form a bigger picture - the advisory core. The API exposes microservices for clients to consume and interact with this core in bite-sized pieces. This allows us to flexibly support use cases spanning over the entire financial advisory spectrum. ![api overview](img/api-overview.png "API Overview")  

There are two usage patterns for the API: full advisory and calculator-like. In the schematic overview above, this is represented by the riskine Advisory making connections to many microservices and the riskine API accessing one microservice directly.  

 - __Full Advisory:__ This is the main usage pattern. API clients create an advisory session and interact with the API service-by-service. The riskine core patches together data from the user, estimations, calculations, and external services to create a holistic advisory. API clients can then get the enriched data and results, or react to conclusion webhooks as explained in the integration section. _For example, you could start adding a person and their income to the advisory. Pension benefits and associated risks would be automatically estimated in the core based on scenarios. You could get that from the API and render it for the user. With a few more inputs, the risk preference could be set. Afterward, you could answer advisory questions from the API like "Should I start saving money, if yes why and how much is recommended?"_
 - __Calculator-Like:__ For simple use cases, you might want to use services without reference to an advisory. For example, the state benefits service can be accessed directly in a single request if the goal is to just calculate state benefits without reference to a bigger picture. This way, integration is simpler.  

 ## Private Lines and Business Lines 
There are riskine advisory solutions available to advise private persons and business entities. The API is not strictly divided into private lines and business lines microservices, as there is an overlap. However, there are certain services that can be parameterized to deliver either private or business content: `accountType=sme|private`. There are also services that are designed specifically for either of the two.  

 ## Ontology and Data Model 
As core and basis for the data objects in the API, we utilize schemas in the [Open Insurance Ontology](https://github.com/riskine/ontology) which we are maintaining as open-source on GitHub. Building upon its core schemas, we can ensure that data from all subdomains works together and creates a cohesive bigger picture. Find more detailed documentation [here](https://schema.riskine.com/). ![ontology](/img/ontology.png)  

## Countries and Languages  
The riskine API is designed to work the same in all countries, but it differs in content. For example, each country has a unique tax system which in turn influences recommendations. There are two localization dynamics: API content may vary in countries and additionally in different languages. 

 - __Countries__: Country-specific finance logic is embedded in our core for each country that we cover (Germany `de`, Austria `at`, Switzerland `ch`, Spain `es`, Italy `it`, Netherlands `nl`, Japan `jp`). Define the country for your request via the URL parameter `country`.
 - __Languages__: For services with language content as text, the language is controlled via the URL parameter `locale`, for example, `locale=de`, `locale=en`, `locale=es`, ...

Contact Support:
 Email: office@riskine.com