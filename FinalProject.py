# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 22:58:01 2021

@author: asus
"""

class Manager():
    
    def __init__(self, name, lname, age, salary):
        
        self.name = name
        self.last_name = lname
        self.age = age
        self.salary = salary
        self.language = set() # language type shoul be set because sets do not allow duplicates
        
    def getName(self):
        
        print(self.name +  " "  +  self.last_name)
    
    def getAge(self):
        
        print("Age is : " + str(self.age))
        
    def getSalary(self):
        
        print("Salary is: " + str(self.salary))
        
    def addLang(self, new_lang):
        print("New language added..", new_lang)
        self.language.add(new_lang)
        
    def showLang(self):
        print(self.name + " can speaks :")
        for i in self.language:
              print(i)    
        
    def showInfo(self):
        print("{} {} is {} years old".format(self.name, self.last_name,self.age))
        print("He/She can speak :")
        for i in self.language:
              print(i)
              
    
# employees can subclass of managers because they have same feautures and functions
                  
class Employees(Manager):  
    
    def __init__(self,name, lname, age, salary):
        super().__init__(name, lname, age, salary)
        
    def getName(self):
        super().getName()
        
    def getAge(self):
        
        super().getAge()
        
    def getSalary(self):
        
        super().getSalary()
        
    def addLang(self, new_lang):
        super().addLang(new_lang)
    
    def showLang(self):
        super().showLang()
    
    def showInfo(self):
        super().showInfo()
    
 # Create some employees and managers
 
employees1 = Employees("Efe", "Yılmaz", 23, 5500)    
manager1 = Manager("Emre", "Deniz", 45, 7800) 
employees2 = Employees("Helin", "Kalay", 30, 4200)
manager2 = Manager("Mete", "Bilir", 43, 6650) 
employees3 = Employees("Gencay", "Ozen", 28, 5400)
manager3 = Manager("Halil", "Ege", 38, 7655) 
employees4 = Employees("Ayris", "Arslan", 25, 5200)
manager4 = Manager("Arda", "Saygı", 40, 6990) 
employees5 = Employees("Elif", "Ezgi", 26, 4980)

#manager3.showInfo()

# create a dictionary for employees

my_dict = {"Efe" : {"employee": employees1 }, 
           
           "Helin" : {"employee": employees2 },
         
           "Gencay" : {"employee": employees3 },
           
           "Ayris" : {"employee": employees4 },
          
           "Elif" : {"employee": employees5 }
           } 

# to see the languages of all employees in my dictionary ;

for i in my_dict.keys():
    my_dict[i]["employee"].showLang()

# to see the languages of specific employee;

my_dict["Gencay"]["employee"].showLang()

  


  
# add languages to employees objects also we can do the same thing to managers,too

employees1.addLang("English")
employees1.addLang("French")
employees1.addLang("English")
employees1.addLang("Turkish")

employees2.addLang("English")
employees2.addLang("Polish")
employees2.addLang("English")
employees2.addLang("Turkish")

employees3.addLang("English")
employees3.addLang("Arabic")
employees3.addLang("Turkish")

employees4.addLang("Turkish")

employees5.addLang("French")
employees5.addLang("Arabic")
employees5.addLang("Turkish")





 