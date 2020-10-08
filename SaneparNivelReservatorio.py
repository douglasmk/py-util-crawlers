from bs4 import BeautifulSoup
import urllib

class SaneparNivelReservatorioCrawler(object):

    def __init__(self):
        self.reservatorios = []
        self.dataAtualizacao = ""

    def crawl(self):
        url = 'http://site.sanepar.com.br/'

        try:
            site = urllib.request.urlopen(url).read()
            soup_site = BeautifulSoup(site)

            blockNivel = soup_site.select("div.view-id-nivel_reservatorios > div")
            self.dataAtualizacao = soup_site.select("div.view-id-nivel_reservatorios span.nivel-reserv-data")[0].text.strip()
            for blockItem in blockNivel :
                if blockItem.select('.views-field-title span'):
                    titulo = blockItem.select('.views-field-title span')[0].text.strip()
                    valor = blockItem.select('.views-field-body .field-content')[0].text.strip()

                    if titulo != 'Barragem Miringuava':
                        reservatorio = Reservatorio()
                        reservatorio.nome = titulo
                        reservatorio.nivel = valor
                        self.reservatorios.append(reservatorio)
        except:
            print('ERRO')
            reservatorio = Reservatorio()
            reservatorio.nome = 'ERRO'
            reservatorio.nivel = 'ERRO'
            self.reservatorios.append(reservatorio)

        return self.reservatorios


class Reservatorio():

    def __init__(self):
        self.nome = ''
        self.nivel = ''

    def getNome(self):
        return self.nome

    def getNivel(self):
        return self.nivel
