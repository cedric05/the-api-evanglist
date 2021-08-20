# data.world in a nutshell

data.world is a productive, secure platform for modern data teamwork.

We bring together your data practitioners, subject matter experts, and other stakeholders by removing costly barriers to data discovery, comprehension, integration, and sharing. 

Everything your team needs to quickly understand and use data stays with it. 

Social features and integrations encourage collaborators to ask and answer questions, share discoveries, and coordinate closely while still using their preferred tools.

Our focus on interoperability helps you enhance your own data with data from any source, including our vast and growing library of free public datasets. 

Sophisticated permissions, auditing features, and more make it easy to manage who views your data and what they do with it.

# Conventions

## Authentication

All data.world API calls require an API token. 

OAuth2 is the preferred and most secure method for authenticating users of your data.world applications. Visit our [oauth documentation](https://apidocs.data.world/toolkit/oauth) for additional information. Alternatively, you can obtain a token for _personal use or testing_ by navigating to your profile settings, under the Advanced tab ([https://data.world/settings/advanced](https://data.world/settings/advanced)).

Authentication must be provided in API requests via the `Authorization` header. For example, for a user whose API token is `my_api_token`, the request header should be `Authorization: Bearer my_api_token` (note the `Bearer` prefix).

## Content type  
By default, `application/json` is the content type used in request and response bodies. Exceptions are noted in respective endpoint documentation.

## HTTPS only  
Our APIs can only be accessed via HTTPS.

# Interested in building data.world apps?

Check out our [developer portal](https://apidocs.data.world) for tips on how to get started, tutorials, and to interact with the API endpoints right within your browser.

Contact Support:
 Name: data.world
 Email: help@data.world