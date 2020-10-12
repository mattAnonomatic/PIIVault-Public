import json

class Settings:
    file_name = "settings.json"
    settings_data = {}

    def __init__(self):
        with open(self.file_name) as f:
            self.settings_data = json.load(f)

    def get_api_auth_data(self):
        return {
            'AccountId': self.settings_data["AccountId"],
            'ApiKey' : self.settings_data["ApiKey"]
            }