# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import sys
import time
 
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'C:\\Users\\kcast\\predj\\predj')
import items


class PredjspiderSpider(scrapy.Spider):
    name = 'predjspider4'
    allowed_domains = ['www.engii.org/PaperInformation.aspx?id=']
    ASIN = list(range(701,4098))
    ASIN = [str(i) for i in ASIN]

    def start_requests(self):
        for i in self.ASIN:
            req = Request('http://www.engii.org/PaperInformation.aspx?id='+i,callback = self.parse_article)
            # Wait for 5 seconds
          #  time.sleep(.5)
            yield req

    def parse_article(self, response):
        item = items.PredjItem()
        item['title'] = response.xpath("//ul/li[2]/text()").getall()
        item['author'] = response.xpath("//ul/li[5]/text()").getall()
        item['abstract'] = response.xpath("//li[@class='li14']/p/text()").getall()
        return item