import os, time, requests
from boltiot import Sms
from decouple import config
# later use time to avoid alerts at times you are busy

def send_simple_message(message):
	return requests.post(
		"https://api.mailgun.net/v3/{}/messages".format(os.environ['MAILGUN_URL']),
		auth=("api", os.environ['MAILGUN_API_KEY']),
		data={"from": "Pomodoro Clock <mailgun@{}>".format(os.environ['MAILGUN_URL']),
			"to": [os.environ['RECIPIENT_EMAIL']],
			"subject": "ALERT",
			"text": message})

if(config['IS_ACTIVATED']=='1'):
    message="STOP! 45 mins is over. Go take a break!!"
    response=send_simple_message(message)
    print("Response EMAIL",response)

    sms = Sms(config['SSID'], config['AUTH_TOKEN'], config['TO_NUMBER'], config['FROM_NUMBER'])
    response = sms.send_sms(message)
    print("Response SMS",response)

    time.sleep(900)

    message="Time's up, now get back to work!"
    response=send_simple_message(message)
    print("Response EMAIL",response)

    sms = Sms(config['SSID'], config['AUTH_TOKEN'], config
	      ['TO_NUMBER'], config['FROM_NUMBER'])
    response = sms.send_sms(message)
    print("Response SMS",response)


