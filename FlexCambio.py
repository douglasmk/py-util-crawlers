import json
import urllib3


class FlexCambioCrawler(object):

    def __init__(self):
        self.cotacao = ''

    def crawl(self):
        http = urllib3.PoolManager()
        url = 'https://www.flexcambio.com.br/api/public/v1/moedas-order'
        response = http.request('GET', url)

        data = json.loads(response.data)
        for item in data:
            if (item['tipo'] == 'Moeda' and item['nome'] == 'EURO'):
                self.cotacao = item['venda']
                break


    def getCotacao(self):
        return self.cotacao

    def getCotacaoFormatada(self):
        cotacaoFormatada = self.cotacao.replace('.', ',')
        cotacaoFormatada = 'R$ '+cotacaoFormatada[:4]
        return cotacaoFormatada