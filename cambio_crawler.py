from Deboni import DeboniCambioCrawler
from FlexCambio import FlexCambioCrawler
from send_email import SendEmail
import csv
import datetime
from pytz import timezone

# deboniCrawler = DeboniCambioCrawler()
# deboniCrawler.crawl()

flexCrawler = FlexCambioCrawler()
flexCrawler.crawl()

dt = datetime.datetime.now().astimezone(timezone('America/Sao_Paulo')).strftime("%d/%m/%Y %H:%M:%S")
txtEmail = 'VALORES ATUALIZADOS EM '+dt
# txtEmail += '\n--------------------------------------------------------------\n'
# txtEmail += 'Deboni  '+deboniCrawler.getCotacaoFormatada()+'  https://debonicambio.com.br'
txtEmail += '\n--------------------------------------------------------------\n'
txtEmail += 'Flex  '+flexCrawler.getCotacaoFormatada()+'  https://www.flexcambio.com.br'
txtEmail += '\n--------------------------------------------------------------\n'
print(txtEmail)
email = SendEmail()
# email.send('Cotação Euro '+dt, txtEmail)