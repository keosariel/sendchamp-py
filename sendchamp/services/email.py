from sendchamp._http_client import CUSTOM_HTTP_CLIENT
from sendchamp.constants import (
    EMAIL_URL
)

from typing import Dict, List

class Email:
    def __init__(self, headers: Dict[str, str]):
        self.headers = headers
        self.request = CUSTOM_HTTP_CLIENT(url=EMAIL_URL, headers=self.headers)

    def send(self, subject: str, to: List[Dict[str, str]], 
                sender: Dict[str, str], message_body: Dict[str, str]):
        """
        Sending Email

        :param subject: Email Subject
        :param to: Add the name and email address of the recipeint
        :param sender: Add the name and email address of the sender. This is optional. 
                       If you don't specify a name, the system will pick your business short name
        :param message_body: This is the body of your message. Type should be text/html and value should be either a text or html
        """

        data = {
            "subject" : subject,
            "to"   : to,
            "from" : sender,
            "message_body" : message_body
        }

        return self.request("POST", data)

    