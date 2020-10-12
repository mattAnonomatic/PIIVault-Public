class ApiError:
    status = ""
    message = ""

    def __init__(self, status="", message=""):
        self.status = status
        self.message = message