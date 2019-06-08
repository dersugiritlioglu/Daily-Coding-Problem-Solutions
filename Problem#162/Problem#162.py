# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 12:56:00 2019

@author: DERSU GIRITLIOGLU

Daily Coding Problems - 162 [Medium]
"""

"""

Good morning! Here's your coding interview problem for today.

This problem was asked by Square.

Given a list of words, return the shortest unique prefix of each word. For example, given the list:

dog
cat
apple
apricot
fish
Return the list:

d
c
app
apr
f

"""


l = ["dog","cat","apple","apricot","fish","almond","doggy"]
newlist = []

for i in range(len(l)):
    # for every element in the list
    a = l.copy()
    for j in range(len(l[i])):
        # look at every letter
        letter = l[i][j]
        for k in range(len(a)-1,-1,-1):
            if j<len(a[k]):
                # variable word length
                if a[k][j] != letter:
                    a.remove(a[k])
            else:
                # shorter word
                a.remove(a[k])
        if len(a) == 1:
            newlist.append(a[0][:j+1])
            # we have found the representation
            break
    if len(a) > 1:
        # we have found multiple reprs. Select the word that we care initially
        newlist.append(l[i])

print(l)
print(newlist)








