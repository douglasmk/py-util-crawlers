# -*- coding: utf-8 -*-
from helpers.Html import Html
from pytz import timezone
from SaneparNivelReservatorio import SaneparNivelReservatorioCrawler
from SaneparRodizio import SaneparRodizioCrawler
from send_email import SendEmail
import datetime

txtEmail = Html.tag('h2', 'PRÓXIMAS INTERRUPÇÕES NO FORNECIMENTO DE ÁGUA')

try:
    saneparRodizio = SaneparRodizioCrawler()
    txtEmail += Html.table(saneparRodizio.crawl(True), {
        'border': 1,
        'cellpadding': 5,
        'cellspacing': 0,
    })
    txtEmail += Html.br()+Html.hr()

except Exception as e:
    txtEmail += Html.tag('p', 'FALHA AO RECUPERAR A TABELA DE RODIZIOS')
    print(e)


try:
    saneparNivel = SaneparNivelReservatorioCrawler()
    niveis = saneparNivel.crawl(True)

    txtEmail += Html.tag('h2', 'NÍVEL DOS RESERVATÓRIOS')
    txtEmail += Html.tag('p', saneparNivel.data_atualizacao)
    txtEmail += Html.table(niveis, {
        'border': 1,
        'cellpadding': 5,
        'cellspacing': 0,
    })
    txtEmail += Html.tag('p', '*Sistema de Abastecimento de Água Integrado de Curitiba')

except Exception as e:
    txtEmail += Html.tag('p', 'FALHA AO RECUPERAR DADOS DE NIVEIS DOS RESERVATÓRIOS')
    print(e)

dt = datetime.datetime.now().astimezone(timezone('America/Sao_Paulo')).strftime("%d/%m/%Y %H:%M:%S")

email = SendEmail()
email.send('Rodízio Sanepar '+dt, txtEmail)
