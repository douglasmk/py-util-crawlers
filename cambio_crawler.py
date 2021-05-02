from FlexCambio import FlexCambioCrawler
from send_email import SendEmail
import datetime
from pytz import timezone
from helpers.Html import Html

txtEmail = Html.tag('h2', 'COTAÇÕES DO EURO')

try:
    flexCrawler = FlexCambioCrawler()
    txtEmail += Html.table(flexCrawler.crawl(True), {
        'border': 1,
        'cellpadding': 5,
        'cellspacing': 0,
    })

except Exception as e:
    txtEmail += Html.tag('p', 'FALHA AO RECUPERAR A TABELA DE COTAÇÕES')
    print(e)

dt = datetime.datetime.now().astimezone(timezone('America/Sao_Paulo')).strftime("%d/%m/%Y %H:%M:%S")

email = SendEmail()
email.send('Cotação Euro '+dt, txtEmail)
