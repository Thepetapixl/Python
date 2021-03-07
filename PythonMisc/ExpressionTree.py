#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 11:26:30 2020

@author: admin
"""
# Assignment 2 - Expression Tree

class Expression:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
               
     
def operator(char):
    if(char == '*' or char == '%' or char == '+' or char == '/' or char == '^' or char == '-'):
        return True
    else:
        return False
   
def create(prefix):
    stack = []
    prefix = prefix[:: -1]
   
    for char in prefix:
        if not operator(char):
            node = Expression(char)
            stack.append(node)
        else:
            node = Expression(char)
            leftnode = stack.pop()
            rightnode = stack.pop()
            node.right = rightnode
            node.left = leftnode
            stack.append(node)
    node = stack.pop()       
    return node
           
def inorderR(node):
    if node is not None:
        inorderR(node.left)
        print(node.data)
        inorderR(node.right)
         
 
def preorderR(node):
    if node is not None:
        preorderR(node.left)
        preorderR(node.right)
        print(node.data,end = ' ')
                 
           
def postorderR(node):
    if node is not None:
        print(node.data,end = ' ')
        postorderR(node.left)
        postorderR(node.right)
       
           
def inorderwithout(node):
    stack1 = []
    while node is not None:
        while node.left is not None:
            stack1.append(node)
            node = node.left
        print(node.data)
        node = stack1.pop()
        print(node.data)
        stack1.push(node)
        while node.right is not None:
            stack1.append(node)
            node = node.right
        print(node.data)
        node = stack1.pop()       
    
        
   

root = None      
while True:
   
    print('\n\n1 Insertion \n2 Inorder using Recursion \n3 Preorder  \n4 Postorder \n5 Inorder recursive\n6 Post order recursive\n7 Post order non recursive\n8 for Exit')
    print('Only 4 inputs work as of now')
    choice = int(input('Enter your Choice :'))

    if choice == 1:
        prefix = input("Enter the prefix Expression")
        print(prefix)
        root = create(prefix)
        print(root)
    elif choice == 2:
        root = inorderR(root)
   
    elif choice == 3:
        root = preorderR(root)
       
    elif choice == 4:
        root = postorderR(root)
       
    elif choice == 8:
        exit()
    