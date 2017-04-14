# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    girdle.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tjose <marvin@42.fr>                       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/14 14:00:24 by tjose             #+#    #+#              #
#    Updated: 2017/04/14 16:40:58 by tjose            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import smtplib
import imaplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


myemail = "timjjose@gmail.com"
sendto = "timjose3@gmail.com"
msg = MIMEMultipart()
msg['From'] = myemail
msg['To'] = sendto
msg['Subject'] = "AN EMAIL FROM YA BOI"

### Receive latest Email ###
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

### Send an Email ###
body = raw_email
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(myemail, "Piepie1!")
text = msg.as_string()
server.sendmail(myemail, sendto, text)
server.quit()
