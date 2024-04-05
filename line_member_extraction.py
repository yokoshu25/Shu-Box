#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 20:47:05 2021

@author: shuseiyokoi
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
sys.setrecursionlimit(10000)#エラー回避
import joblib
import time
from tqdm import tqdm
import random

f = open('/Downloads/[LINE] Chat in 【ノート必見👀】〇〇卒内定者の会.txt', 'r')
#f = open('/yasapy/ひま/[LINE]_Chat_copy.txt')
file = f.read()
text = file.split('\n')
f.close()

members = []

for sentence in tqdm(text):
    if 'joined the group.' in sentence:
        sentence = sentence[8:][:-20]
        members.append(sentence)
        
left = []
for sentence in tqdm(text):
    if 'left the group.' in sentence:
        sentence = sentence[8:][:-18]
        left.append(sentence)
        

for member in members:
    if member in left:
        members.remove(member)
        
f = open("SB_LINE_members.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()


try:
    with open('/Users/Desktop/mypy/ひま/LINE_members.txt', mode='w') as f:
        f.write(str(members))
except FileExistsError:
    pass

    
# members = []
       
# for message in tqdm(sentences):
#     a = message.replace('\t\u2068\u2068', '')
#     a = a.replace('\u2069\u2069 joined the group.', '')
#     a = a[5:]
#     members.append(a)
    



# len(members)

# n = random.sample(range(1,452), 8)

# for i in n:
#     print(members[i])
