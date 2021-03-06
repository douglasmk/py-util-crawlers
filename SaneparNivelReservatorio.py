from bs4 import BeautifulSoup
import urllib

class SaneparNivelReservatorioCrawler(object):

    def __init__(self):
        self.reservatorios = []
        self.data_atualizacao = ""

    def crawl(self, as_dict:bool = False):
        url = 'https://site.sanepar.com.br/'

        try:
            site = urllib.request.urlopen(url).read()
            soup_site = BeautifulSoup(site)

            block_nivel = soup_site.select("div.view-id-nivel_reservatorios > div")
            self.data_atualizacao = soup_site.select("div.view-id-nivel_reservatorios span.nivel-reserv-data")[0].text.strip()
            for block_item in block_nivel :
                if block_item.select('.views-field-title span'):
                    titulo = block_item.select('.views-field-title span')[0].text.strip()
                    valor = block_item.select('.views-field-body .field-content')[0].text.strip()

                    if valor != 'Ver obra':
                        reservatorio = Reservatorio()
                        reservatorio.nome = titulo
                        reservatorio.nivel = valor
                        self.reservatorios.append(reservatorio.as_dict() if as_dict else reservatorio)
        except Exception:
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

    def get_nome(self):
        return self.nome

    def get_nivel(self):
        return self.nivel

    def as_dict(self):
        return {
            self.get_label('nome'): self.get_nome(),
            self.get_label('nivel'): self.get_nivel(),
        }

    def get_label(self, attribute:str):
        return ({
            'nome': 'Reservatório',
            'nivel': 'Nível',
        }[attribute])
