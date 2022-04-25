from sendchamp._http_client import CUSTOM_HTTP_CLIENT
from sendchamp.constants import (
    WHATSAPP_URL
)
from typing import Dict

class Whatsapp:
    def __init__(self, headers: Dict[str, str]):
        self.headers = headers
        self.request = CUSTOM_HTTP_CLIENT(url=WHATSAPP_URL, headers=self.headers)

    def send_template(self, sender: str, recipient: str, template_code: str, custom_data: Dict[str, str]):
        """
        Send highly structured messages to your customers based on approved template

        :param sender: Your approved Whatsapp number on Sendchamp. 
                       You can use our phone number if you have not registered a number 2347067959173
        :param recipient: Whatsapp number of the customer you are sending the message to
        :param template_code: You can find this on the template page under 
                              Whatsapp Channel of your Sendchamp dashboard
        :param custom_data: Custom data

        :return: Tuple[Dict[str, Any], Error]
        """

        data = {
            "sender"    : sender,
            "recipient" : recipient,
            "template_code" : template_code,
            "type"   : "template",
            "custom_data"   : custom_data
        }

        return self.request("POST", data)

    def send_message(self, message: str, sender: str, recipient: str):
        """
        Send Messages via WhatsApp

        :param message: message to customer
        :param sender: This will be the activated Whatsapp phone number or use our default number 2347067959173
        :param recipient: This will be the phone number of the customer E.g 234811111111

        :return: Tuple[Dict[str, Any], Error]
        """

        data = {
            "message": message,
            "type"   : "text",
            "sender" : sender,
            "recipient" : recipient   
        }

       
        return self.request("POST", data)

    def send_video(self, sender: str, recipient: str, link: str,):
        """
        Send Video via WhatsApp

        :param sender: This will be the activated Whatsapp phone number E.g 234810000000
        :param recipient: This will be the phone number of the customer E.g 234811111111
        :param link: link to video i.e (https://sample-videos.com/audio/mp3/crowd-cheering.mp3)

        :return: Tuple[Dict[str, Any], Error]
        """

        data = {
            "type"   : "video",
            "sender" : sender,
            "recipient" : recipient,
            "link"   : link
        }
       
        return self.request("POST", data)

    def send_audio(self, sender: str, recipient: str, message: str, link: str, ):
        """
        Send Audio via WhatsApp

        :param sender: This will be the activated Whatsapp phone number E.g 234810000000
        :param recipient: This will be the phone number of the customer E.g 234811111111
        :param message: message to customer
        :param link: link to audio i.e (https://sample-videos.com/audio/mp3/crowd-cheering.mp3)

        :return: Tuple[Dict[str, Any], Error]
        """

        data = {
            "message": message,
            "type"   : "audio",
            "sender" : sender,
            "recipient" : recipient,
            "link"   : link
        }

        return self.request("POST", data)
    
    def send_location(self, sender: str, recipient: str, longititude: int, latitude: int, name: str, address: str):
        """
        Send Location via WhatsApp

        :param sender: This will be the activated Whatsapp phone number E.g 234810000000
        :param recipient: This will be the phone number of the customer E.g 234811111111
        :param longititude: example: - 46.662787
        :param latitude: example: -23.553610
        :param name: example - Robbu Brazil
        :param address: example: Av. Angélica, 2530 - Bela Vista, São Paulo - SP, 01228-200
        
        :return: Tuple[Dict[str, Any], Error]
        """

        data = {
            "name"   : name,
            "longititude" : longititude,
            "latitude"    : latitude,
            "address"     : address,
            "type"   : "location",
            "sender" : sender,
            "recipient" : recipient,
        }
       
        return self.request("POST", data)
    
    def send_sticker(self, sender: str, recipient: str, link: str):
        """
        Send Sticker via WhatsApp

        :param sender: This will be the activated Whatsapp phone number E.g 234810000000
        :param recipient: This will be the phone number of the customer E.g 234811111111
        :param link: link to sticker i.e (https://studio.posit.us/api/samples/sticker.webp)

        :return: Tuple[Dict[str, Any], Error]
        """

        data = {
            "type"   : "sticker",
            "sender" : sender,
            "recipient" : recipient,
            "link"   : link
        }
       
        return self.request("POST", data)

    