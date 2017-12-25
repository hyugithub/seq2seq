import urllib
import re
from bs4 import BeautifulSoup
import urllib.request
import requests
import csv

path = "C:/Users/hyu/temp/cpvip/data/journal/"
list_journals = []
with open("C:/Users/hyu/temp/cpvip/data/journal/journal_list.txt", 'r', encoding='utf-8') as f:
    f2 = f.read()
    list_journals = f2.split("\n")    
    print(len(list_journals))
    print("done")
    
list_journals = [path+f for f in list_journals]    

#list_journals = list_journals[0:2]
#print(list_journals)

issue_list = []
for fname in list_journals:    
    #fname = "C:/Users/hyu/temp/cpvip/data/journal/journal-98578X.html"
    html = open(fname, 'r', encoding='utf-8')
    mystr = html.read() 
    html.close()
    #print(mystr)
    
    keyword = fname.split("-")[-1]
    keyword = keyword.split(".html")[-2]
    #print(keyword)
        
    soup = BeautifulSoup(mystr, 'html.parser')    
    for rows in soup.find_all('a', href=True):
        string = rows['href']
        if "/qk/" in string and keyword in string and "html" not in string:
            issue_list.append("http://lib.cqvip.com"+string)
print(issue_list)

with open("issue.txt", 'w') as myfile:
    for j in issue_list:
        print(j, file=myfile)
