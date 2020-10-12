import requests
from Settings import Settings
from ApiResponse import ApiResponse
from Profile import Profile
from ProfileBulk import ProfileBulk
from ObjectBuilder import ObjectBuilder

# Initialize the setings
settings = Settings()

# Build the request to get the token
request = requests.post(settings.settings_data["Urls"]["AuthLoginUrl"], json=settings.get_api_auth_data())

# Token request response
response = request.json()

# Object to represent the API response
api_response = ApiResponse()
api_response.process_object(response)

if api_response.success:
    # Build bearer token value
    headers = { "Authorization": "Bearer " + api_response.data["Token"] }

    # Used to mock some data
    builder = ObjectBuilder()

    # Bulk object
    bulk = ProfileBulk()
    bulk.profiles.append(builder.profile_0)
    bulk.profiles.append(builder.profile_1)
    bulk.profiles.append(builder.profile_2)

    # Get bulk poly ID
    poly_id_request = requests.put(
        settings.settings_data["Urls"]["GetPolyIdBulk"],
        json=bulk.get_json_object(),
        headers=headers)

    # Bulk ID response
    poly_id_response = poly_id_request.json()

    # Bulk ID response API object
    poly_api_response = ApiResponse()
    poly_api_response.process_object(poly_id_response)

    if poly_api_response.success:
        response_array = poly_api_response.data["Responses"]

        for poly_id in response_array:
            print(
                "Poly ID for profile source key {source_key} at index {index} is {poly_id}".format(
                    source_key=poly_id["SourceSystemKey"],
                    index=poly_id["Index"],
                    poly_id=poly_id["PolyId"]))
    else:
        print(poly_api_response.error.status)
        print(poly_api_response.error.message)
else:
    print(api_response.error.status)
    print(api_response.error.message)