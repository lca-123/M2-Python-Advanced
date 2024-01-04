#!/usr/bin/env python
# coding: utf-8

# ### Search 

# In[ ]:


def Algorithm1(alist, item):
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found


# In[ ]:


testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(Algorithm1(testlist, 3))
print(Algorithm1(testlist, 13))


# In[ ]:


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


# In[ ]:


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(Algorithm2(testlist, 3))
print(Algorithm2(testlist, 2))


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





# ### Search Efficiency

# In[ ]:


import numpy
import time

r = numpy.random.randint(0, 9, 5)
print(list(r))


# In[ ]:





# In[ ]:


import numpy
import time

l = []
dl = dict()

r = numpy.random.randint(0, 100000000, 10_0000)


total_num = 10000
search_range = 1000

for i in range(0, total_num):
    l.append(r[i])
    dl.setdefault(r[i], 1)


# In[ ]:


print(len(l), len(dl))


# In[ ]:


start = time.perf_counter()
for i in range(search_range):
    t = i in dl
end = time.perf_counter()

print("time of dict is %.5f" % float(end-start))

start = time.perf_counter()
for i in range(search_range):
    t = i in l
end = time.perf_counter()
print("time of list is %.5f" % float(end-start))


# In[ ]:





# ## Functions

# In[ ]:


def my_function():
    print("Hello from a function")

my_function()


# ## Arguments (args)

# In[ ]:


def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Emil", "Refsnes")


# ## Arbitrary Arguments, *args

# In[ ]:


def my_function(*kids):
    print(len(kids))
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


# In[ ]:


def my_function(*kids):
    print(type(kids))
    for k in range(len(kids)):
        print(kids[k])

my_function("Emil", "Tobias", "Linus")


# ## Keyword Arguments

# In[ ]:


def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


# ## Arbitrary Keyword Arguments, **kwargs

# In[ ]:


def my_function(**kid):
    print(type(kid))
    print("His last name is " + kid["lname"])

my_function(fname = "Refsnes", lname = "Zhang")


# In[ ]:


def my_function(**kid):
    for k in kid:
        print(kid[k])

my_function(fname = "Refsnes", lname = "Zhang")


# ## Default Parameter Value

# In[ ]:


def my_function(country="China", age = 18):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function(age = 20)


# ## Passing a List as an Argument

# In[ ]:


def my_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)


# ## Return Values

# In[ ]:


def my_function(x):
    return 5 * x
a = my_function(3)
print(a)
print(my_function(5))
print(my_function(9))


# ## The pass Statement

# In[ ]:


def myfunction():


# In[ ]:


def myfunction():
    pass


# ### Annotations

# In[ ]:


def twoSum(num1: int, num2: int=100) -> int:
    sum = num1 + num2
    return sum


# In[ ]:


a = twoSum(1)
print(a)


# In[ ]:


a = twoSum(1.1, 2)
print(a)


# In[ ]:


def twoSum2(num1, num2):
    sum = num1 + num2
    return sum

a = twoSum2(1.0)
print(a)


# In[ ]:


print(twoSum.__annotations__)
print(twoSum2.__annotations__)


# In[ ]:





# ## Scope

# ### Local Scope

# In[1]:


def myfunc():
    x = 300
    print(x)

myfunc()


# In[4]:


def myfunc():
    x = 300
    print(x)

myfunc()

print(x)


# In[ ]:





# In[3]:


print(x)


# In[8]:


x = 200

def myfunc():
    x = 300
    def myinnerfunc():
        global x
        x = 400
    myinnerfunc()
    print(x)

myfunc()
print(x)


# In[ ]:





# In[9]:


def myfunc():
    x = 300
    y = 200
    def myinnerfunc():
        print(x + y)
    myinnerfunc()

myfunc()


# ## Global Scope

# In[10]:


x = 300

def myfunc():
    print(x)

myfunc()

print(x)


# In[ ]:


x = 300

def myfunc():
    x = 200
    print(x)

myfunc()

print(x)


# ## Global Keyword

# In[ ]:


x = 200

def myfunc():
    global x
    x = 300

myfunc()

print(x)


# In[ ]:


x = 300

def myfunc():
    global x
    x = 200

myfunc()

print(x)


# In[ ]:





# In[ ]:





# In[ ]:





# ## Recursion

# ### Once upon a time, there was a mountain. 
# ### There was a temple in the mountain. 
# ### There was a monk telling stories in the temple:

# In[ ]:





# In[ ]:





# In[11]:


def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
#         print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(5) 5 + 4 + 3 + 2 + 1 


# ### Homework1

# ### A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# ### The robot can only move either down or right at any point in time. 
# ### The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# ### How many possible unique paths are there?

# In[ ]:


# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down


# In[ ]:


def uniquePaths(m, n):
    pass
    return


# In[ ]:





# In[ ]:





# ### Homework 2

# ### Given an integer array nums, return the length of the longest strictly increasing subsequence.
# ### A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. 
# ### For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

# In[ ]:


# Example 1:
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
    
# Example 2:
# Input: nums = [0,1,0,3,2,3]
# Output: 4


# In[ ]:


def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    return 


# In[ ]:




