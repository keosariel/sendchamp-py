from sendchamp._http_client import CUSTOM_HTTP_CLIENT
from sendchamp.constants import (
    SMS_URL, CREATE_SENDER_ID_URL,
    SMS_DELIVERY_REPORT_URL, BULK_SMS_DELIVERY_REPORT_URL
)
from typing import Dict, List

class Sms:
    def __init__(self, headers=Dict[str, str]):
        self.headers = headers
        self.request = CUSTOM_HTTP_CLIENT(url=SMS_URL, headers=self.headers)

    def send(self, to: List[str], message: str, sender_name: str, route: str):
        """
        Sending SMS

        :params to: This represents the destination phone number. 
                    The phone number(s) must be in the international 
                    format (Example: 23490126727)
        :param message: Text message being sent.
        :param sender_name: Represents the sender of the message. 
                            This Sender ID must have been requested via 
                            the dashboard or use "Sendchamp" as default
        :param route: Here you can specify a route you want your 
                      SMS to go through. dnd, non_dnd or international

        :return: Tuple[Dict[str, dict], Error]
        """

        data = {
            "to"      : to,
            "message" : message,
            "sender_name" : sender_name,
            "route"   : route
        }

        return self.request("POST", data)
    
    def create_sender_id(self, name: str, sample: str, use_case: str):
        """
        Register Sender ID for sending SMS

        :param name: Represents the sender of the message
        :param sample: This should contain your sample message
        :param use_caes: You should pass either of the following: Transactional, Marketing, or Transactional & Marketing    

        :return: Tuple[Dict[str, Any], Error]
        """
        data = {
            "name"     : name,
            "sample"   : sample,
            "use_case" : use_case
        }
       
        return self.request.use_url(CREATE_SENDER_ID_URL)("POST", data)

    def delivery_report(self, sms_uid: str):
        """
        Request SMS Delivery report

        :param sms_uid: SMS unique ID

        :return: Tuple[Dict[str, Any], Error]
        """

        return self.request.use_url(SMS_DELIVERY_REPORT_URL + "/" + str(sms_uid))("GET")

    def bulk_delivery_report(self, bulk_sms_uid: str):
        """
        Request Bulk SMS Delivery report

        :param bulk_sms_uid: Bulk SMS unique ID

        :return: Tuple[Dict[str, Any], Error]
        """

        return self.request.use_url(BULK_SMS_DELIVERY_REPORT_URL + "/" + str(bulk_sms_uid))("GET")
    
