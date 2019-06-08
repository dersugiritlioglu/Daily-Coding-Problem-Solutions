# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 17:51:17 2019

@author: DERSU GIRITLIOGLU
"""

"""

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear 
time and constant space. In other words, find the lowest positive integer that 
does not exist in the array. The array can contain duplicates and negative 
numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should 
give 3.

You can modify the input array in-place.

"""

import numpy as np

def firstmissingposint(list):

    #num = np.inf
    smallnum = 0
    # a big number...
    bignum = 9999
    
    for i in range(len(list)):
        if list[i] > 0:
            if list[i] == smallnum +1 :
                smallnum = list[i]
                
    for i in range(len(list)):
        if list[i] > 0:
            if list[i] < bignum and list[i]>smallnum:
            bignum = list[i]
        print("\n",i)
        print("bignum: ", bignum)
        print("smallnum: ",smallnum)
    if bignum-smallnum == 1: # we have spotted everynumber until the first number, so answer need not to be one of the smaller numbers
        return bignum + 1
    else:
        return smallnum+1

def firstmissinginteger(list):
    #num = np.inf
    smallnum = 0
    # a big number...
    bignum = 9999
    for i in range(len(list)):
        if list[i] > 0:
            if list[i] == smallnum +1 :
                smallnum = list[i]    
            elif list[i] < bignum and list[i]>smallnum:

    

l = [5,-4,0,7,1,19,2,3,-9,-7,4,8,6]
print(firstmissingposint(l))