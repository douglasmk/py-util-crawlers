import json
import urllib3
import time
from datetime import datetime


class FlexCambioCrawler(object):

    def __init__(self):
        self.cotacoes = []

    def crawl(self, as_dict:bool = False):
        http = urllib3.PoolManager()
        url = 'https://api-moedas.herokuapp.com/v1/moedas-order'

        try:
            response = http.request('GET', url)
            data = json.loads(response.data)
            for item in data:
                if (item['tipo'] == 'Moeda' and item['nome'] == 'EURO'):
                    cotacao = Cotacao()
                    cotacao.valor = item['venda']
                    cotacao.data = item['updated_at']
                    self.cotacoes.append(cotacao.as_dict() if as_dict else cotacao)
                    break
        except Exception:
            self.cotacao = 'ERRO'

        return self.cotacoes


class Cotacao():

    def __init__(self):
        self.valor = ''
        self.data = ''
        self.site = 'https://www.flexcambio.com.br'

    def get_valor(self):
        return self.valor

    def get_data(self):
        return self.data

    def get_site(self):
        return self.site

    def get_cotacao_formatada(self):
        cotacao_formatada = self.valor.replace('.', ',')
        cotacao_formatada = 'R$ '+cotacao_formatada[:4]
        return cotacao_formatada

    def get_data_formatada(self):
        return datetime.strftime(datetime.strptime(self.data, '%Y-%m-%d %H:%M:%S'), "%d/%m/%Y %H:%M:%S")

    def as_dict(self):
        return {
            self.get_label('valor'): self.get_cotacao_formatada(),
            self.get_label('data'): self.get_data_formatada(),
            self.get_label('site'): self.get_site(),
        }

    def get_label(self, attribute:str):
        return ({
            'valor': 'Valor',
            'data': 'Data',
            'site': 'Site',
        }[attribute])
