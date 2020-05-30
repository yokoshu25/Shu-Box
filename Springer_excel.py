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

os.chdir('-pathname-')
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


int_lis = ['Business Information Systems', 
            'Data Structures','IT in Business', 
            'Information Systems Applications (incl.Internet)', 
            'Information Systems and Communication Service','Python', 
            'e-Business/e-Commerce','e-Commerce/e-business' 'Statistics and Computing/Statistics Programs',
            'Statistics for Business/Economics/Mathematical Finance/Insurance',]

#int_lis = ['IT in Business','Business Information Systems']




        
New_df = pd.DataFrame()
c = -1
for n in range(len(clas)):
    c += 1
    for i in int_lis:
        if i in clas[c]:
            New_df = New_df.append(df.iloc[c])
            
New_df = New_df.drop_duplicates()
New_df = New_df.reset_index(drop = True)


########## cited from https://takala.tokyo/takala_wp/2020/05/09/889/ credits on Takala ######## 


N = New_df.shape[0]

for i in range(26,36):

    time.sleep(10) # Manner

    download_URL = 'https://link.springer.com/content/pdf/' + New_df['DOI URL'][i].split('http://doi.org')[1] + '.pdf'
    editoin = New_df['Edition'][i]

    year = re.findall('\d{4}', editoin)[0]
    title = New_df['Book Title'][i].replace(' ', '_')

    file_name = 'pdf\\' + year + '_' + title + '.pdf'

    urllib.request.urlretrieve(download_URL, file_name)










