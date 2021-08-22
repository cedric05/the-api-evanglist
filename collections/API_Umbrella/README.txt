The admin API is accessible via `/api-umbrella/v1`. In order to access this API, you must pass:

- Your API key via one of the [supported methods](http://nrel.github.io/api-umbrella/docs/api-keys/).
- **AND** an admin token via the `X-Admin-Auth-Token` header.

To find the admin auth token for your admin account, login the web admin tool, and choose "My Account" under the top right gear menu. On that page, you should see your "Admin API Token" listed. Use this in conjunction with your normal API key to make requests to the admin APIs:

```http
X-Api-Key: YOUR_API_KEY_HERE
X-Admin-Auth-Token: YOUR_ADMIN_TOKEN_HERE
```

Contact Support:
 Name: No Contact
 Email: email@example.com