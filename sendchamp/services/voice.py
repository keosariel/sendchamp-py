from sendchamp._http_client import CUSTOM_HTTP_CLIENT
from sendchamp.constants import (
    VOICE_URL, VOICE_DELIVERY_REPORT
)
from typing import Dict, List

class Voice:
    def __init__(self, headers: Dict[str, str]):
        self.headers = headers
        self.request  = CUSTOM_HTTP_CLIENT(url=VOICE_URL, headers=self.headers)

    def text_to_speech(self, customer_mobile_number: List[str], message: str, type: str, repeat: int):
        """
        Sending Voice Call (Text to Speech)

        :param customer_mobile_number: The number represents the destination phone number. 
                                       The number must be in international format (E.g. 2348012345678)
        :param message: The text message you to send with voice
        :param type: The type of voice message. Outgoing, incoming or template
        :param repeat: Number of times the voice message should be repeated to the recipient

        :return: Tuple[Dict[str, Any], Error]
        """

        data = {
            "customer_mobile_number" : customer_mobile_number,
            "message" : message,
            "type"    : type,
            "repeat"  : int(repeat)
        }

        return self.request("POST", data)
    
    def audio_to_voice(self, customer_mobile_number: List[str], path: str, repeat: int):
        """
        Voice (Audio File-to-Voice)

        :param customer_mobile_number: The customer mobile number. With country code, e.g 234
        :param path: Link to the audio file
        :param repeat: Number of times the voice message should be repeated to the recipient

        :return: Tuple[Dict[str, Any], Error]
        """
        
        data = {
            "customer_mobile_number" : customer_mobile_number,
            "path"   : path,
            "type"   : "outgoing",
            "repeat" : repeat
        }

        return self.request("POST", data)

    def delivery_report(self, voice_uid: str):
        """
        Request Voice Delivery Report

        :param voice_uid: Add the voice uid of the message to get the delivery report

        :return: Tuple[Dict[str, Any], Error]
        """

        return (self.request.use_url(VOICE_DELIVERY_REPORT + "/" + str(voice_uid))("GET"))
