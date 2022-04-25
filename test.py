from xml.etree.ElementTree import PI
from sendchamp import Sendchamp
from pprint import pprint

sendchamp = Sendchamp(public_key=PUBLIC_KEY)

# data, error = sendchamp.wallet_balance()

# sms

# data, error = sendchamp.sms.send(
#     to=["2349164086076"],
#     message= "test",
#     sender_name="osas",
#     route= "international"
# )

# data, error = sendchamp.sms.create_sender_id(
#     name="SMS",
#     sample= "...",
#     use_case="marketing"
# )

# uid = "4a75dbd0-8a61-420f-80b5-aafbc7504ee9"

# data, error = sendchamp.sms.delivery_report(
#     sms_uid=uid
# )


# data, error = sendchamp.sms.bulk_delivery_report(
#     bulk_sms_uid=uid
# )

# data, error = sendchamp.voice.text_to_speech(
#     customer_mobile_number=["2349164086076"],
#     message= "call osas asap",
#     type="outgoing",
#     repeat=3
# )

# uid = "63840a67-f546-4a93-a8f6-674392a595ae"

# data, error = sendchamp.voice.delivery_report(
#     voice_uid=uid
# )

# customer

# data, error = sendchamp.customer.create(
#     phone_number="2349164086076",
#     first_name="terry",
#     last_name="jay",
#     email="terryjay@gmail.com"
# )

# data, error = sendchamp.customer.list()

# data, error = sendchamp.customer.update(
#     external_user_id="579eb992-ab97-4dfb-9357-9dd1b5144f87",
#     first_name="newterry",
#     last_name="newjay",
#     phone_number="2349164086076",
#     email="newterryjay@gmail.com"
# )

# data, error = sendchamp.customer.delete("579eb992-ab97-4dfb-9357-9dd1b5144f87")

# data, error   = sendchamp.customer.group.create("new group", "my new group")

# data, error   = sendchamp.customer.group.update(
#     uid="5b5a3591-bf94-46e4-b7b6-8cfd12406a90",
#     name="new new group", 
#     description="new my new group")

# whatsapp

# data, error   = sendchamp.whatsapp.send_template(
#     sender="2348086995538",
#     recipient="2349164086076",
#     template_code="template code",
#     custom_data=[]
# )

# {'code': 6, 'message': 'Invalid sender', 'status': 'failed'}

# data, error   = sendchamp.whatsapp.send_message(
#     sender="Sendchamp",
#     recipient="2349164086076",
#     message="from progran"
# )

# data, error = sendchamp.email.send(
#     subject="Sendchamp subject",
#     sender={
#         "email":"keosariel@sendchamp.com",
#         "name":"keosariel"
#     },
#     to=[{
#         "email":"kennethgabriel78@gmail.com",
#         "name":"gabriel"
#     }],
#     message_body={
#         "type": "text/html",
#         "value": "email fron sendchamp"
#     }
# )



# pprint(error)
# pprint(data)


