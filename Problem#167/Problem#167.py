# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 00:51:17 2019

@author: DERSU GIRITLIOGLU

Daily Coding Problems - 167 [Hard]
"""
"""

This problem was asked by Airbnb.

Given a list of words, find all pairs of unique indices such that the concatenation of the two words is a palindrome.

For example, given the list ["code", "edoc", "da", "d"], return [(0, 1), (1, 0), (2, 3)].

"""

l = ["code", "edoc", "da", "d", "ad"]
p = []

for i in range(len(l)):
    f = l[i]
    # first word
    for j in range(len(l)):
        s = l[j]
        # second word
        if f != s:
            word = f + s
            if len(word) % 2 == 0:
                #even
                flag = True
                for k in range(len(word)//2):
                    if word[k] != word[-k-1]:
                        flag = False
                        break
                    
            else:
                #odd
                flag = True
                for k in range(len(word)//2+1):
                    if word[k] != word[-k-1]:
                        flag = False
                        break
            
            if flag:
               p.append((i,j)) 
            

print(p)                
                
                