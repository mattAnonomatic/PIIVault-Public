import requests
from Settings import Settings
from ApiResponse import ApiResponse
from Profile import Profile
from ObjectBuilder import ObjectBuilder

# Initialize the setings
settings = Settings()

# Build the request to get the token
request = requests.post(settings.settings_data["Urls"]["AuthLoginUrl"], json=settings.get_api_auth_data())

# Token request response
response = request.json()

# Object to represent the API response
api_response = ApiResponse()
api_response.ProcessObject(response)

if api_response.success:
    # Build bearer token value
    headers = { "Authorization": "Bearer " + api_response.data["Token"] }

    # Used to mock some data
    builder = ObjectBuilder()

    # Get single poly ID
    poly_id_request = requests.put(
        settings.settings_data["Urls"]["GetPolyIdUrl"],
        json=builder.profile_0.get_json_object(),
        headers=headers)

    # Poly ID request response
    poly_id_response = poly_id_request.json()

    # Poly ID request API response objkect
    poly_api_response = ApiResponse()
    poly_api_response.ProcessObject(poly_id_response)

    if poly_api_response.success:
        print(
            "Resulting poly ID for profile {f_name} {l_name} is {poly_id}".format(
                f_name=builder.profile_0.first_name,
                l_name=builder.profile_0.last_name,
                poly_id=poly_api_response.data))
    else:
        print(poly_api_response.error.status)
        print(poly_api_response.error.message)
else:
    print(api_response.error.status)
    print(api_response.error.message)