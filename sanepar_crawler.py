from SaneparRodizio import SaneparRodizioCrawler
from send_email import SendEmail
import datetime
from pytz import timezone

saneparRodizio = SaneparRodizioCrawler()
rodizios = saneparRodizio.crawl()

dt = datetime.datetime.now().astimezone(timezone('America/Sao_Paulo')).strftime("%d/%m/%Y %H:%M:%S")
txtEmail = '\n -----------------------------------------------------------------------------------------------------------\n'
txtEmail += '|             INÍCIO           |       RETOMADA        |    NORMALIZAÇÃO                        |\n'

for rodizio in rodizios :
    txtEmail += '| '+rodizio.getInicio()+' | '+rodizio.getRetomada()+' | '+rodizio.getNormalizacao()+' ('+rodizio.getPeriodo()+') | '+rodizio.getObservacao()
    txtEmail += '\n------------------------------------------------------------------------------------------------------------\n'

print(txtEmail)
email = SendEmail()
email.send('Rodízio Sanepar '+dt, txtEmail)
