import scrapy


class MlSpider(scrapy.Spider):
    name = "ml"

    start_urls = [f"https://lista.mercadolivre.com.br/celulares-telefones/celulares-smartphones/iphone_Desde_1_NoIndex_True"]

    def parse(self, response, **kwargs):
        for i in response.xpath('//li[@class="ui-search-layout__item shops__layout-item"]'):
            price = i.xpath('.//div[@class="ui-search-price__second-line shops__price-second-line"]//text()').getall()
            title = i.xpath('.//h2[@class="ui-search-item__title shops__item-title"]//text()').get()
            link = i.xpath('.//a/@href').get()

            yield {
                'price': price[0],
                'title': title,
                'link': link
            }

        next_page = response.xpath('//a[contains(@title,"Seguinte")]//@href').get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)