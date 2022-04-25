class Error:

    def __init__(self, code, message, status, **kwargs):
        self.code    = int(code)
        self.message = message
        self.status  = status

    def __bool__(self):
        return not (self.code >= 200 and self.code <= 300)
    
    def __repr__(self):
        return str({"code": self.code, "message": self.message, "status":self.status})