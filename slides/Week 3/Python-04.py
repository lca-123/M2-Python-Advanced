#!/usr/bin/env python
# coding: utf-8

# ### Syntactic Sugar

# In[ ]:


# 1
a = 1_000_000_00
print(a)
print(type(a))


# In[ ]:





# In[ ]:





# In[ ]:


a = 1_000_100_00.
print(a)
print(type(a))


# In[1]:


# 2
a = 1
b = 2

print(f"a = {a}")
print(f"b = {b}")


a,b = b,a


# In[ ]:





# In[2]:


print(f"a = {a}")
print(f"b = {b}")


# In[ ]:





# In[3]:


# 3
a = 95
if 0 < a < 100:
    print("Good")


# In[ ]:





# In[4]:


# 4

print('_'*50)
print('@'*50)
print('^-^ '*10)


# In[ ]:





# In[5]:


# 5

a = [1,2,3]
b = [3,4,5,6]
print(a+b)


# In[ ]:





# In[6]:


a = (1,2,3)
b = (3,4,5,6)
print(a+b)


# In[ ]:





# In[7]:


a = [1,2,3]
b = (3,4,5,6)
print(a+b)


# In[ ]:





# In[8]:


#6
a = [1,2,3,4,5,6,7]
print(a[:3])


# In[ ]:





# In[ ]:


a = [1,2,3,4,5,6,7]
print(a[2:-2])


# In[ ]:


a = [1,2,3,4,5,6,7]
print(a[1:2])


# In[10]:


#7
x = (1,2,4)
a,b = x[:2]
print(a,b)


# In[ ]:





# In[ ]:





# In[ ]:


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(type(red))


# In[ ]:


fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)


# In[12]:


# 8
a = [1,2,3,4] + [233]
c = [233 for e in a]
print(c)


# In[ ]:





# In[ ]:





# In[ ]:


b = []
for e in a:
    b.append(e + 233)
print(b)


# In[ ]:


a = [1,2,3,4] + 233


# ### Set 

# In[ ]:


# A set is a collection which is unordered, unchangeable*, and unindexed.
# * Note: Set items are unchangeable, but you can remove items and add new items.


# In[1]:


thisset = {"apple", "banana", "cherry"}
print(thisset)


# In[2]:


# Set items are unordered, unchangeable, and do not allow duplicate values.
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)


# In[3]:


# Access Set Items
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


# In[5]:


print(thisset[1])


# In[ ]:





# In[7]:


thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)


# In[ ]:





# In[ ]:





# In[ ]:


# Change Items
# Once a set is created, you cannot change its items, but you can add new items.


# In[8]:


# Add Set Items

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)


# In[ ]:





# In[9]:


# Add Sets
thisset = {"apple", "banana", "cherry", "mango"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)


# In[ ]:





# In[10]:


# Add Any Iterable

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

mylist.extend(thisset)

print(mylist)


# In[11]:


# Remove Item
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)


# In[ ]:





# In[12]:


thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)


# In[ ]:





# In[13]:


# thisset = {"apple", "banana", "cherry"}
thisset = {"cherry", "banana", "apple"}
x = thisset.pop()

print(x)

print(thisset)


# In[ ]:





# In[14]:


thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

a = set()
print(a)


# In[ ]:





# In[15]:


thisset = {"apple", "banana", "cherry"}
print(thisset)
del thisset

print(thisset)


# In[ ]:





# In[16]:


# Loop Sets

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


# In[17]:


len(thisset)


# In[18]:


# Join Two Sets

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
print(set1)


# In[ ]:


set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set2.update(set1)
print(set2)
print(set3)
print(set1)


# In[ ]:


# Keep ONLY the Duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection_update(y)
print(x)
print(z)


# In[19]:


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)
print(x)


# In[ ]:





# In[ ]:


# Keep All, But NOT the Duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)
print(len(x))


# In[ ]:


x = {"apple", "banana", "cherry"}
y = {"google", 12, (1,3)}

z = x.symmetric_difference(y)

print(z)


# In[ ]:


x = {"apple", "banana", "cherry"}
y = {"google", 12, [1,3]}

z = x.symmetric_difference(y)

print(z)


# ### Dictionary

# In[20]:


thisdict = {
 1: "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


# In[ ]:





# In[ ]:


# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.


# In[25]:


# Dictionary Items
thisdict = {
  "brand": "Ford",
  0: "Mustang",
  22: 1964
}
print(thisdict[2])


# In[26]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2090
}
print(thisdict)


# In[27]:


# Dictionary Length
print(len(thisdict))


# In[28]:


# Dictionary Items - Data Types
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
# print(thisdict)
print(thisdict["colors"])


# In[29]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))


# In[30]:


# Accessing Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)


# In[31]:


x = thisdict.get("model")
print(x)


# In[32]:


# Get Keys
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.keys()
print(x)


# In[34]:


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"
# print(car)

print(x) #after the change
print(car)


# In[ ]:





# In[35]:


# Get Values

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change


# In[ ]:





# In[36]:


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change


# In[ ]:





# In[37]:


# Get Items

x = thisdict.items()
print(x)


# In[ ]:





# In[38]:


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change


# In[ ]:





# In[ ]:


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["color"] = "red"

print(x) #after the change


# In[40]:


# Check if Key Exists

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "Ford" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
else:
    print('Not exist')


# In[ ]:


# Change Values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
thisdict["year"] = 2018
print(thisdict)


# In[ ]:


# Update Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)


# In[ ]:


# Adding Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)


# In[ ]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
print(thisdict)


# In[41]:


# Removing Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)


# In[43]:


thisdict = {
  "brand": "Ford",

  "model": "Mustang",
      "year": 1964
    
}
thisdict.popitem()
print(thisdict)


# In[ ]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)


# In[44]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict)


# In[ ]:





# In[ ]:


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.clear()
# print(thisdict)
a = ()
b = []
c = {}
d = set()
print(type(a))
print(type(b))
print(type(c))
print(type(d))


# In[46]:


# Loop Through a Dictionary
thisdict = {
  "Name": "PKUSZ",
  "ID": "001",
  "Year": 2001
}

for x in thisdict:
    print(x)


# In[ ]:





# In[48]:


thisdict = {
  "Name": "PKUSZ",
  "ID": "001",
  "Year": 2001
}
# print(thisdict["Year"])
for x in thisdict:
    print(thisdict[x])


# In[ ]:





# In[ ]:





# In[ ]:


for x in thisdict.values():
    print(x)


# In[ ]:


for x in thisdict.keys():
    print(x)


# In[49]:


thisdict.items()


# In[ ]:





# In[50]:


iter_num = 0
for x, y in thisdict.items():
    print(x, y)
    iter_num = iter_num + 1
    if iter_num >=2:
        break


# In[52]:


# Copy a Dictionary

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict
print(mydict)

mydict["year"]  = 2021
print(mydict)
print(thisdict)
print(id(mydict),id(thisdict))


# In[ ]:





# In[53]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)

mydict["year"]  = 2021
print(mydict)
print(thisdict)
print(id(mydict),id(thisdict))


# In[54]:


# Nested Dictionaries

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily['child1']['name'])


# In[ ]:





# In[ ]:


child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}


# In[ ]:





# In[ ]:





# ## Functions

# In[ ]:


def my_function():
    print("Hello from a function")


# In[ ]:





# In[ ]:


def my_function():
    print("Hello from a function")

my_function()


# ## Arguments (args)

# In[55]:


def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


# In[56]:


def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")


# In[ ]:


def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Emil")


# In[ ]:





# ## Arbitrary Arguments, *args

# In[62]:


def my_function(*kids):
    print(type(kids))
    print(len(kids))
    print("The youngest child is " + kids[1])

my_function("Emil", "Tobias", "Linus", 'Jack', 'xxx')


# ## Keyword Arguments

# In[66]:


def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child3 = "Linus")


# In[ ]:





# In[ ]:





# In[ ]:





# ## Arbitrary Keyword Arguments, **kwargs

# In[69]:


def my_function(**kid):
    print(type(kid))
    print("His last name is " + kid["lname"])

my_function(lname = "Refsnes")


# In[ ]:





# In[ ]:





# In[ ]:





# ### Lambda

# In[ ]:


# lambda arguments : expression


# In[71]:


x = lambda a : a + 10
print(x(10))


# In[ ]:





# In[ ]:





# In[72]:


x = lambda a, b : a * b
print(x(5, 6))


# In[ ]:





# In[73]:


x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


# In[ ]:





# In[76]:


def myfunc(n):
    return lambda a : a * n


# In[ ]:





# In[78]:


mydoubler = myfunc(3)
print(type(mydoubler))
print(mydoubler(11))


# In[ ]:





# In[ ]:





# In[75]:


def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))


# ### Search 

# In[ ]:


def Algorithm1(alist, item):
    pos = 0
    found = False
    while pos < len(alist) and not found:
        print(pos)
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found


# In[ ]:


testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(Algorithm1(testlist, 3))
print(Algorithm1(testlist, 13))


# In[79]:


def Algorithm2(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found


# In[82]:


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(Algorithm2(testlist, 33))


print(Algorithm2(testlist, 17))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


def sequentialSearch(alist, item):
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found


# In[ ]:


def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found


# In[ ]:





# ### Homework 1
# 
# ###### Given two strings s and t, return true if t is an anagram of s, and false otherwise. (Using Dictionary)
# ###### Example :
# ###### Input: s = "anagram", t = "nagaram"
# ###### Output: True
# ###### print(IsAnagram(s,t)) 	

# In[ ]:


def IsAnagram(s,t):
    
    return True or False


# ### Homework 2
# 
# ###### Given a non-negative integer x, compute and return the square root of x.
# 
# ###### Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
# 
# ######  Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.
# 
# ###### Example:
# ###### Input: x = 8
# ###### Output: 2

# In[ ]:


def MySqrt(x):
    
    return xxx

