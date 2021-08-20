The MarketPay Funding API provides endpoints for managing the funds in MarketPay accounts. These management operations include actions such as the transfer of funds from one account to another, the payout of funds to an account holder, and the retrieval of balances in an account.

For further information on MarketPay fund management, please visit the [MarketPay documentation](https://docs.adyen.com/marketpay).
## Authentication
To connect to the MarketPay API, you must use basic authentication credentials of your web service user. If you don't have one, please contact the [Adyen Support Team](https://support.adyen.com/hc/en-us/requests/new). Then use its credentials to authenticate your request, for example:

```
curl
-U "ws@MarketPlace.YourMarketPlace":"YourWsPassword" \
-H "Content-Type: application/json" \
...
```
Note that when going live, you need to generate new web service user credentials to access the [live endpoints](https://docs.adyen.com/development-resources/live-endpoints

Contact Support:
 Name: No Contact
 Email: email@example.com