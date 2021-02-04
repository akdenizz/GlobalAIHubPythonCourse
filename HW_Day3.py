# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 20:56:06 2021

@author: asus
"""

user_name = "Akdenizz"
password = "drowssapgnorw"


User_Name = input("Please enter your username : ")
Password = input("Please enter your password : ")

if User_Name == user_name and Password != password:
    print("Wrong password!")
elif User_Name != user_name and Password == password:
    print("Wrong password!")
elif User_Name != user_name and Password != password:
    print("User does not exist!!")
else:
    print("Logged in...")

# Extra (Using Dictionary)

#keys as user_name and values as password

users = {"Fatih":"hitaf", "Eren":"nere", "Omer":"remo", "Enes":"sene", "Daghan":"nahgad"}


User_Name = input("Please enter your username : ")
Password = input("Please enter your password : ")

#check the entered user name is in the users dictionary or not

if User_Name in users.keys(): # if the  entered user name exists in dict 
    user_name = User_Name  #  assign the user name as user_name
    password = users.get(user_name) # assign its value as the password
else:
    print("User does not exist!!")    

#check the login

if User_Name == user_name and Password != password:
    print("Wrong password!")
elif User_Name != user_name and Password == password:
    print("Wrong password!")
elif User_Name != user_name and Password != password:
    print("User does not exist!!")
else:
    print("Logged in...")
