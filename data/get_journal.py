import urllib
import re
from bs4 import BeautifulSoup
import urllib.request
import requests
import csv

files_cat = ["category-10.html"
    ,"category-11.html"
    ,"category-12.html"
    ,"category-13.html"
    ,"category-14.html"
    ,"category-15.html"
    ,"category-16.html"
    ,"category-17.html"
    ,"category-18.html"
    ,"category-2.html"
    ,"category-3.html"
    ,"category-4.html"
    ,"category-5.html"
    ,"category-6.html"
    ,"category-68.html"
    ,"category-7.html"
    ,"category-8.html"
    ,"category-9.html"
    ]

files_cat = ["C:/Users/hyu/temp/cpvip/data/category/"+f for f in files_cat]

journal_list = []
for fname in files_cat:
    html = open(fname, 'r', encoding='utf-8')
    mystr = html.read() 
    html.close()
    #print(mystr)
    
    soup = BeautifulSoup(mystr, 'html.parser')    
    for rows in soup.find_all('a', href=True):
        string = rows['href']
        if "/qk/" in string:
            journal_list.append("http://lib.cqvip.com"+string)

print(len(journal_list))

with open("journal.txt", 'w') as myfile:
    for j in journal_list:
        print(j, file=myfile)
