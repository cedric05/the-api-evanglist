# Scalyr API
You can use the Scalyr API to send and retrieve log data directly from Scalyr servers, as well as manage configuration files. It is usually most convenient to use the [Scalyr Agent](https://www.scalyr.com/help/scalyr-agent) to send log files, and to view logs on the web site. We also provide a [Java client library](https://www.scalyr.com/help/java-api) and a [command-line](https://www.scalyr.com/help/command-line) tool. But if you'd like to talk directly to the Scalyr servers from a language other than Java, you've come to the right place.

## API FORMAT
(Note: this section does not apply to the uploadLogs API, which uses simple text bodies.)

To invoke a Scalyr API method, send an HTTPS POST to the URL for the method you wish to invoke. The request should have Content-Type "application/json", and the body should be a JSON-formatted, UTF-8 encoded string. The response is also a JSON-formatted, UTF-8 encoded string.

The query, numericQuery, facetQuery, and timeseriesQuery methods can also be invoked via GET, passing arguments in standard URL format. (Remember to encode spaces as %20.) When invoked in this fashion, the response will still be JSON.

The response will always include a "status" property, indicating whether the operation succeeded or failed. Status codes are hierarchical, with slash-delimited components. For example, "error/client" and "error/server" both indicate that the operation failed, but one indicates that the problem was the client's fault and the other the server's fault. New status values may be added in the future, but they will generally extend (refine) existing values. So when checking the status value, always be prepared for extra text — check startsWith() instead of equals(). Each method may list one or more responses specific to that method. In addition, the following responses are possible for all methods:

  1. Response if the request is somehow incorrect ("your fault"):

      ```
      {
        "status":  "error/client",
        "message": "a human-readable message"
      }
      ```

  2. Response if the server experiences an internal error while processing the request ("our fault"):

      ```
      {
        "status":  "error/server",
        "message": "a human-readable message"
      }
      ```

  If the server is overloaded, or for some other reason is temporarily unable to process the request, it will return a status of "error/server/backoff". When this status is returned, you may wish to retry the request after a short delay. You should also retry after a delay in the case of server errors (5xx status code), 429 status code ("Too Many Requests"), or a request timeout.

Note that new status values, in particular new error statuses, may be added in the future. Please treat any unexpected status value like "error".

When an error is returned, the HTTP status code will contain an appropriate non-200 value. Some HTTP client libraries (such as the standard Java library) don't provide access to the response body when the status code is not 200, making it difficult to get a detailed error message. If you provide an "errorStatus" request header with value "always200", the Scalyr server will return a 200 status code even for errors. In this mode, to detect errors, check the JSON response body for a status string beginning with "error". Note that some low-level errors may still yield a non-200 status code.


Contact Support:
 Name: Scalyr
 Email: contact@scalyr.com