class Profile:
    index = 0
    source_system_key = ""
    first_name = ""
    middle_name = ""
    last_name = ""
    date_of_birth = ""
    gender = ""
    is_forgotten = False
    emails = []
    phones = []
    addresses = []
    keys = []

    def __init__(self):
        self.index = 0

    def get_json_object(self):
        rtn_val = {
            'Index': self.index,
            'SourceSystemKey': self.source_system_key,
            'FirstName': self.first_name,
            'MiddleName': self.middle_name,
            'LastName': self.last_name,
            'DateOfBirth': self.date_of_birth,
            'Gender': self.gender,
            'IsForgotten': 1 if self.is_forgotten else 0,
            'Emails': [],
            'Phones': [],
            'Addresses': [],
            'Keys': []
            }

        # Fill in emails
        profile_emails = []
        for email in self.emails:
            profile_emails.append(email.get_json_object())
        rtn_val["Emails"] = profile_emails

        # Fill in phones
        profile_phones = []
        for phone in self.phones:
            profile_phones.append(phone.get_json_object())
        rtn_val["Phones"] = profile_phones

        # Fill in keys
        profile_keys = []
        for key in self.keys:
            profile_keys.append(key.get_json_object())
        rtn_val["Keys"] = profile_keys

        # Fill in addresses
        profile_addrs = []
        for addr in self.addresses:
            profile_addrs.append(addr.get_json_object())
        rtn_val["Addresses"] = profile_addrs

        return rtn_val