import urllib
import re
from bs4 import BeautifulSoup
import urllib.request
import requests
import csv

#list_journals = []
#with open("C:/Users/hyu/temp/cpvip/data/journal/journal_list.txt", 'r', encoding='utf-8') as f:
#    f2 = f.read()
#    list_journals = f2.split("\n")    
#    print(len(list_journals))
#    print("done")
    
#list_journals = [path+f for f in list_journals]    

#list_journals = list_journals[0:2]
#print(list_journals)

list_journals = ["../../site/issues/sample.html"]

for fname in list_journals:    
    html = open(fname, 'r', encoding='utf-8')
    mystr = html.read() 
    html.close()
    
    soup = BeautifulSoup(mystr, 'html.parser')    
    for rows in soup.find_all('a', href=True):
        string = rows['href']
#        print(string)
        if "/qk/" in string and "html" in string:
      	    print(string)
            #issue_list.append("http://lib.cqvip.com"+string)
#print(issue_list)

