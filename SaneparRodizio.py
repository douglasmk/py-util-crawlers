import json
import urllib3
import requests
import time
import datetime


class SaneparRodizioCrawler(object):

    def __init__(self):
        self.rodizios = []

    def crawl(self):
        timestampAtual = int(time.strftime("%s", time.gmtime()))
        http = urllib3.PoolManager()
        url = 'https://services1.arcgis.com/46Oage49MS2a3O6A/arcgis/rest/services/Mapa_Rodizio_Abastecimento_RMC_View/FeatureServer/1/queryRelatedRecords?f=json&definitionExpression=&relationshipId=1&returnGeometry=false&objectIds=147&outFields=*'

        try:
            data = requests.get(url).json()
            for item in data['relatedRecordGroups'][0]['relatedRecords']:
                if timestampAtual < int(str(item['attributes']['INICIO'])[:10]) :
                    rodizio = Rodizio()
                    rodizio.inicio = int(str(item['attributes']['INICIO'])[:10])
                    rodizio.retomada = int(str(item['attributes']['RETOMADA'])[:10])
                    rodizio.normalizacao = int(str(item['attributes']['NORMALIZACAO'])[:10])
                    rodizio.periodo = item['attributes']['PERIODO']
                    rodizio.observacao = item['attributes']['OBSERVACAO']

                    self.rodizios.append(rodizio)
        except:
            print('ERRO')
            rodizio = Rodizio()
            rodizio.inicio = 'ERRO'
        return self.rodizios


    def getCotacao(self):
        return self.cotacao

    def getCotacaoFormatada(self):
        cotacaoFormatada = self.cotacao.replace('.', ',')
        cotacaoFormatada = 'R$ '+cotacaoFormatada[:4]
        return cotacaoFormatada


class Rodizio():

    def __init__(self):
        self.inicio = ''
        self.retomada = ''
        self.normalizacao = ''
        self.observacao = ''
        self.periodo = ''

    def formatData(self, data):
        return datetime.datetime.fromtimestamp(data).strftime("%d/%m/%Y %H:%M:%S")

    def getInicio(self):
        return self.formatData(self.inicio)

    def getRetomada(self):
        return self.formatData(self.retomada)

    def getNormalizacao(self):
        return self.formatData(self.normalizacao)

    def getPeriodo(self):
        return self.periodo

    def getObservacao(self):
        return self.observacao
