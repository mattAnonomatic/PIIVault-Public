# Introduction

This folder contains the NodeJS environment that consumes the PII Vault API. The primary points of entry for this app need to be run as:

```
node index.js
```

After this has been run, a browser can be open to navigate to the following URLS:

- localhost:3137/
- localhost:3137/get-poly-id
- localhost:3137/get-poly-id-bulk

These respectively call the request to get the token, call `GetPolyId` and `GetPolyIdBulk`. A base command to get the token looks like this:

```
static RequestApiToken = async () => {
    let tokenRequest = await axios.post("https://api.piivault.com/api/auth/login", {
        AccountId: process.env["ACCOUNT_ID"],
        ApiKey: process.env["API_KEY"],
    });

    let tokenResponse = tokenRequest.data;

    if (tokenResponse.Success) {
      return tokenResponse.Data.Token;
    } else {
      console.log(`Error Status = ${tokenResponse.Error.Status}\n`);
      console.log(`Error Message = ${tokenResponse.Error.Message}\n`);
      return "";
    }
  };
```

After this is done, all that is needed for each other request is to add this in the header:

```
{ headers: { Authorization: `Bearer ${token}` } }
```

# Setup

It is very important to replace the values in the `.env` file with your account ID and API key. Without this, these requests will result in a an HTTP error.

This project was started using the command `npm init`.

# External Packages

As with any Node environment, some npm packages were used to put this together. Information can be found in the `package.json` file. But the install commands run looks like this:

```
npm install express twilio --save
npm install dotenv --save
npm install axios --save
```

## Express and Twilio

Standard node framework to setup the server each time the project is run.

## dotenv

Used to set and read environment variables

## axios

Promise based HTTP requests library used to call the API within this project.

# Explanation of different files and classes in this repo

Some classes were written in this repo to help out with the consumption of the API. It needs to be understood this was written by a C# developer who tried to keep up with object orientation programming.

## utility.js

Base static class to run redundant code that needs to be called more than once.

### RequestApiToken

Returns the token we need for other API calls.

### GetSinglePerson

Gets a single Profile JSON object to be sent with `GetPolyId`.

### GetPeople

Gets a bulk load of profiles to be sent with `GetPolyIdBulk`.
