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

#%%

# Trivial solution

def basic(mylist, k):
	for i in range(len(mylist)):
		for j in range(i,len(mylist)):
			if mylist[i] + mylist[j] == k :
				return True
	return False

#%%

# In one pass

def myfunc(mylist, k):
	for i in range(len(mylist)):
		temp_l = mylist.copy()
		temp_l.remove(mylist[i])
		# if we did not use remove function, function would return true for mylist[i] * 2
		if k - mylist[i] in temp_l : 
			return True
	return False

#%%
			
l = [10, 15, 3, 7]
k = 17

print(myfunc(l,k))


