from ApiError import ApiError

class ApiResponse:
    success = False
    data = {}
    error = ApiError()

    def __init__(self):
        self.success = False
        self.data = {}
        self.error = ApiError()

    def ProcessObject(self, response):
        self.success = response["Success"]
        
        if self.success:
            self.data = response["Data"]
            self.error = ApiError()
        else:
            self.error = ApiError(response["Error"]["Status"], response["Error"]["Message"])