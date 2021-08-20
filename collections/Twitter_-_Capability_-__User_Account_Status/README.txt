This is a Postman collection for looking up the status of a list of Twitter handles, verifying the state of each individual Twitter user. Providing only the basic information you need to validate one or many different Twitter accounts.

Before you can use this API collection you will have to download the Postman applications, then setup your own Twitter application at: https://developer.twitter.com/en/apps so you can make calls to the Twitter API--do not worry, it is painless, and something even a non-developer can do.

![alt text](https://kinlane-productions.s3.amazonaws.com/postman-tutorials/twitter-status-lookup/twitter-application.png "New Application")

When filling out the form, all you need is to give your app a name, description, website URL, and tell them how it will be used. You can ignore the rest of the fields. Once the application is added you can obtain your access tokens by clicking on the keys and tokens tab.

![alt text](https://kinlane-productions.s3.amazonaws.com/postman-tutorials/twitter-status-lookup/twitter-keys-and-tokens.jpg "Keys and Tokens")

The first time you create your application you will have regenerate your access token and access token secret, and then you will need all four tokens to authenticate (Don't worry those aren't my real tokens). Once you have your own tokens, go back to your Postman application and click on the Twitter Lookup Postman collection, and edit its details.

![alt text](https://kinlane-productions.s3.amazonaws.com/postman-tutorials/twitter-status-lookup/edit-collection.png "Edit Collection")

Once the edit window pops up select the Authorization tab, then select to use OAuth 1.0 and add your auth data to request headers from the dropdown boxes, then add your own {{consumer_key}}, {{consumer_secret}}, {{access_token}}, and {{token_secret}} from the application you setup. 

![alt text](https://kinlane-productions.s3.amazonaws.com/postman-tutorials/twitter-status-lookup/edit-collection-authorization.png "Edit Collection Authorization")

Once you have entered all your tokens you should be able to make a Twitter lookup API request, passing in one or many Twitter handles for the users you'd like to validate the status for--then hitting the send button for the request in Postman.

![alt text](https://kinlane-productions.s3.amazonaws.com/postman-tutorials/twitter-status-lookup/make-response.png "Make Request")

Once you hit send on the request, with the proper authorization, you will see a full API response from the Twitter API in a JSON format, providing you with all the detail on each user included as part of the API request.

![alt text](https://kinlane-productions.s3.amazonaws.com/postman-tutorials/twitter-status-lookup/see-response.png "See Response")

Each Twitter account response is pretty verbose, and requires you to wade through a lot of JSON to find what you are looking for. To help make more accessible to non-developers I made a visualizer response that only shows the relevant information to the status of each account. You can see this by clicking on the visualizer tab for the Postman response.

![alt text](https://kinlane-productions.s3.amazonaws.com/postman-tutorials/twitter-status-lookup/see-visual-response.png "Visualize Response")

This Postman collection should allow anyone (developer or non-developer) to work with the Twitter API and make lookups via the Twitter API to validate any Twitter user account. If you have any questions you an ping me on Twitter at [@apievangelist ](https://twitter.com/apievangelist), or via [info@apievangelist.com](mailto:info@apievangelist.com).

You can view the basic documentation for this endpoint below, and run using the Run in Postman button in the top-right corner of this documentation. You can also find code samples in a variety of programming languages using the dropdown just below the Run in Postman button, helping you quickly integrate this API capability into your application.