import scrapy
from scrapy.crawler import CrawlerProcess
import numpy as np
import time
import sys

ts = time.time()
list_journals = []
with open("/data/papers/paper.txt", 'r', encoding='utf-8') as f:
    f2 = f.read()
    list_journals = f2.split("\n")    
    print(len(list_journals))
    print("done")

#sys.exit()

start = 0
step = 10
end = start+step

class MySpider(scrapy.Spider):
    name = "quotes"

    def __init__(self):
        self.start = 0
        self.end = 10
        self.step = 10

    def start_requests(self):
        urls = list_journals
        self.start += self.step
        self.end += self.step
        count = 0
        for url in urls:
            count += 1
            if count > 0 and count % 2000 == 0:
                time.sleep(np.random.uniform()*10+10)
            yield scrapy.Request(url=url, callback=self.parse)

        with open("/data/log/cpvip.log", 'a') as logfile:
            logfile.write(urls[-1]+"\n")

    def parse(self, response):
        page = response.url
        page = page.replace("http://lib.cqvip.com/qk/","")
        page = page.replace("/","_")
        filename = '/data/papers/%s' % page
        with open(filename, 'wb') as f:
            f.write(response.body)

        self.log('Saved file %s' % filename)

process = CrawlerProcess({ \
	'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)' \
    })

process.crawl(MySpider)

process.start()

#process.start(stop_after_crawl=False) 

print("done")
