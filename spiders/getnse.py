import scrapy
from scrapy_splash import SplashRequest
from scrapy.crawler import CrawlerProcess
from scrapy_selenium import SeleniumRequest


class GpSpider(scrapy.Spider):
    name = 'gp'

    def start_requests(self):
        url = 'https://www.nseindia.com/get-quotes/equity?symbol=PSUBNKBEES'
        yield SeleniumRequest(url=url, callback=self.parse, wait_time=15)

    def parse(self, response):
        yield {
            # 'name': response.css('td:nth-child(2) ::text()').get(),
            'title': response.css('title ::text').get(),
            'ltp': response.css('div#quoteLtp ::text').get()
        }


process = CrawlerProcess()
process.crawl(GpSpider)
process.start()
