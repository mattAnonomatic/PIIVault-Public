from Profile import Profile
from ProfileEmail import ProfileEmail
from ProfilePhone import ProfilePhone
from ProfileKey import ProfileKey
from ProfileAddress import ProfileAddress

class ObjectBuilder:
    profile_0 = Profile()
    profile_1 = Profile()
    profile_2 = Profile()
    
    def __init__(self):
        email_0 = ProfileEmail("rick.sanchez@all.com")
        phone_0 = ProfilePhone("Mobile", "SSA", "123-456-7890")
        key_0 = ProfileKey("SSN", "SSA", "123-45-6789")
        address_0 = ProfileAddress("Home", "123 Anywhere Lane", "", "Anytown USA", "NY", "10001")

        email_1 = ProfileEmail("morty.smith@all.com")
        phone_1 = ProfilePhone("Landline", "SSA", "987-605-4321")
        key_1 = ProfileKey("SSN", "SSA", "987-65-4321")
        address_1 = ProfileAddress("Home", "456 Everywhere Circle", "", "Anytown USA", "NY", "10001")

        email_2 = ProfileEmail("lars.peters@all.com")
        phone_2 = ProfilePhone("Jupiter", "SSA", "+31 902377345")
        key_2 = ProfileKey("SSN", "SSA", "826-01-1495")
        address_2 = ProfileAddress("HQ", "789 Nowhere Ave", "", "Anytown USA", "NY", "10001")

        # Profile Index 0
        self.profile_0 = Profile()
        self.profile_0.index = 0
        self.profile_0.source_system_key = "12345"
        self.profile_0.first_name = "Rick"
        self.profile_0.last_name = "Sanchez"
        self.profile_0.date_of_birth = "1980-10-10T01:00:00.000Z"
        self.profile_0.gender = "M"
        self.profile_0.emails = [email_0]
        self.profile_0.phones = [phone_0]
        self.profile_0.keys = [key_0]
        self.profile_0.addresses = [address_0]

        # Profile Index 1
        self.profile_1 = Profile()
        self.profile_1.index = 1
        self.profile_1.source_system_key = "67890"
        self.profile_1.first_name = "Morty"
        self.profile_1.last_name = "Smith"
        self.profile_1.date_of_birth = "1999-07-30T01:00:00.000Z"
        self.profile_1.gender = "M"
        self.profile_1.emails = [email_1]
        self.profile_1.phones = [phone_1]
        self.profile_1.keys = [key_1]
        self.profile_1.addresses = [address_1]

        # Profile Index 2
        self.profile_2 = Profile()
        self.profile_2.index = 2
        self.profile_2.source_system_key = "84292"
        self.profile_2.first_name = "Lars"
        self.profile_2.last_name = "Peters"
        self.profile_2.date_of_birth = "1985-11-15T01:00:00.000Z"
        self.profile_2.gender = "M"
        self.profile_2.emails = [email_2]
        self.profile_2.phones = [phone_2]
        self.profile_2.keys = [key_2]
        self.profile_2.addresses = [address_2]