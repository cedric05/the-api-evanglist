## Authorization

Step by step instruction how to use Watson Machine Learning service
can be found [here](https://datascience.ibm.com/docs/content/analyze-data/ml-overview.html?context=analytics)

### IBM Watson Machine Learning Credentials

To start working with API one needs to generate an `access token` using the `username` and `password`
available on the Service Credentials tab of the IBM Watson Machine Learning service instance or also available in the VCAP environment variable.

Example of the Service Credentials:

```json
{
    "url": "https://ibm-watson-ml.mybluemix.net",
    "username": "c1ef4b80-2ee2-458e-ab92-e9ca97ec657d",
    "password": "030528d4-5a3e-4d4c-9258-5d553513be6f",
    "instance_id": "a751c209-954e-dc32-b441-ad56ce7a9f40"
}
```

Example of obtaining `access token` from Token Endpoint using HTTP Basic Auth (for details please refer to Token section below):

`
curl --basic --user username:password https://ibm-watson-ml.mybluemix.net/v3/identity/token
`

The obtai

Contact Support:
 Name: No Contact
 Email: email@example.com