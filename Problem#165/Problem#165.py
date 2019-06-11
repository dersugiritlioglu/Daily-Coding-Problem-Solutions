# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 16:19:34 2019

@author: DERSU GIRITLIOGLU

Daily Coding Problems - 165 [Medium]
"""

"""

This problem was asked by Google.

Given an array of integers, return a new array where each element in the new array is the number of smaller elements to the right of that element in the original input array.

For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:

There is 1 smaller element to the right of 3
There is 1 smaller element to the right of 4
There are 2 smaller elements to the right of 9
There is 1 smaller element to the right of 6
There are no smaller elements to the right of 1

"""

a = [3, 4, 9, 6, 1]
b = []

for i in range(len(a)):
    count = 0
    for j in range(i+1,len(a)):
        if a[i] > a[j]:
            count += 1
    b.append(count)
    
print(b)




