# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 20:43:24 2019

@author: DERSU GIRITLIOGLU
"""

"""

This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the 
number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 
'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not 
allowed.

"""
import numpy as np
msg = '111'
count=0

def howmanyways(msg, count):
    # detecting zeros would be important
# =============================================================================
#     zero = np.zeros(len(msg))
#     for i in range(len(zero)):
#         if msg[i] == '0':
#             zero[i] == 1
# =============================================================================
    print(count)
    for i in range(len(msg)):
        count+=1
        if msg[i] != '0':
            count = howmanyways(msg[i+1:],count)
        print(count)
    return count
    
howmanyways(msg,count)