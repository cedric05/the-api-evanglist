This is a Zomato RESTful API. It gives you the freshest and most exhaustive restaurant content to power your applications with. It covers 1.5 million restaurants across 10,000 cities globally.This RESTful API searches for restaurants by name, cuisine, or location, a detailed information including ratings, location and cuisine. You can get free and instant access to restaurant information by requesting the [`access-key`](https://developers.zomato.com/api).

# Concepts

The Zomato Web-API utilizes standard HTTP communication and uses REST concepts. Requests and responses contain JSON in the HTTP body. The character encoding is always UTF8. Ensure that your client is capable of handling SSL/TLS HTTP requests.

**API-Key**

An API-Key is a long-lasting secret that represents a unique id. An authorized user can generate a key in Zomato-API for his usage. The user should place this secret in your application settings. Important: Keep this API-Key secret! The application then uses this api-key in each request that is made with our api.

**Example HTTP Header**

    Authorization: Bearer <API-Key or Access Token>
    Accept: application/json
# HTTP Request examples
Requests that don’t have side-effects (and do not change anything) utilize
the `GET` method.

**Read example**

    GET /api/v2.1/categories
    Host: developers.zomato.com
    Authorization: Bearer 5ffb698e3d9a8ea8d51fb8847c216058
    Accept: application/json
# HTTP Response body

Every HTTP response is wrapped by a response body. You should evaluate the success value to check if the operation was successful. If there was a failure an error object will be returned. 

For successful operations we will return the data for read operations. For read operations a corresponding object will be returned if the data is a array of multiple items.

Example HTTP Response with single expected result or single affected entity

    HTTP/2 200 OK
    Content-Type: application/json

    {
        "success": true,
        "data": {
            "id": 1234,
             ...
        }
    }
  
 # Error handling


Ensure to evalute the http status code and react on them accordingly. See table below. If there is an error code that is not 200, there might not be a response body.

However if there is a response body `success` should be `false` and we return a error with additional information what went wrong. 


Contact Support:
 Email: vivekraj3200@gmail.com