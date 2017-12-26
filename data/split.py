import scrapy
from scrapy.crawler import CrawlerProcess
import numpy as np
import time
import sys

ts = time.time()
list_journals = []
with open("/data/paper.txt", 'r', encoding='utf-8') as f:
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

with open("/data/paper2.txt", "w") as fout:
    for u in list_journals:
        fout.write(u+"\n")
print("done")
