# -*- coding: utf-8 -*-
from SaneparRodizio import SaneparRodizioCrawler
from SaneparNivelReservatorio import SaneparNivelReservatorioCrawler
from send_email import SendEmail
import datetime
from pytz import timezone

saneparRodizio = SaneparRodizioCrawler()
rodizios = saneparRodizio.crawl()

saneparNivel = SaneparNivelReservatorioCrawler()
niveis = saneparNivel.crawl()

dt = datetime.datetime.now().astimezone(timezone('America/Sao_Paulo')).strftime("%d/%m/%Y %H:%M:%S")
txtEmail = ''
try:
    txtEmail += ' PRÓXIMAS INTERRUPÇÕES NO FORNECIMENTO DE ÁGUA\n'
    txtEmail += ' _____________________________________________________________________________\n'
    txtEmail += '|       INÍCIO        |      RETOMADA       |          NORMALIZAÇÃO           |\n'
    txtEmail += ' -----------------------------------------------------------------------------\n'

    for rodizio in rodizios :
        txtEmail += '| '+rodizio.get_inicio()+' | '+rodizio.get_retomada()+' | '+rodizio.get_normalizacao()+' ('+rodizio.get_periodo()+') | '+rodizio.get_observacao()
        txtEmail += '\n -----------------------------------------------------------------------------\n'
except Exception as e:
    txtEmail += '|                   FALHA AO RECUPERAR A TABELA DE RODIZIOS                   |\n'
    txtEmail += ' -----------------------------------------------------------------------------\n'

try:
    if len(niveis) > 0 :
        txtEmail += '\n\n ______________________________'
        txtEmail += '\n| NÍVEL DOS RESERVATÓRIOS '
        txtEmail += '\n ------------------------------'
        txtEmail += '\n| '+saneparNivel.data_atualizacao
        txtEmail += '\n =============================='

        for nivel in niveis :
            txtEmail += '\n| '+nivel.get_nome()+': '+nivel.get_nivel()+' '
            txtEmail += '\n ------------------------------'

        txtEmail += '\n *Sistema de Abastecimento de Água Integrado de Curitiba'
except Exception as e:
    txtEmail += 'FALHA AO RECUPERAR DADOS DE NIVEIS DOS RESERVATÓRIOS\n'

if len(rodizios) > 0 or len(niveis) > 0 :
    print(txtEmail)
    email = SendEmail()
    email.send('Rodízio Sanepar '+dt, txtEmail)
