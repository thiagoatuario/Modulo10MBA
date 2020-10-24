import scrapy

class UolSpider(scrapy.Spider):
    name = 'uol_spider'
    start_urls = ['https://www.uol.com.br/']
    def parse(self,response):
        titulos = response.css(".HU_currency__quote::text")
        conteudo = titulos[0].get().strip()
        if conteudo != "":
            print('A cotação do dólar é: ',conteudo)
