# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import sys
import time
 
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'C:\\Users\\kcast\\predj\\predj')
import items


class PredjspiderSpider(scrapy.Spider):
    name = 'predjspider3'
    allowed_domains = ['www.sersc.org/journals/index.php/IJAST/article/view/']
    ASIN = list(range(1,5535))
    ASIN = [str(i) for i in ASIN]

    def start_requests(self):
        for i in self.ASIN:
            req = Request('http://www.sersc.org/journals/index.php/IJAST/article/view/'+i,callback = self.parse_article)
            # Wait for 5 seconds
          #  time.sleep(.5)
            yield req

    def parse_article(self, response):
        item = items.PredjItem()
        item['title'] = response.xpath("//article[@class='obj_article_details']/h1/text()").getall()
        item['author'] = response.xpath("//ul[@class='item authors']").getall()
        item['abstract'] = response.xpath("//div[@class='main_entry']/div/text()").getall()
        return item