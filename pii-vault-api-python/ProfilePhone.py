class ProfilePhone:
    phone_type = ""
    phone_owner = ""
    phone_number = ""

    def __init__(self, phone_type = "", phone_owner = "", phone_number = ""):
        self.phone_type = phone_type
        self.phone_owner = phone_owner
        self.phone_number = phone_number

    def get_json_object(self):
        return { 'PhoneType': self.phone_type, 'PhoneOwner': self.phone_owner, 'PhoneNumber': self.phone_number }