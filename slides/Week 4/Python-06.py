#!/usr/bin/env python
# coding: utf-8

# ### Python Classes/Objects
# Python is an object oriented programming language.
# 
# Almost everything in Python is an object, with its properties and methods.
# 
# A Class is like an object constructor, or a "blueprint" for creating objects.

# ### Create a Class

# In[ ]:


class MyClass:
    x = 5


# In[ ]:


print(type(MyClass))


# ### Create Object

# In[ ]:


p1 = MyClass()
print(p1.x)


# ### The \_\_init\_\_() Function

# In[ ]:


class Person:
    def __init__(self, name, age=34):
        self.name = name
        self.age = age


# In[ ]:


p1 = Person("John", 36)

print(p1.name)
print(p1.age)


# In[ ]:


p2 = Person('ZhangJian')
print(p2.name)
print(p2.age)


# In[ ]:


print(type(p1))


# In[ ]:


print(type(Person))


# ## Object Methods

# In[ ]:


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printname(CN):
        print(id(CN))
        print("Hello, my name is " + CN.name)
        print("Hello, my age is ", CN.age)

p1 = Person("John", 36)
p1.printname()
print(id(p1))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


p2 = Person("Jack", 35)
p2.printname()


# In[ ]:





# In[ ]:





# In[ ]:


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printname(self):
        print("Hello, my name is " + self.name)
    
    def printname_age(self):
        print("Hello, my name is " + self.name + " and my age is " + str(self.age))
    
    def print_hello(self):
        print(self)
        print('Hello!')

p3 = Person("PKUSZ", 20)
# p3.printname()
p3.printname_age()


# In[ ]:





# In[ ]:


p3.print_hello()


# In[ ]:





# In[ ]:


print(p3)


# In[ ]:


Person.print_hello()


# ### The self Parameter

# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# 
# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

# In[ ]:


class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def printname(abc):
        print("Hello, my name is " + abc.name)

p1 = Person("John", 36)
p1.printname()


# In[ ]:


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printname(self):
        print("Hello, my name is " + self.name)

p1 = Person("John", 36)
p1.printname()
p2 = Person("Jack", 30)
p2.printname()


# ### Modify Object Properties

# In[ ]:





# In[ ]:


print(p1.age)


# In[ ]:





# In[ ]:


p1.age = 40


# In[ ]:


print(p1.age)


# In[ ]:





# ### Delete Object Properties

# In[ ]:


del p1.age


# In[ ]:





# In[ ]:


print(p1.age)


# In[ ]:





# ### Delete Objects

# In[ ]:


del p1


# In[ ]:


print(p1)


# ### The pass Statement

# In[ ]:


class Person:
    pass


# In[ ]:


class Person:


# ### Python Inheritance

# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# 
# Parent class is the class being inherited from, also called base class.
# 
# Child class is the class that inherits from another class, also called derived class.

# In[ ]:


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person("Jian", "Zhang")
x.printname()


# ### Create a Child Class

# In[ ]:


class Student(Person):
    pass


# In[ ]:





# In[ ]:


x = Student("Mike", "Olsen")
x.printname()


# In[ ]:





# In[ ]:





# ### Add the \_\_init\_\_() Function

# In[ ]:


class Student(Person):
    def __init__(self, fname, lname):
        self.firstname = "Dear " + fname
        self.lastname = lname


# In[ ]:





# In[ ]:


x = Student("Mike", "Olsen")
x.printname()


# In[ ]:





# In[ ]:


class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
x.printname()


# In[ ]:





# In[ ]:


class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
        self.firstname = 'Mr. ' + self.firstname 

x = Student("Mike", "Olsen")
x.printname()


# In[ ]:





# ### Use the super() Function

# In[ ]:


class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)


# In[ ]:





# In[ ]:





# In[ ]:


x = Student("Mike", "Olsen")
x.printname()


# In[ ]:





# ### Add Properties

# In[ ]:


class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2019


# In[ ]:





# In[ ]:


x = Student("Mike", "Olsen")
x.printname()
print(x.graduationyear)


# In[ ]:





# In[ ]:


print(x.graduationyear)


# In[ ]:


x2 = Student("San", "Zhang")
x2.printname()


# In[ ]:





# In[ ]:


print(x2.graduationyear)


# In[ ]:





# In[ ]:


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

x = Student("Mike", "Olsen", 2019)


# In[ ]:





# In[ ]:


x.printname()


# In[ ]:





# In[ ]:


print(x.graduationyear)


# In[ ]:





# In[ ]:


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person("Jian", "Zhang")
x.printname()


# In[ ]:





# ### Add Methods

# In[ ]:


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


# In[ ]:





# In[ ]:


x = Student("Mike", "Olsen", 2019)
x.welcome()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ### Python Modules

# What is a Module?
# Consider a module to be the same as a code library.
# 
# A file containing a set of functions you want to include in your application.

# Create a Module

# To create a module just save the code you want in a file with the file extension .py:

# In[ ]:


def greeting(name):
    print("Hello, " + name)


# Save this code in a file named mymodule.py

# ### Use a Module

# In[1]:


import mymodule

mymodule.greeting("PKUSZ")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


import math


# In[2]:


mymodule.welcome()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


mymodule.greeting("PHBS")


# In[ ]:





# Note: When using a function from a module, use the syntax: module_name.function_name.

# ### Variables in Module

# In[ ]:


# Save this code in the file mymodule.py

person1 = {
  "name": "San Zhang",
  "age": 36,
  "country": "China"
}


# In[ ]:


import mymodule

a = mymodule.person1["name"]
print(a)


# In[ ]:


student_num


# In[ ]:


mymodule.student_num = 56


# In[ ]:


mymodule.student_num


# In[ ]:


import mymodule
print(mymodule.student_num)


# ### Naming a Module

# You can name the module file whatever you like, but it must have the file extension .py

# ### Re-naming a Module

# You can create an alias when you import a module, by using the as keyword:

# In[ ]:


import mymodule as mx

a = mx.person1["age"]
print(a)


# In[ ]:





# ### Built-in Modules

# In[ ]:


import platform

x = platform.system()
print(x)


# In[ ]:


import platform

x = dir(platform)
print(x)


# In[ ]:


platform.architecture()


# In[ ]:


import math
print(dir(math))


# In[ ]:


math.pi


# ### Import From Module

# You can choose to import only parts from a module, by using the from keyword.

# In[ ]:


from mymodule import person1

print(person1["age"])


# In[ ]:


print(person1["name"])


# In[ ]:


mymodule.person1["age"]


# In[ ]:


mymodule.greeting("PKUSZ")


# In[ ]:


from mymodule import *


# In[ ]:


greeting("PKUSZ")


# In[ ]:


student_num


# In[ ]:


def greeting(x):
    print(f"Hi {x}, Welcome to Python Class!")


# In[ ]:


greeting("PKUSZ")


# In[ ]:





# In[ ]:


from modules.test1 import person2


# In[ ]:


person2['name']


# In[ ]:


from modules import test1


# In[ ]:


test1.person2


# ### Python Datetime

# In[ ]:


import datetime

x = datetime.datetime.now()
print(x)


# In[ ]:


import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))


# In[ ]:


print(x.strftime("%c"))


# In[ ]:


print(x.strftime("%U"))


# In[ ]:


print(x.strftime("%j"))


# In[ ]:





# In[ ]:


x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)


# In[ ]:


x = abs(-7.25)

print(x)


# In[ ]:


import math

x = math.sqrt(64)

print(x)


# In[ ]:


import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) 
print(y)


# In[ ]:


x = math.pi
print(x)


# In[ ]:





# ### RegEx in Python

# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# 
# RegEx can be used to check if a string contains the specified search pattern.

# In[ ]:


import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)


# In[ ]:


print(x)


# In[ ]:


import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)


# In[ ]:


import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)


# In[ ]:


import re

txt = "The rain in Spain"
x = re.search("rai", txt)

print("The first white-space character is located in position:", x.start())


# In[ ]:


import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)


# In[ ]:


import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)


# In[ ]:


import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())


# 

# ### xlrd Module

# In[ ]:


import xlrd


# In[ ]:


get_ipython().system('pip install xlrd')


# In[ ]:


data = xlrd.open_workbook('H1.xls')


# In[ ]:


sheet1 = data.sheet_by_index(0)


# In[ ]:


print(sheet1)


# In[ ]:


print(sheet1.name, sheet1.nrows, sheet1.ncols)


# In[ ]:


print(sheet1.cell_value(50,2))


# In[ ]:


print(sheet1.cell_value(25,2))


# In[ ]:


print(sheet1.hyperlink_map.get((25,2)))


# In[ ]:


sheet1.hyperlink_map.get((25,2)).url_or_path


# ### xlwt Module

# In[ ]:


get_ipython().system('pip install xlwt')


# In[ ]:


import xlwt


# In[ ]:


workbook = xlwt.Workbook(encoding = 'ascii')


# In[ ]:


worksheet = workbook.add_sheet('NewSheet')


# In[ ]:


worksheet.write(0, 0, label = 'Row 0, Column 0 Value')


# In[ ]:


worksheet.write(1, 0, label = sheet1.cell_value(50,2))


# In[ ]:


workbook.save('New_H1.xls')


# ### webbrowser Module

# In[ ]:


import webbrowser


# In[ ]:


webbrowser.open_new("https://docs.qq.com/doc/DR1BwQWtsWVZIdVdN")


# In[ ]:


webbrowser.open_new("https://docs.qq.com/doc/DUER5cEpkTGJ5bG1x")


# ### Homework

# ### Given H1.xls, extract all the hyperlinks into one column, as illusrated in New_H1.xls.

# In[ ]:




