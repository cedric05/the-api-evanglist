![ORE ID Logo](https://storage.googleapis.com/aikon-assets/Logo_OREIDMark_150.png "ORE ID Logo")

# Getting Started with ORE ID

The easiest way to use ORE ID is the **eos-auth** library<br/>

```
npm install oreid-js --save
```
<br/>

Best place to see how to use eos-auth is to check the [**example apps**](https://github.com/API-market/ore-id-docs/tree/master/examples) inside the [**ore-id-docs**](https://github.com/API-market/ore-id-docs) repo on Github.  Look inside the examples folder in the repo.

<br/>

---


# Simple example

```javascript

import { OreId } from 'oreid-js';

// Create an OreId object to initialize the library
let oreId = new OreId({ appName:"My App", appId, apiKey, ... })

// Start the OAuth flow by setting browser to URL returned by login
let loginResponse = await oreId.login({provider:'facebook'});
window.location = loginResponse.loginUrl

// Get the user's info given a blockchain account
let userInfo = await oreId.getUser(loginResponse.account)

// Start the 

Contact Support:
 Name: No Contact
 Email: email@example.com