from sendchamp._http_client import CUSTOM_HTTP_CLIENT
from sendchamp.constants import (
    VERIFICATION_URL, VERIFICATION_COMFIRMATION_URL
)

class Verification:
    def __init__(self, headers):
        self.headers = headers
        self.request = CUSTOM_HTTP_CLIENT(url=VERIFICATION_URL, headers=self.headers)

    def send_otp(self, channel, sender, token_type, 
                token_length, expiration_time, customer_email_address,
                customer_mobile_number, meta_data, token):
        
        """
        Sending Verification OTP

        :param channel: Voice, SMS, WhatsApp or Email
        :param sender: Specify the sender you want to use. This is important when using SMS OR Whatsapp 
                        Channel or we will select a default sender from your account. Eg: KUDA OR +234810000000
        :param token_type: numeric or alphanumeric
        :param token_length: The length of the token you want to send to your customer. Minimum is 4
        :param expiration_time: How long you want to the to be active for in minutes. (E.g 10 means 10 minutes )
        :param customer_email_address: The email address of your customer. It's required if you're using Email Channel
        :param customer_mobile_number: The phone number of your customer. It must be in international format (E.g 2348012345678). 
                                        It is required if you're using the SMS or Voice Channel
        :param meta_data: To pass additional information as an object.
        :param token: You can pass in your own token.

        :return: Tuple[Dict[str, Any], Error]
        """

        data = {
            "sender"    : sender,
            "channel" : channel,
            "token_type" : token_type,
            "token_length"   : token_length,
            "expiration_time"   : expiration_time,
            "customer_email_address" : customer_email_address,
            "customer_mobile_number" : customer_mobile_number,
            "meta_data" : meta_data,
            "token"     : token
        }

        return self.request("POST", data)
    
    def confirm_otp(self, verification_reference, verification_code):
        """
        Sending Verification OTP

        :param verification_reference: The unique reference that was returned as response when the OTP was created
        :param verification_code: The OTP that was sent to the customer.

        :return: Tuple[Dict[str, Any], Error]
        """
        data = {
            "verification_reference": verification_reference,
            "verification_code"   : verification_code
        }

       
        return self.request.use_url(VERIFICATION_COMFIRMATION_URL)("POST", data)
