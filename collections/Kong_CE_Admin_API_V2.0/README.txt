<img src="https://2tjosk2rxzc21medji3nfn1g-wpengine.netdna-ssl.com/wp-content/themes/konghq/assets/img/gradient-logo.svg" alt="Kong Community Edition Admin API" title="Kong Community Edition Admin API" />
<br>

This Postman Collection refers to the [Kong Community Edition Admin API](https://docs.konghq.com/2.0.x/admin-api/) for running Kong configured with a database (Postgres or Cassandra). For using the Admin API for Kong in DB-less mode, please refer to the Admin API for DB-less Mode [konghq](https://docs.konghq.com/2.0.x/db-less-admin-api/).<br>

**Disclaimer**: Collection not hardened by development AToW [George Jeffcock](https://www.linkedin.com/in/georgejeffcock/)

Kong comes with an internal RESTful Admin API for administration purposes. Requests to the Admin API can be sent to any node in the cluster, and Kong will keep the configuration consistent across all nodes.

* **8001** is the default port on which the Admin API listens.
* **8444** is the default port for HTTPS traffic to the Admin API.

This API is designed for internal use and provides full control over Kong, so care should be taken when setting up Kong environments to avoid undue public exposure of this API. See this [document](https://docs.konghq.com/2.0.x/secure-admin-api/) for a discussion of methods to secure the Admin API.

# Supported Content Types
* The Admin API accepts 2 content types on every endpoint:
* application/x-www-form-urlencoded
 * Simple enough for basic request bodies, you will probably use it most of the time. Note that when sending nested values, Kong expects nested objects to be referenced with dotted keys
 * Example: config.limit=10&config.period=seconds
* application/json
 * Handy for complex bodies (ex: complex plugin configuration), in that case simply send a JSON representation of the data you want to send.
 * Example:
 {"config": {"limit": 10, "period": "seconds"}}