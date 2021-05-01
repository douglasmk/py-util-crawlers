from FlexCambio import FlexCambioCrawler
from send_email import SendEmail
import csv
import datetime
from pytz import timezone

flexCrawler = FlexCambioCrawler()
flexCrawler.crawl()

dt = datetime.datetime.now().astimezone(timezone('America/Sao_Paulo')).strftime("%d/%m/%Y %H:%M:%S")
txtEmail = 'VALORES ATUALIZADOS EM '+flexCrawler.get_data_formatada()
txtEmail += '\n--------------------------------------------------------------\n'
txtEmail += 'Flex  '+flexCrawler.get_cotacao_formatada()+'  https://www.flexcambio.com.br'
txtEmail += '\n--------------------------------------------------------------\n'
print(txtEmail)
email = SendEmail()
email.send('Cotação Euro '+dt, txtEmail)
