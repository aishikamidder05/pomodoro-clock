import os, time, requests
from boltiot import Sms

# later use time to avoid alerts at times you are busy

def send_simple_message():
	return requests.post(
		"https://api.mailgun.net/v3/{}/messages".format(os.environ['MAILGUN_URL']),
		auth=("api", os.environ['MAILGUN_API_KEY']),
		data={"from": "User Name <mailgun@{}>".format(os.environ['MAILGUN_URL']),
			"to": [os.environ['RECIPIENT_EMAIL']],
			"subject": "ALERT",
			"text": "STOP! 45 mins is over. Go take a break!!"})

if(os.environ['IS_ACTIVATED']=='1'):
    response=send_simple_message()
    print("Response EMAIL",response)

    sms = Sms(os.environ['SSID'], os.environ['AUTH_TOKEN'], os.environ['TO_NUMBER'], os.environ['FROM_NUMBER'])
    response = sms.send_sms("STOP! 45 mins is over! Take a chill pill ")
    print("Response SMS",response)
