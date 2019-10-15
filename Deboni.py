import lxml.html as parser
import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

COTACAO_XPATH = '//*[@id="carrinho_valor_unit"]'

class DeboniCambioCrawler(object):

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        self.driver = webdriver.Chrome(options=options)
        self.items = []
        self.cotacao = []
        self.url = "https://store.debonicambio.com.br/carrinho/widget/EUR/100"
        self.xpath = ''

    # def save_items(self):
    #     keys = self.items[0].keys()
    #     with open("items.csv", 'w') as f:
    #         dict_writer = csv.DictWriter(f, keys)
    #         dict_writer.writeheader()
    #         dict_writer.writerows(self.items)

    # def crawl_list_and_save(self, search_list):
    #     self.crawl_list(search_list)
    #     self.save_items()

    # def crawl_list(self, search_list):
    #     items = []
    #     for term in search_list:
    #         url = BASE_URL + term
    #         tweets = self.crawl_url(url)
    #         items.append({
    #             "term": term,
    #             "tweets": tweets
    #         })
    #     self.items = items

    # def enviar_email(self):
    #     dt = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    #     txtEmail = 'Cotação Euro Deboni em '+dt+'\n\n'
    #     txtEmail += self.cotacao+' COM IOF INCLUSO\n\n'
    #     txtEmail += 'Confira em https://debonicambio.com.br/'

    #     email = SendEmail()
    #     email.send('Cotação Euro Deboni '+dt, txtEmail)

    def crawl(self):
        items = []
        url = self.url
        cotacao = self.crawl_url(url)
        items.append({
            "cotacao": cotacao
        })
        self.items = items
        # self.save_items()

    def crawl_url(self, url):
        self.driver.get(url)
        # return self.get_cotacao()
        return self.parse_cotacao()

    def get_cotacao(self):
        # try:
        #     WebDriverWait(self.driver, 20).until(
        #         lambda driver: new_cotacao(driver))
        # except TimeoutException:
        #     # simple exception handling, just move on in case of Timeout
        #     cotacao = self.driver.find_element_by_xpath(COTACAO_XPATH)
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