import json
import urllib3
import time
from datetime import datetime


class FlexCambioCrawler(object):

    def __init__(self):
        self.cotacao = ''
        self.data = ''

    def crawl(self):
        http = urllib3.PoolManager()
        url = 'https://api-moedas.herokuapp.com/v1/moedas-order'

        try:
            response = http.request('GET', url)
            data = json.loads(response.data)
            for item in data:
                if (item['tipo'] == 'Moeda' and item['nome'] == 'EURO'):
                    self.cotacao = item['venda']
                    self.data = item['updated_at']
                    break
        except Exception:
            self.cotacao = 'ERRO'


    def get_cotacao(self):
        return self.cotacao

    def get_cotacao_formatada(self):
        cotacao_formatada = self.cotacao.replace('.', ',')
        cotacao_formatada = 'R$ '+cotacao_formatada[:4]
        return cotacao_formatada

    def get_data_formatada(self):
        return datetime.strftime(datetime.strptime(self.data, '%Y-%m-%d %H:%M:%S'), "%d/%m/%Y %H:%M:%S")
