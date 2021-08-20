This is a collection for deploying an API from Postman to AWS API Gateway, with an AWS RDS Aurora backend that is powered using AWS Lambdas. It was distilled down from a larger API life cycle collection I am building but I wanted to pull out and let it stand on its own to show how Postman can be used to deploy API infrastructure. It has 21 (with two to test) steps that can be run independently or collectively using a Postman runner.

All of this could easily be distilled down into a single Postman request, but it can be valuable to see each step that is needed to actually deploy an API, then packaging up as a repeatable process. It has already been distilled down from multiple API calls to Postman, AWS Lambda, AWS RDS, and AWS API Gatway. So, I am just pausing to make sure of the workflow I want for deploying an API to a development or production environment.

This collection depends on this environment to authenticate with the Postman API, AWS Lambda API, AWS RDS API, and AWS API Gateway API, as well as to store data used in the deployment process. You can import this environment into your Postman, enter your keys and tokens into the environment, and it should work as long as your AWS IAM is configured properly.

There is a significant more work that needs to be done validating the OpenAPI definition before it enters this process, but I am building that as a separate governance collection that can be run independently of each API deployment workflow.

If you need an OpenAPI to test out, I have ran this collection against the following APIs so far:

- [Products](https://github.com/union-fashion/products/blob/master/products-v1.json)

I will keep working on stablizing and streamling this collection, and publishing any changes as part of this documentation. Using these docs as a complete set of instructions for how to use this collecton for deploying APIs.