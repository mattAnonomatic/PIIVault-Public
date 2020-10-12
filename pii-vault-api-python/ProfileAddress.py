class ProfileAddress:
    address_type = ""
    street_address_1 = ""
    street_address_2 = ""
    city = ""
    state = ""
    address_zip = ""

    def __init__(self, address_type = "", street_address_1 = "", street_address_2 = "", city = "", state = "", address_zip = ""):
        self.address_type = address_type
        self.street_address_1 = street_address_1
        self.street_address_2 = street_address_2
        self.city = city
        self.state = state
        self.address_zip = address_zip

    def get_json_object(self):
        return {
            'AddressType' : self.address_type,
            'StreetAddress1': self.street_address_1,
            'StreetAddress2': self.street_address_2,
            'City': self.city,
            'State': self.state,
            'Zip': self.address_zip
        }