import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email ['from'] = 'input name'
email['to'] = 'receiver\'s email'
email['subject'] = 'Here is how I send emails using python!'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('inputemail', 'input password')
	smtp.send_message(email)
	print('     process complete!')