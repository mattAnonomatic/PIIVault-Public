# Introduction

This folder contains the Python environment that consumes the PII Vault API. The primary points of entry for this app need to be run as:

```
py GetPolyId.py
py GetPolyIdBulk.py
```

These commands consume a different API end point. Each one of these files starts by requesting a token to be used as an authorization header. This block of code will look like:

```
import requests
from Settings import Settings
from ApiResponse import ApiResponse

# Initialize the setings
settings = Settings()

# Build the request to get the token
request = requests.post(settings.settings_data["Urls"]["AuthLoginUrl"], json=settings.get_api_auth_data())

# Token request response
response = request.json()

# Object to represent the API response
api_response = ApiResponse()
api_response.process_object(response)
```

After this is done, all that is needed for each other request is to add this in the header:

```
headers = { "Authorization": "Bearer " + api_response.data["Token"] }
```

# Setup

It is very important to replace the values in the `settings.json` file with your account ID and API key. Without this, these requests will result in a an HTTP error.

# External Packages

This repo comes with a `requirements.txt` file that has the necessary PIP installs. PIP was used in making this repository but a developer is free to use another package manager should they feel comfortable with it.

## requests

`pip install requests`

Standard Python library used to make HTTP requests.

# Explanation of different files and classes in this repo

Some classes were written in this repo to help out with the consumption of the API. It needs to be understood this was written by a C# developer who tried to keep up with object orientation programming.

## ApiError.py

Each API call comes with an `Error` object that this class will embody. A standard message and status to tell the user what went wrong.

## ApiResponse.py

All API calls have some standard fields attached to them, an error object which is null is there are no errors, a success boolean, and a data field that can be information specific to an API response.

## Profile.py

Representation of a profile object that is sent to the API. All classes that fall into this category have a method called `get_json_object` which returns the object in a Python dict that is sent as JSON to the API. The `Profile` object also contains arrays or other classes.

## ProfileBulk.py

Contains multiple profiles, will be used in the bulk call.

## ObjectBuilder.py

Creates some mock instances to be used in the following code examples.
