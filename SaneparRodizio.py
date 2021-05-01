import json
import urllib3
import requests
import time
import datetime
from pytz import timezone


class SaneparRodizioCrawler(object):

    def __init__(self):
        self.rodizios = []

    def crawl(self):
        timestamp_atual = int(time.strftime("%s", time.gmtime()))
        url = 'https://services1.arcgis.com/46Oage49MS2a3O6A/arcgis/rest/services/Mapa_Rodizio_Abastecimento_RMC_View/FeatureServer/1/queryRelatedRecords?f=json&definitionExpression=&relationshipId=1&returnGeometry=false&objectIds=283&outFields=*'

        try:
            data = requests.get(url).json()
            for item in data['relatedRecordGroups'][0]['relatedRecords']:
                if timestamp_atual < int(str(item['attributes']['NORMALIZACAO'])[:10]) :
                    rodizio = Rodizio()
                    rodizio.inicio = int(str(item['attributes']['INICIO'])[:10])
                    rodizio.retomada = int(str(item['attributes']['RETOMADA'])[:10])
                    rodizio.normalizacao = int(str(item['attributes']['NORMALIZACAO'])[:10])
                    rodizio.periodo = item['attributes']['PERIODO']
                    rodizio.observacao = item['attributes']['OBSERVACAO']

                    self.rodizios.append(rodizio)
        except Exception:
            print('ERRO')
            rodizio = Rodizio()
            rodizio.inicio = 'ERRO'
            self.rodizios.append(rodizio)

        return self.rodizios


class Rodizio():

    def __init__(self):
        self.inicio = ''
        self.retomada = ''
        self.normalizacao = ''
        self.observacao = ''
        self.periodo = ''

    def format_data(self, data):
        return datetime.datetime.fromtimestamp(data).astimezone(timezone('America/Sao_Paulo')).strftime("%d/%m/%Y %H:%M:%S")

    def get_inicio(self):
        return self.format_data(self.inicio)

    def get_retomada(self):
        return self.format_data(self.retomada)

    def get_normalizacao(self):
        return self.format_data(self.normalizacao)

    def get_periodo(self):
        return self.periodo

    def get_observacao(self):
        return self.observacao
