The Recurring APIs allow you to manage and remove your tokens or saved payment details. Tokens should be created with validation during a payment request.

For more information, refer to our [Tokenization documentation](https://docs.adyen.com/checkout/tokenization).
## Authentication
To connect to the Recurring API, you must use your basic authentication credentials. For this, create your web service user, as described in [How to get the WS user password](https://docs.adyen.com/user-management/how-to-get-the-web-service-ws-user-password). Then use its credentials to authenticate your request, for example:

```
curl
-U "ws@Company.YourCompany":"YourWsPassword" \
-H "Content-Type: application/json" \
...
```
Note that when going live, you need to generate new web service user credentials to access the [live endpoints](https://docs.adyen.com/development-resources/live-endpoints).

## Versioning
Recurring API supports versioning of its endpoints through a version suffix in the endpoint URL

Contact Support:
 Name: No Contact
 Email: email@example.com