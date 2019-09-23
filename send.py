import os
from dotenv import load_dotenv
import sendgrid
from sendgrid.helpers.mail import Mail


def send_email(from_email, from_name, to_email, subject, content):
	message = Mail(
        from_email=from_email,
        to_emails=to_email,
        subject=subject,
        html_content=content
    )

	try:
		sg = sendgrid.SendGridAPIClient(apikey=os.getenv('SENDGRID_API_KEY'))
		response = sg.send(message)
		print(response.status_code)
		print(response.body)
		print(response.headers)
	except Exception as e:
		print(str(e))


if __name__ == '__main__':
	load_dotenv()
	from_email = input('From email: ')
	from_name = input('From name: ')
	to_email = input('To email: ')
	subject = input('Subject: ')
	content = input('Content: ')
	send_email(from_email, from_name, to_email, subject, content)
