The Postman API allows you to programmatically access data stored in Postman account with ease.

The easiest way to get started with the API is to click the [_Run in Postman_](https://www.getpostman.com/docs/run_button_ux) button present at the top of the documentation page and use the Postman App to send requests.


# Overview

1. You need a valid <a href="#authentication">API Key</a> to send requests to the API endpoints. You can get your key from the [integrations dashboard](https://go.postman.co/integrations/services/pm_pro_api).

1. The API has an access <a href="#rate-limits">rate limit</a> applied to it.

1. The Postman API will only respond to secured communication done over HTTPS. HTTP requests will be sent a `301` redirect to corresponding HTTPS resources.

1. Response to every request is sent in [JSON format](https://en.wikipedia.org/wiki/JSON). In case the API request results in an error, it is represented by an `"error": {}` key in the JSON response.

1. The request method

Contact Support:
 Name: No Contact
 Email: email@example.com