# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import sys
import time
 
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'C:\\Users\\kcast\\predj\\predj')
import items


class PredjspiderSpider(scrapy.Spider):
    name = 'predjspider7'
    allowed_domains = ['www.theinternationaljournal.org/ojs/index.php?journal=rjebs&page=article&op=view&path%5B%5D=']
    ASIN = list(range(464,8193))
    ASIN = [str(i) for i in ASIN]

    def start_requests(self):
        for i in self.ASIN:
            req = Request('http://www.theinternationaljournal.org/ojs/index.php?journal=rjebs&page=article&op=view&path%5B%5D='+i,callback = self.parse_article)
            # Wait for 5 seconds
          #  time.sleep(.5)
            yield req

    def parse_article(self, response):
        item = items.PredjItem()
        item['title'] = response.xpath("//div[@id='articleTitle']/h3/text()").getall()
        item['author'] = response.xpath("//div[@id='authorString']/em/text()").getall()
        item['abstract'] = response.xpath("//div[@id='articleAbstract']").getall()
        return item