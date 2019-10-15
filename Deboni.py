import lxml.html as parser
import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from dotenv import load_dotenv
from pathlib import Path
import os
from selenium.webdriver.chrome.options import Options

COTACAO_XPATH = '//*[@id="carrinho_valor_unit"]'

class DeboniCambioCrawler(object):

    def __init__(self):
        options = Options()
        chrome_bin = os.environ.get("GOOGLE_CHROME_SHIM")
        options.binary_location = chrome_bin
        print(str(chrome_bin))

        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        # options.add_argument('window-size=1920x1080')
        self.driver = webdriver.Chrome(str(chrome_bin), chrome_options=options)
        self.items = []
        self.cotacao = []
        self.url = "https://store.debonicambio.com.br/carrinho/widget/EUR/100"
        self.xpath = ''

    def crawl(self):
        items = []
        url = self.url
        cotacao = self.crawl_url(url)
        items.append({
            "cotacao": cotacao
        })
        self.items = items

    def crawl_url(self, url):
        self.driver.get(url)
        return self.parse_cotacao()

    def get_cotacao(self):
        cotacao = self.driver.find_element_by_xpath(COTACAO_XPATH)
        return cotacao

    def parse_cotacao(self):
        html = parser.fromstring(self.driver.page_source)
        cotacoes = html.xpath(COTACAO_XPATH)
        extracted = []
        for cotacao in cotacoes:
            valor = cotacao.xpath('//*[@id="carrinho_valor_unit"]/text()')[0].strip()
            self.cotacao = valor
            extracted.append({
                "valor": valor
            })
        return extracted

    def getCotacaoFormatada(self):
        cotacaoFormatada = self.cotacao.replace('.', ',')
        cotacaoFormatada = cotacaoFormatada[8:]
        return cotacaoFormatada