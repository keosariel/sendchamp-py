from .services import (
    Customer, Email, Sms,
    Verification, Voice, Whatsapp
)
from ._http_client import CUSTOM_HTTP_CLIENT
from .constants    import WALLET_BALANCE_URL

class Sendchamp:

    def __init__(self, public_key: str):
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {public_key}"
        }

        headers_wo_bearer = headers.copy()
        headers_wo_bearer.update({ "Authorization": public_key })

        self.sms   = Sms(headers=headers)
        self.email = Email(headers=headers)
        self.voice = Voice(headers=headers)
        self.customer     = Customer(headers=headers_wo_bearer)
        self.whatsapp     = Whatsapp(headers=headers)
        self.verification = Verification(headers=headers)

        self.headers = headers
    
    def wallet_balance(self):
        req = CUSTOM_HTTP_CLIENT(WALLET_BALANCE_URL, self.headers)

        return req.requests("POST")
    



        