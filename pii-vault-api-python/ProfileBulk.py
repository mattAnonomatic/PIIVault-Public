class ProfileBulk:
    profiles = []

    def __init__(self):
        profiles = []
    
    def get_json_object(self):
        rtn_val = {
            "Profiles": []
            }
        
        profiles_to_add = []
        for profile in self.profiles:
            profiles_to_add.append(profile.get_json_object())
        rtn_val["Profiles"] = profiles_to_add

        return rtn_val