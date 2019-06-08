# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 14:51:41 2018

@author: DERSU GIRITLIOGLU
"""

"""
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes 
the tree into a string, and deserialize(s), which deserializes the string back 
into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node = Node('root', Node('left', Node('left.left')), Node('right'))


def serialize(root):
    serialize_inner_bf(root)
    mystr = l[0]
    for i in range(1,len(l)):
        mystr = mystr + "," + l[i]
    return mystr


def serialize_inner_bf(root):
    l.append(root.val)
    if root.left != None:
        l.append(root.left.val)
    else:
        l.append('None')
    if root.right != None:
        l.append(root.right.val)
    else:
        l.append('None')
    
    if root.left != None:
        serialize(root.left)
    if root.right != None:
        serialize(root.right)


def serialize_inner_df(root):
    l.append(root.val)
    if root.left != None:
        serialize(root.left)
    else:
        l.append("None")
    if root.right != None:
        serialize(root.right)
    else:
        l.append("None")
    return

l = []
string = serialize(node)
print(str)
print(l)
deserialize(string)

def deserialize(s):
    listnew = s.split(",")
    deserialize_inner(listnew)
    
    
def deserialize_inner(list):
    # bottom-up
    for i in range(len(list)):
        if list[i+1] == 'None' and list[i+2] == 'None':
            # no child
            newnode = Node(list[i])
            for j in range(3):
                list.remove(list[i])
            list.insert(i,'None')
            deserialize_inner(list)
            #bottommost element extracted and tree reorginized
    # UNFINISHED
    newnode = Node(listnew[0])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    