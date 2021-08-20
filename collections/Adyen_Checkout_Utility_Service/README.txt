A web service containing utility functions available for merchants integrating with Checkout APIs.
## Authentication
Each request to the Checkout Utility API must be signed with an API key. For this, obtain an API Key from your Customer Area, as described in [How to get the Checkout API key](https://docs.adyen.com/developers/user-management/how-to-get-the-checkout-api-key). Then set this key to the `X-API-Key` header value, for example:

```
curl
-H "Content-Type: application/json" \
-H "X-API-Key: Your_Checkout_API_key" \
...
```
Note that when going live, you need to generate a new API Key to access the [live endpoints](https://docs.adyen.com/developers/api-reference/live-endpoints).

## Versioning
Checkout API supports versioning of its endpoints through a version suffix in the endpoint URL. This suffix has the following format: "vXX", where XX is the version number.

For example:
```
https://checkout-test.adyen.com/v1/originKeys
```

Contact Support:
 Name: No Contact
 Email: email@example.com