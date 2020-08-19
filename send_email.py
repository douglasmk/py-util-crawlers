import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

__all__ = ["SendEmail"]
EMAIL_USERNAME = os.getenv("EMAIL_USERNAME")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_TO = os.getenv("EMAIL_TO")

class SendEmail(object):
    def send(self, assunto, texto):
        # conexão com os servidores do google
        smtp_ssl_host = 'smtp.gmail.com'
        smtp_ssl_port = 465

        from_addr = EMAIL_USERNAME
        to_addrs = EMAIL_TO.split(',')

        # a biblioteca email possuí vários templates
        # para diferentes formatos de mensagem
        # neste caso usaremos MIMEText para enviar
        # somente texto
        header = '<html><body><pre style="font: monospace">'
        footer = '</pre></body></html>'
        message = MIMEText(header+texto+footer, 'html')
        message['subject'] = assunto
        message['from'] = from_addr
        message['to'] = ', '.join(to_addrs)

        # conectaremos de forma segura usando SSL
        server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
        # para interagir com um servidor externo precisaremos
        # fazer login nele
        server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
        server.sendmail(from_addr, to_addrs, message.as_string())
        return server.quit()
