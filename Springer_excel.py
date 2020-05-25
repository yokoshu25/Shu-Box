#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 09:51:58 2020

@author: yokoishusei
"""
# Test
import pandas as pd
import urllib
import re
import time
import os

os.chdir('/Users/yokoishusei/Desktop/mypy/Springer')
excel_path = 'Free+English+textbooks.xlsx'
df = pd.read_excel(excel_path)

df.head(3)

col_lis = list(df.columns)
class_lis = list(df['Subject Classification'])

clas = []

for i in range(len(class_lis)):
    clas.append(class_lis[i].split('; '))

genres = []
for s in clas:
    genres.extend(s)

for i in range(100):
    for i in genres:
        if ',' in i:
            genres.remove(i)
            genres.extend(i.split(','))


genres = [i.strip() for i in genres]


    
genre = []
for s in genres:
    if s not in genre:
        genre.append(s)
genre.sort()


# int_lis = ['Big Data','Business Information Systems','Computer Applications', 
#            'Computer Engineering','Data Structures','IT in Business', 
#            'Information Systems Applications (incl.Internet)', 
#            'Information Systems and Communication Service','Python', 
#            'e-Business/e-Commerce','e-Commerce/e-business',]

int_lis = ['IT in Business','Business Information Systems' ]




        
l = pd.DataFrame()
c = -1
for n in range(len(clas)):
    c += 1
    for i in int_lis:
        if i in clas[c]:
            l = l.append(df.iloc[c])

