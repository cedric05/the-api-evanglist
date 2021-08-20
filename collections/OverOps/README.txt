Main OverOps API.
The REST API layer enables OverOps admins and users to perform and automate all actions
provided by the OverOps UI available at https://app.overops.com (or On-premises equivalent URL) via a platform independent programmatic interface.
A wrapper Java client API library that leverages these APIs for convenience by
Java and Scala developers is available at https://github.com/takipi/api-client and on Maven Central.

All calls must be authenticated using one of the following methods:
  1. Using `x-api-key` header (To generate the token, go to `Settings` --> `Account Settings` in the OverOps App). This is the recommended method.
  2. Using Basic auth with `username:password` combo.


Contact Support:
 Email: hello@overops.com