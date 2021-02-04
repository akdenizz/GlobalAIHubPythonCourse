# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 22:29:15 2021

@author: asus
"""

def prime():
    
    n = int(input("Please enter a number between 1 and 100:"))
    
    if n > 1 and n < 100 : # the entered number must be between 1 and 100
        for i in range(2,n):
            if n % i == 0: # if n is divisible by any number between 2 and  entered number 
                print(n, "is not a prime number") # it is not a prime number
                break
            else: # if the entered number is not divisible by any number up to itself; also means it can be divisible only 1 and itself. Then,
                print(n, "is a prime number") # it is a prime number
                break
    else:
        print("You entered out of asked interval!!")
        

prime()




# Another version with parameter

def prime(n):
    
    if n > 1 and n < 100 :
        for i in range(2,n):
            if n % i == 0: 
                print(n, "is not a prime number") # it is not a prime number
                break
            else:
                print(n, "is a prime number")
                break
    else:
        print(n, "is not between 1 and 100!")
        
prime(54)
prime(17)
prime(157)