from crypt import methods
import httpx
from .error import Error

class CUSTOM_HTTP_CLIENT:

    def __init__(self, url, headers):
        self.url = url
        self.headers = headers
    
    def __call__(self, method, data=None):
        method = method.upper()
        if method not in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
            raise NotImplementedError(f"Method '{method}' not recognised.")

        if method == "GET":
            make_request = httpx.get
        elif method == "POST":
            make_request = httpx.post
        elif method == "PUT":
            make_request = httpx.put
        elif method == "PATCH":
            make_request = httpx.patch
        elif method == "DELETE":
            make_request = httpx.delete

        if method == "GET" or method == "DELETE":
            res  = make_request(self.url, headers=self.headers)
        else:
            res  = make_request(self.url, json=data, headers=self.headers)
            
        json_response = res.json()
        
        data  = json_response.get("data")
        error = Error(**json_response)

        return data, error

    def use_url(self, url):
        return CUSTOM_HTTP_CLIENT(url=url, headers=self.headers)