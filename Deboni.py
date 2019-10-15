import lxml.html as parser
import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from dotenv import load_dotenv
from pathlib import Path
import os

COTACAO_XPATH = '//*[@id="carrinho_valor_unit"]'

class DeboniCambioCrawler(object):

    def __init__(self):
        options = webdriver.ChromeOptions()
        chrome_bin=False

        if os.getenv("GOOGLE_CHROME_SHIM"):
            chrome_bin = os.getenv("GOOGLE_CHROME_SHIM")
        if chrome_bin:
            options.add_argument('binary='+chrome_bin)

        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        self.driver = webdriver.Chrome(options=options)
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