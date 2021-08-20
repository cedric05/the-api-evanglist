The Schema Registry API is used to access the Schema Library within Adobe Experience Platform. The registry provides a user interface and RESTful API from which all available library resources are accessible.

Related documentation:
  * [XDM documentation](http://www.adobe.com/go/xdm-home-en)

Visualize API calls with Postman (a free, third-party software):
  * [Schema Registry API Postman collection on GitHub](https://github.com/adobe/experience-platform-postman-samples/blob/master/apis/experience-platform/Schema%20Registry%20API.postman_collection.json)
  * [Video guide for creating the Postman environment](https://video.tv.adobe.com/v/28832)
  * [Steps for importing environments and collections in Postman](https://learning.getpostman.com/docs/postman/collection_runs/using_environments_in_collection_runs/)

API paths:
  * PLATFORM Gateway URL: https://<span>platform.adobe.io
  * Base path for this API: /data/foundation/schemaregistry
  * Example of a complete path for making a call to "/stats": https://<span>platform.adobe.io/data/foundation/schemaregistry/stats

Required headers:
  * All calls require the headers `Authorization`, `x-gw-ims-org-id`, and `x-api-key`. For more information on how to obtain these values, see the [authentication tutorial](http://www.adobe.com/go/platform-api-authentication-en).
  * All resources in Experience Platform are isolated to specific virtual sandboxes. All requests to Platform APIs require the header `x-sandbox-name` whose value is the all-lowercase name of the sandbox the operation will take place in (for example, "prod"). See the [sandboxes overview](https://docs.adobe.com/content/help/en/experience-platform/sandbox/home.html) for more information.
  * All GET requests to the Schema Registry require an `Accept` header to determine what data is returned by the system. See the [section on Accept headers](https://experienceleague.adobe.com/docs/experience-platform/xdm/api/getting-started.html?lang=en#accept) in the Schema Registry developer guide for more information.
  * All requests with a payload in the request body (such as POST, PUT, and PATCH calls) must include the header `Content-Type` with a value of `application/json`.