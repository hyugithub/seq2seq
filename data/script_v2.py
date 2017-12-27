# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 13:43:02 2017

@author: HYU
"""

# in order to do this, we need to run split first
# split -l 500 -d -a 4 ../paper2.txt chunk
import numpy as np

num_trunks = 6376
num_computer = 638

size = 10

count = 0

for count in range(num_computer):
    fout = open("C:/Users/YUH015/Desktop/script/script_"+str(count)+".sh", "w")
    fout.write("#!/bin/bash \n")
    fout.write("echo 'sudo halt' | at now + 180 minutes \n")
    #fout.write("sudo -i -u ubuntu \n")
    fout.write("export AWS_ACCESS_KEY_ID=AKIAJD2EKB4LMHOIW6CA")
    fout.write("\n")
    fout.write("export AWS_SECRET_ACCESS_KEY=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")
    fout.write("\n")
    fout.write("export AWS_DEFAULT_REGION=us-east1")
    fout.write("\n")
    #fout.write("sudo mkdir /data")
    #fout.write("\n")
    fout.write("sudo mount /dev/xvdc /data")
    fout.write("\n")
    #fout.write("sudo chown ubuntu /data")
    fout.write("mkdir /data/log /data/papers /data/script")
    fout.write("\n")
    fout.write("sudo apt-get -q -y install awscli")
    fout.write("\n")
    fout.write("aws s3 cp s3://s3free5gb/cqvip/done.txt /data/")
    fout.write("\n")
    fout.write("aws s3 cp s3://s3free5gb/cqvip/script.tar.gz /data/")
    fout.write("\n")
    fout.write("aws s3 cp s3://s3free5gb/cqvip/chks_0500.tar.gz /data/")
    fout.write("\n")
    #fout.write("cd script")
    #fout.write("\n")
    fout.write("tar -xzf /data/script.tar.gz -C /data/script")
    fout.write("\n")
    fout.write("tar -xzf /data/chks_0500.tar.gz -C /data/script")
    fout.write("\n")
    for k in range(size*count, size*(count+1)):    
        if k >= num_trunks:
            break
        name = "/home/ubuntu/anaconda3/bin/python3 /home/ubuntu/cr2/seq2seq/data/cpvip.py /data/script/chunk"+format(k, '04d')+" >/data/log/run.log \n"
        fout.write(name)
        name = "tar -czf /data/papers/result.tar.gz /data/papers/*.html \n"
        fout.write(name)
        name = "aws s3 cp /data/papers/result.tar.gz s3://s3free5gb/cqvip/result/result.$(date '+%Y.%m.%d-%H.%M.%S').tar.gz \n"
        fout.write(name)        
        name = "rm /data/papers/*.html \n"
        fout.write(name)
        sec = int(np.random.uniform()*200+200)
        fout.write("sleep %d\n" % sec)            
    fout.close()

fout.close()
