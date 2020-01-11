import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Dan K'
email['to'] = 'email@gmail.com'
email['subject'] = 'Sending with python!'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('email@gmail.com', 'password')
    smtp.send_message(email)
    print('all good')

# ***************************************
# import smtplib
# from email.message import EmailMessage
#
# email = EmailMessage()
# email['from'] = 'Dan K'
# email['to'] = 'dankkaplan@gmail.com'
# email['subject'] = 'Sending with python!'
#
# email.set_content('I am testing sending with python, how cool is that?')
#
# with smtplib.SMTP(host='smtp.gmail.com',port = 587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login('dankkaplan@gmail.com', 'password')
#     smtp.send_message(email)
#     print('all good')
