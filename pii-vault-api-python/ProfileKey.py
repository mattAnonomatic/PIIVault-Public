class ProfileKey:
    key_type = ""
    key_owner = ""
    key_number = ""

    def __init__(self, key_type = "", key_owner = "", key_number = ""):
        self.key_type = key_type
        self.key_owner = key_owner
        self.key_number = key_number

    def get_json_object(self):
        return { 'KeyType': self.key_type, 'KeyOwner': self.key_owner, 'KeyValue': self.key_number }