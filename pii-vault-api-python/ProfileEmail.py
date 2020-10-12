class ProfileEmail:
    email_address = ""

    def __init__(self, email_address = ""):
        self.email_address = email_address

    def get_json_object(self):
        return { 'EmailAddress' : self.email_address }