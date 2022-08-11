#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 03:05:23 2021


#import string
#data=list(string.ascii_uppercase)
#num1=ord('A')-77
#print(num1)
    
list1=[]
ref_value=-27
letters=[]
for i in range (len(letters)):
  value= ord(letters[i])-77
  list1.append(value)
#print(max_value1)
max_value=max(list1)
index_max_value=list1.index(max_value)
 #print(var[index_max_value])
 #print (max_value)
for j in range (len(list1)):
   value1= list1[j]
   if(len(list1)==1):
        ref_value=list1[0]
        initial_index=j
        final_index=j
   for k in range (j+1,len(list1)):
      value1=value1+list1[k]
      if value1 > ref_value:
       ref_value=value1
       initial_index=j
       final_index=k               #print(ref_value)
first_letter= letters[initial_index] 
last_letter= letters[final_index]
first_last_letter= first_letter + last_letter
        
if max_value > ref_value:
   ref_value=max_value
   initial_index=index_max_value
   final_index=index_max_value
   #print(ref_value)
   first_letter= letters[initial_index] 
   last_letter= letters[final_index]
   first_last_letter=first_letter + last_letter
      

greatest_score=ref_value

