#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 22:49:09 2021


import numpy as np
path= '/Users/sahilbhat/Downloads/Task3_Rand_words_text.txt'
 
highest_frequency_words = []
    # Add your code here 
data=np.genfromtxt(path, skip_header=0, delimiter=' ', dtype=str)
list1=data.tolist()
#print(list1)
list2=[]  
length=len(list1)
for i in range (length):
    word_count=list1.count(list1[i])
    list2.append(word_count)
    #print (list2)
max_occur=max(list2)
 #print(max_occur)
for j in range (length):
     if list1.count(list1[j])==max_occur and highest_frequency_words.count(list1[j])<1:
        highest_frequency_words.append(list1[j])  
print(highest_frequency_words)
    
    
    
    