from sendchamp._http_client import CUSTOM_HTTP_CLIENT
from sendchamp.constants import (
    CUSTOMER_URL, CUSTOMER_GROUP_URL
)
from typing import Dict

class CustomerGroup:
    def __init__(self, headers: Dict[str, str]):
        self.request = CUSTOM_HTTP_CLIENT(url=CUSTOMER_GROUP_URL, headers=headers)

    def create(self, name: str, description: str):
        """
        Create customer group

        :param name: Customer group name
        :param description: Description of the customer group

        :return: Tuple[Dict[str, Any], Error]
        """

        data = {
            "name" : name,
            "description" : description
        }

        return self.request("POST", data)

    def list(self, name: str, sample: str, use_case: str):
        """
        List

        :param name: Name of the customer group
        :param sample: group sample
        :param use_case: transactional

        :return: Tuple[Dict[str, Any], Error]
        """

        data = {
            "name" : name,
            "sample"   : sample,
            "use_case" : use_case
        }

        return self.request("GET", data)

    def update(self, uid: str, name: str, description: str):
        """
        Update customer group

        :param uid: Group external ID
        :param name: Customer group name
        :param description: Description of the customer group

        :return: Tuple[Dict[str, Any], Error]
        """
        data = {
            "name" : name,
            "description" : description
        }

        return self.request.use_url(CUSTOMER_GROUP_URL + "/" + str(uid))("PUT", data)

class Customer:
    def __init__(self, headers):
        self.request = CUSTOM_HTTP_CLIENT(url=CUSTOMER_URL, headers=headers)
        self.group   = CustomerGroup(headers=headers)

    def create(self, phone_number: str, first_name: str, last_name: str, email: str):
        """
        Create Customer

        :param phone_number: Customer Phone Number
        :param first_name: Customer first name
        :param lastname: Customer last name
        :param email: Customer email address

        :return: Tuple[Dict[str, Any], Error]
        """

        data = {
            "phone_number" : phone_number,
            "first_name"   : first_name,
            "last_name" : last_name,
            "email"     : email
        }

        return self.request("POST", data)

    def list(self):
        """
        List Customer

        :return: Tuple[Dict[str, Any], Error]
        """

        return self.request("GET")
    
    def update(self, external_user_id: str, phone_number: str, first_name: str, last_name: str, email: str):
        """
        Update Customer

        :param external_user_id: External ID of the user
        :param phone_number: Customer Phone number
        :param first_name: Customer first name
        :param last_name: Customer last name
        :param email: Customer email address

        :return: Tuple[Dict[str, Any], Error]
        """

        data = {
            "phone_number" : phone_number,
            "first_name"   : first_name,
            "last_name" : last_name,
            "email"     : email
        }

        return self.request.use_url(CUSTOMER_URL + "/" + str(external_user_id))("PUT", data)
    
    def delete(self, external_user_id: str):
        """
        Delete Customer

        :param external_user_id: Customer External ID
        :return: Tuple[Dict[str, Any], Error]
        """

        return self.request.use_url(CUSTOMER_URL + "/" + str(external_user_id))("DELETE")
    
