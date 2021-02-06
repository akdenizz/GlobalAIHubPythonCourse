# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 21:38:30 2021

@author: asus
"""

class Animals():
    
    def __init__(self, name, age, place ):
        self.name = name
        self.age = age
        self.place = place
        
    def showInfo(self):
        print(self.name + " is " + str(self.age) + " years old " + "and it is in " + self.place + " right now ")
    
    
class Dogs(Animals):
    
    def __init__(self, name, age, place, breed):
        super().__init__(name, age, place)
        self.breed = breed
        
    def showBreed(self):
         print(self.name + "'s breed is : " + self.breed)
         
    def showInfo(self):
        print(self.name + " is " + str(self.age) + " years old, " + " its breed is " + self.breed + " and it is in  " + self.place + " right now")

class Cats(Animals):
    
    def __init__(self, name, age, place, breed):
        super().__init__(name, age, place)
        self.breed = breed
        
    def showBreed(self):
         print(self.name + "'s breed is : " + self.breed)
         
    def showInfo(self):
        print(self.name + " is " + str(self.age) + " years old, " + " its breed is " + self.breed + " and it is in  " + self.place + " right now")



dog = Dogs("Bartek", 2, "Lublin, Poland" , "Border Sheepdog")
dog.showInfo()
dog.showBreed()

cat  = Cats("Juliet", 1, "Africa", "Savannah")
cat.showInfo()
    