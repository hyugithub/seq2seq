import scrapy
from scrapy.crawler import CrawlerProcess
import numpy as np
import time
import sys

ts = time.time()
list_journals = []

#fname = "/data/paper.txt"
fname = "null.txt"
if len(sys.argv) > 1:
    fname = sys.argv[1]

with open(fname, 'r', encoding='utf-8') as f:
    f2 = f.read()
    list_journals = f2.split("\n")    
    print("raw entry: ", len(list_journals))

list_done = []
with open("/data/done.txt", "r") as done:
    f3 = done.read()
    list_done = f3.split("\n")
list_done = [p.split("_")[-1] for p in list_done]
list_done = set(list_done)
print("entries done: ", len(list_done))

list_journals = [u for u in list_journals if (u.split("/")[-1] in list_done) == False ]
print("after removing: ", len(list_journals))

start = 0
step = 10
end = start+step

class MySpider(scrapy.Spider):
    name = "Google Analytics"
    custom_settings = {
        "AUTOTHROTTLE_ENABLED": True,
        "AUTOTHROTTLE_START_DELAY": 5.0
    }

    def __init__(self):
        self.start = 0
        self.end = 10
        self.step = 10
        self.count = 0

    def start_requests(self):
        urls = list_journals
        self.start += self.step
        self.end += self.step
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

        #with open("/data/log/cpvip.log", 'a') as logfile:
        #    logfile.write(urls[-1]+"\n")

    def parse(self, response):
        page = response.url
        page = page.replace("http://lib.cqvip.com/qk/","")
        page = page.replace("/","_")
        filename = '/data/papers/%s' % page
        with open(filename, 'wb') as f:
            f.write(response.body)

        self.log('Saved file %s' % filename)
        self.count += 1
        if self.count > 0 and self.count % 500 == 0:
            time.sleep(np.random.uniform()*10+10)
        time.sleep(np.random.uniform()*0.25+0.2)

process = CrawlerProcess({ \
	'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)' \
    })

process.crawl(MySpider)

process.start()

#process.start(stop_after_crawl=False) 

print("done")
