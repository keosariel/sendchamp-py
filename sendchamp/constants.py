SENDER_NAMES = ["DAlert", "SAlert", "SendChamp"]

BASE_URL    = "https://api.sendchamp.com/api/v1"

# SMS
SMS_URL      = f"{BASE_URL}/sms/send"
CREATE_SENDER_ID_URL = f"{BASE_URL}/sms/create-sender-id"
SMS_DELIVERY_REPORT_URL      = f"{BASE_URL}/sms/status"
BULK_SMS_DELIVERY_REPORT_URL = f"{BASE_URL}/sms/bulk-sms-status"

# VOICE
VOICE_URL    = f"{BASE_URL}/voice/send"
VOICE_DELIVERY_REPORT = f"{BASE_URL}/voice/status"

# CUSTOMER
CUSTOMER_URL = f"{BASE_URL}/customer"
CUSTOMER_GROUP_URL = f"{BASE_URL}/core/customer-group"

# Whatsapp
WHATSAPP_URL = f"{BASE_URL}/whatsapp/message/send"

# Verification
VERIFICATION_URL = f"{BASE_URL}/verification/create"
VERIFICATION_COMFIRMATION_URL = f"{BASE_URL}/verification/confirm"

# Email
EMAIL_URL    = f"{BASE_URL}/email/send"

WALLET_BALANCE_URL = f"{BASE_URL}/wallet/wallet_balance"