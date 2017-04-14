# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    texttest.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tjose <marvin@42.fr>                       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/14 14:00:24 by tjose             #+#    #+#              #
#    Updated: 2017/04/14 15:47:40 by tjose            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import smtplib
import imaplib
import json
import time
#import gspread
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
#from oauth2client.client import SignedJwtAssertionCredentials
from twilio.rest import TwilioRestClient

json_key = json.load(open('.json'))
#scope = ['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'],
											json_key['private_key'].encode(),
											scope)
#gc = gspread.authorize(credentials)
#wks = gc.open("text list")
#wks_ppl = wks.get_worksheet(0)

ACCOUNT_SID = 'AC314d69b9e40a9ce15adebb69f6b2a778'
AUTH_TOKEN = '148173759046dc8983bc8a808c9e9c52'

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

print 'Sending message ' + 'me'
client.messages.create(
		to="+5107096227",
		from_="+6508521195",
		body="sup",
		)


##########################################################
myemail = "timjjose@gmail.com"
sendto = "timjose3@gmail.com"
msg = MIMEMultipart()
msg['From'] = myemail
msg['To'] = sendto
msg['Subject'] = "AN EMAIL FROM YA BOI"

### Receiving Emails ###
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(myemail, 'Piepie1!')
mail.list()
mail.select("inbox")
result, data = mail.search(None, "ALL")

ids = data[0]
id_list = ids.split()
latest_email_id = id_list[-1]

result, data = mail.fetch(latest_email_id, "(RFC822)")

raw_email = data[0][1]

### Sending Emails ###
body = raw_email
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(myemail, "Piepie1!")
text = msg.as_string()
server.sendmail(myemail, sendto, text)
server.quit()



