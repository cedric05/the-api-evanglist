The MarketPay Notification Configuration API provides endpoints for configuration a subscription to a marketplace's MarketPay-related notifications. Notifications are sent upon the occurrence of certain events (such as a KYC check completion or a payout completion), and the subscription to these notifications dictates to where they are sent.

For further information on MarketPay notifications, please visit the [MarketPay documentation](https://docs.adyen.com/marketpay).
## Authentication
To connect to the MarketPay API, you must use basic authentication credentials of your web service user. If you don't have one, please contact the [Adyen Support Team](https://support.adyen.com/hc/en-us/requests/new). Then use its credentials to authenticate your request, for example:

```
curl
-U "ws@MarketPlace.YourMarketPlace":"YourWsPassword" \
-H "Content-Type: application/json" \
...
```
Note that when going live, you need to generate new web service user credentials to access the [live endpoints

Contact Support:
 Name: No Contact
 Email: email@example.com