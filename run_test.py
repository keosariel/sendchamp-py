from sendchamp import Sendchamp
import pytest
import os

PUBLIC_KEY  = os.environ.get('PUBLIC_KEY')
sendchamp = Sendchamp(public_key=PUBLIC_KEY)

def test_send_sms():
    data, error = sendchamp.sms.send(
        to=["2349164086076"],
        message= "message text",
        sender_name="Sendchamp",
        route= "international"
    )

    assert type(data) == dict
    assert bool(error) == False

def test_create_sender_id():
    data, error = sendchamp.sms.create_sender_id(
        name="New Token",
        sample= "transactional purpose",
        use_case="transactional"
    )

    assert type(data) == dict
    assert bool(error) == False

def test_text_to_speech():
    data, error = sendchamp.voice.text_to_speech(
        customer_mobile_number=["2349164086076"],
        message= "register your nin",
        type="outgoing",
        repeat=2
    )

    assert type(data) == dict
    assert bool(error) == False

def test_audio_to_voice():
    data, error = sendchamp.voice.audio_to_voice(
        customer_mobile_number=["2349164086076"],
        path= "https://sample-videos.com/audio/mp3/crowd-cheering.mp3",
        repeat=2
    )

    assert type(data) == dict
    assert bool(error) == False

def test_customer_create():
    data, error = sendchamp.customer.create(
        phone_number="2349164086076",
        first_name="kenneth",
        last_name="gabriel",
        email="kennethgabriel@gmail.com"
    )

    assert type(data) == dict
    assert bool(error) == False

def test_customer_group_create():
    data, error = sendchamp.customer.group.create("new group", "my new group")

    assert type(data) == dict
    assert bool(error) == False


def test_send_email():
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
            "value": "email fron sendchamp test"
        }
    )

    assert type(data) == dict
    assert bool(error) == False