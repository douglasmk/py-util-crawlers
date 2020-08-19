from bs4 import BeautifulSoup
import urllib

class SaneparNivelReservatorioCrawler(object):

    def __init__(self):
        self.reservatorios = []

    def crawl(self):
        url = 'http://site.sanepar.com.br/'

        try:
            site = urllib.request.urlopen(url).read()
            soup_site = BeautifulSoup(site)

            blockNivel = soup_site.select("div.view-id-nivel_reservatorios > div")

            for blockItem in blockNivel :
                titulo = blockItem.select('.views-field-title')[0].text.strip()
                valor = blockItem.select('.views-field-body')[0].text.strip()

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
