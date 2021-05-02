from dotenv import load_dotenv
from pathlib import Path
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Content
import os

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class SendEmail(object):
    def send(self, assunto, texto):
        # using SendGrid's Python Library
        # https://github.com/sendgrid/sendgrid-python
        message = Mail(
            from_email=os.getenv('EMAIL_SENDER'),
            to_emails=os.getenv('EMAIL_TO').split(';'),
            subject=assunto,
            html_content=texto)
        try:
            sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e)
