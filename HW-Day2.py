# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 15:53:21 2021

@author: asus
"""


"""
1)
Create a list 
Swap the second half of the list with the first half of the list 
Print this list on the screen

"""

my_list = list(range(10)) # create a list which has 10 elements 

x = my_list[:5] # hold the first half element of the list in a variable called x 

my_list[:5] = my_list[5:] # replace the first half  with the last half of the list

my_list[5:] = x # replace the last half element with x which is the value of first half at the beginning

print(my_list) # print the list

"""
2)
Ask the user to input a single digit integer to a variable 'n'
Print out all of the even numbers from 0 to n (including n)

"""

n = int(input("Please enter a single digit integer: ")) #the user inputs the integer number

while  n<0 or n>=10 : # while the entered number is not single digit ,
    
    print("That is not single digit!!!") #print a warning.
    
    n = int(input("please enter a single digit integer: ")) # ask the user to input a number until  the condition of while statemnet is not true
    
    break

even_numbers = [ i for i in range(n+1) if i % 2 ==  0]  # assign a list that the even numbers from 0 to n (including n)
   
print(even_numbers) #print out the list
