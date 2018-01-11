# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 21:29:56 2018

@author: hyu
"""
import os
import sys
import time
from bs4 import BeautifulSoup
import multiprocessing
import numpy as np

#print(sys.getdefaultencoding())
#fname = path + "82147X_201205_42712784.html"

def read_abstract(fname, path):
    with open(path+fname, encoding="utf-8", mode = "r") as f:
        soup = BeautifulSoup(f, "html.parser")
        
    zhaiyao = "摘\u3000\u3000要"
    
    abstract_chinese = ""
    abstract_english = ""
    for s in soup.find_all("span", {"class" : "abstrack"}):
        #remove Chinese zhaiyao
        abstract_chinese = s.get_text().replace(zhaiyao,"")
        #print(s.class)
        #print("chinese")
        #print(abstract_chinese)
        tmp = s.find_next_sibling("span", class_="en")
        #print(type(tmp))
        if tmp != None:
            abstract_english = tmp.get_text()
            #if abstract_english != "" and "Objective" in abstract_english:
                #print("english")
                #print(abstract_english)
    
    if abstract_english != "" and abstract_chinese != "" and "Objective" in abstract_english:
        # now we should store results in somewhere
        return abstract_english, abstract_chinese
        #result_e.append(abstract_english)
        #result_c.append(abstract_chinese)
    return "",""
    #EOF
      
class functor:
    def __init__(self, data_path):
        self.path = data_path
    
    def action(self, fn):
        return read_abstract(fn, self.path)
    
def worker(cnt, glist, data_path, return_dict):
    fc = functor(data_path)
    tmp = list(map(fc.action, glist))
    return_dict[cnt] = [(e,c) for e,c in tmp if e != "" and c != ""]

if __name__ == '__main__':    

    ts = time.time()    
        
    result_english = []
    result_chinese = []
    #data_path = "C:/Users/hyu/Desktop/seq2seq/data/"
    data_path = "/data/html/papers/"
    
    global_list = os.listdir(data_path)
    #global_list = global_list[0:1000]
    glen = len(global_list)
    
    num_cpu = 7
    pos_start = list(np.arange(0, glen, glen/float(num_cpu)))
    pos_end = pos_start[1:]
    pos_end.append(glen)

    jobs = []    
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    count = 0
    for s,e in zip(pos_start,pos_end):
        p = multiprocessing.Process(target=worker, 
                                    args=(count,global_list[int(s):int(e)],data_path,return_dict))
        jobs.append(p)
        count += 1
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()    
    
    #fc = functor(data_path)
    
    #result = list(map(fc.action, global_list))
    
    
    count = 0
    with open("/data/output/result_abstract.txt", "w", encoding='utf-8') as fout:
        for k in return_dict.keys():
            for re,rc in return_dict[k]:
                if re != "" and rc != "":
                    count += 1
                    fout.write("".join(["hyu sequence record start ",str(count),"\n"]))
                    fout.write("".join([re,"\n"]))
                    fout.write("".join([rc,"\n"]))
    print(count, "records written")    
    print("total time = %.3f seconds"%(time.time()-ts))


