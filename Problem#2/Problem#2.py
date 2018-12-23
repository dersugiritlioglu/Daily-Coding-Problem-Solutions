# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 17:46:01 2018

@author: DERSU GIRITLIOGLU
"""

"""

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index 
i of the new array is the product of all the numbers in the original array 
except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be 
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would 
be [2, 3, 6].

Follow-up: what if you can't use division?

"""

import numpy as np

# Trivial solution

def mytrivialfunc(arr):
	# O(n)
	tot = 1
	for i in range(arr.shape[0]):
		tot *= arr[i]
	
	for i in range(arr.shape[0]):
		arr[i] = tot / arr[i]
	return arr

# Follow-up solution
	
def myfunc(arr):
	# O(n^2)
	newarr = np.ones(arr.shape[0])
	for i in range(arr.shape[0]):
		for j in range(arr.shape[0]):
			if i != j:
				newarr[i] *= arr[j]
	return newarr

arr = np.array([1,2,3,4,5])

print(myfunc(arr))
