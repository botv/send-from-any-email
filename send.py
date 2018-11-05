import os
from dotenv import load_dotenv
import sendgrid
from sendgrid.helpers.mail import *


def send_email(from_email, from_name, to_email, subject, content):
	sg = sendgrid.SendGridAPIClient(apikey=os.getenv('SENDGRID_API_KEY'))
	from_email = Email(from_email, from_name)
	to_email = Email(to_email)
	subject = subject
	content = Content('text/plain', content)
	mail = Mail(from_email, subject, to_email, content)
	response = sg.client.mail.send.post(request_body=mail.get())
	print(response.status_code)
	print(response.body)
	print(response.headers)


if __name__ == '__main__':
	load_dotenv()
	from_email = input('From email: ')
	from_name = input('From name: ')
	to_email = input('To email: ')
	subject = input('Subject: ')
	content = input('Content: ')
	send_email(from_email, from_name, to_email, subject, content)
