import scrapy
import base64


class ScrSpider(scrapy.Spider):
    name = "scr"
    start_urls = [
        "http://free-proxy.cz/en/",
    ]

    def parse(self, response):
        for row in response.xpath('//*[@id="proxy_list"]//tbody/tr'):
            a = row.xpath('td[1]//text()').extract_first()
            try:
                yield {
                    'IP_address': base64.b64decode(a.split('"')[1]).decode('utf-8'),
                    'Post': row.xpath('td[2]//text()').extract_first()
                }
            except IndexError:
                print("Index is out of range")
