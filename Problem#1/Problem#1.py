# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 15:55:44 2018

@author: DERSU GIRITLIOGLU
"""

"""

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

"""

import numpy as np

def myfunc(mylist, k):
	all_less = True
	all_greater = True
	for i in range(len(mylist)-1):
		if k<mylist[0] + mylist[i+1]:
			all_greater = False
		elif k>mylist[0] + mylist[i+1]:
			all_less = False
		else:
			return True
		