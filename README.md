# sendchamp-py
Sendchamp API wrapper

## Installation

```pip install sendchamp-py```

```py
from sendchamp import Sendchamp

sendchamp = Sendchamp(public_key=PUBLIC_KEY)
```


## Sendchamp API Methods 

1. **[SMS](#sms)**
   * Send SMS
   * Create Sender ID
   * SMS Delivery report
   * Bulk SMS Delivery report
  
2. **[Voice](#voice)**
   * Text-to-Speech
   * Audio File-to-voice
   * Delivery Report
  
3. **Customer**
   * [Customer](#customer)
     * Create Customer
     * List Customer
     * Update Customer
     * Delete Customer
    
   * [Customer Group](#customer-group)
     * Create customer group
     * List customer groups
     * Update customer group
  
4. **[Whatsapp](#whatsapp)**
   * Send Template
   * Send Message
   * Send Video
   * Send Audio
   * Send Location
   * Send Sticker

5. **[Verification](#verification)**
   * Send OTP
   * Confirm OTP

6. **[Email](#email)**
   * Send Email


## SMS

**Sending SMS**

```py
data, error = sendchamp.sms.send(
   to=["2342345678912"],
   message= "message test",
   sender_name="Sendchamp",
   route= "international"
)
```

**Create Sender ID**

```py
data, error = sendchamp.sms.create_sender_id(
    name="CompanyName",
    sample= "sample",
    use_case="marketing"
)
```

**SMS Delivery report**

```py
data, error = sendchamp.sms.delivery_report(
    sms_uid=uid
)
```

**Bulk SMS Delivery report**

```py
data, error = sendchamp.sms.bulk_delivery_report(
    bulk_sms_uid=uid
)
```

## Voice

**Text-to-Speech**

```py
data, error = sendchamp.voice.text_to_speech(
    customer_mobile_number=["2342345678912"],
    message= "register your nin",
    type="outgoing",
    repeat=2
)
```

**File-to-Voice**

```py
data, error = sendchamp.voice.audio_to_voice(
    customer_mobile_number=["2342345678912"],
    path= "https://sample-videos.com/audio/mp3/crowd-cheering.mp3",
    repeat=2
)
```

**Voice Delivery Report**

```py
data, error = sendchamp.voice.delivery_report(
    voice_uid=uid
)
```

## Customer

**Create Customer**

```py
data, error = sendchamp.customer.create(
    phone_number="2342345678912",
    first_name="kenneth",
    last_name="gabriel",
    email="kennethgabriel78@gmail.com"
)
```

**List Customer**

```py
data, error = sendchamp.customer.list()
```

**Update Customer**

```py
data, error = sendchamp.customer.update(
    external_user_id=uid,
    first_name="kenneth_",
    last_name="gabriel_",
    phone_number="2342345678912",
    email="kennethgabriel@gmail.com"
)
```

**Delete Customer**

```py
data, error = sendchamp.customer.delete(uid)
```

## Customer Group

**Create Group**

```py
data, error = sendchamp.customer.group.create(
                    name="Waitlist", 
                    description="first users"
              )
```

**List**
```py
data, error = sendchamp.customer.group.list(
                  name="Waitlist", 
                  sample="sample",
                  use_case="use case"
              )
```

**Update Customer Group**

```py
data, error   = sendchamp.customer.group.update(
    uid=uid,
    name="Premium Users", 
    description="Paying users")
```

## Whatsapp

**Send Template**

```py
data, error   = sendchamp.whatsapp.send_template(
    sender="2342345678912",
    recipient="2345678912345",
    template_code="template code",
    custom_data={"Body": {}}
)
```

**Send Message**

```py
data, error = sendchamp.whatsapp.send_message(
    sender="234810000000",
    recipient="2342345678912",
    message="message"
)
```

**Send Video**

```py
data, error = sendchamp.whatsapp.send_video(
    sender="234810000000",
    recipient="234811111111",
    link="https://sample-videos.com/audio/mp3/crowd-cheering.mp3"
)
```

**Send Audio**

```py
data, error = sendchamp.whatsapp.send_audio(
    sender="234810000000",
    recipient="234811111111",
    link="https://sample-videos.com/audio/mp3/crowd-cheering.mp3"
)
```

**Send Location**

```py
data, error = sendchamp.whatsapp.send_location(
    sender="234810000000",
    recipient="234811111111",
    longititude=46.662787,
    latitude=23.553610,
    name="Robbu Brazil",
    address="Av. Angélica, 2530 - Bela Vista, São Paulo - SP, 01228-200"
)
```

**Send Sticker**

```py
data, error = sendchamp.whatsapp.send_audio(
    sender="234810000000",
    recipient="234811111111",
    link="https://studio.posit.us/api/samples/sticker.webp"
)
```

## Verification

**Send OTP**

```py
data, error = sendchamp.verification.send_otp(
    channel="channel", 
    sender="234810000000", 
    token_type="numeric", 
    token_length=5, 
    expiration_time=4, 
    customer_email_address="customer@gmail.com",
    customer_mobile_number="234811111111", 
    meta_data={}, 
    token="your_token"
)
```

**Confirm OTP**

```py
data, error = sendchamp.verification.confirm_otp(
                verification_reference=ref,
                verification_code=code
              )
```

## Email

**Send Email**

```py
data, error = sendchamp.email.send(
    subject="Sendchamp subject",
    sender={
        "email":"keosariel@sendchamp.com",
        "name":"keosariel"
    },
    to=[{
        "email":"kennethgabriel78@gmail.com",
        "name":"gabriel"
    }],
    message_body={
        "type": "text/html",
        "value": "email fron sendchamp"
    }
)
```
