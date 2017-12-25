import scrapy
from scrapy.crawler import CrawlerProcess
import numpy as np
import time

class MySpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

process = CrawlerProcess({ \
	'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)' \
    })

for param in np.arange(3):
    process.crawl(MySpider)
    time.sleep(np.random.uniform()*10 + 10)

process.start()

#process.start(stop_after_crawl=False) 

print("done")
