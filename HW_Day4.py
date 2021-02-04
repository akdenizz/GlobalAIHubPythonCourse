# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 22:29:15 2021

@author: asus
"""

def prime():
    
    lower = 0
    upper = 100
    
    for n in range(lower,upper+1):
        if n > 1 : # because prime number cannot be less than one
            for i in range(2,n):
                if n % i == 0 : # if n is divisible by any number between 2 and n(is a number that between 1 and 100)
                    break
            else: # if n is not divisible any number ; also means it can be divisible only 1 and itself , Then print the numbers
                print(n) # Then print the numbers
     
prime()



# Another version of function that uses parameter

def prime(l,u):
    
    for n in range(l,u+1):
        if n > 1 :
            for i in range(2,n):
                if n % i == 0 :
                    break
            else: 
                print(n)
                
prime(0,100)













