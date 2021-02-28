# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 17:56:26 2020

@author: User
"""
import random
f=open("0.txt")
a=f.read()
f.close()
for i in (range(10000)):
    r=random.randint(0,len(a)-1)
    f=open(str(i+1)+".txt",'w')
    f.write(a[r])
    f.close


