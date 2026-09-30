#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 01:53:29 2026

@author: animeshkakoty
"""

# x = 2               #int
# name = "animesh"    #string
# surname = 'kakoty'   #string

# print(type(2.4))  # float as we have decimals


# is_ready = True  # boolean type

# print(type(x))
# print("type of", type(x))
# print("type of", type(name))

# print('type of', type(is_ready))

# print(f"firstname is {name} and surname is {surname} and is a {is_ready}")
 # control one for commenting all in one click 
 
 
 
 # Control flow 
 
 
# =============================================================================
# grade = 67 
# 
# if grade >= 90:
#     print("A")
# elif grade > 75:
#      print("B")
# elif grade >=40:
#     print("C")
# else:
#     print("fail")
# 
# 
# for i in range(10):
#     print(i)
#     # it will print till 9 
#     
# n = 10 
# 
# while n >= 4:
#     # based on this the ops will run print something then do the ops of n - 2 
#     print("something")
#     # n = n - 2
#     n -=2
# =============================================================================
# =============================================================================
#     two things first is n= -2 we are assinging the value 
#     second n -=2 we are minising 2 from n ; n - 2
# =============================================================================
 


 
# =============================================================================
#           DATA STRUCTURE IN PYTHON
# =============================================================================
 

# # list same as arrays of javascript  => we can change lists 

# lists = ["animesh", "kakoty", 2]
 
# print(lists)

# lists.append("animeshagain") # add a new element at the last

# print(lists)
# # ['animesh', 'kakoty', 2, 'animeshagain']

# print(lists[1], lists[-1])
# # indexing starts from 0, like js ; we have minus indexing also which starts from the last element -> the last element is the first negative one

# print(lists[1:3])
# # same as slicing in js , index before : will print but indexed element after the : wont print 

# print(len(lists)) # len(obj) counting the length same as .length of javascript

# print(len("animesh"))  # 7 will be print as it has 7 letters 



 
#  Tuple : same as data storage like list but we cant modified it like list 

# tuple_name = (2, "animesh")

# print(tuple_name)
 
# point = (3 , 2)

# x_cord, y_cord = point

# print(x_cord)
# print(y_cord) 
# # here we are unpacking things , basically the points giving it a name but one more thing if we have another elememt then we have to define it also , if not it will complain 

# new_tuple = (10, 11, 6) 
 
# x_cord, y_cord, z_cord = new_tuple

# print(x_cord, y_cord, z_cord)

# Dictionary - same like js objects we can store 

# js_object = {"obj_1": 2, "obj_2": 97, "obj_3" : "animesh"}

# print(js_object["obj_3"]) # this is how we extract element in objects or dictionary in python , same big bracket but under it instead of index define the objects assign name

# print(js_object["obj_1"])


# marks_of_animesh = {"qm" : 18, "electro" : 19, "mathsphy" : 6}

# for subs, marks in marks_of_animesh.items():
#     print(subs, "==", marks)
# #  we have to define both the object name and its value inside the dictionary of python then we can run , have to use the .items() function so that each value of that dicto, can be touched without it , it will make no sense 

# # sets in python 

# sets = {"set1", "set2", "set3"}

# print(sets)

# sets.add("animesh")
# print(sets)

# lets define something like functions 

# def kinetic_energy(mass, velocity):
#     return 0.5 * mass * velocity ** 2 

# print(kinetic_energy(2, 12))


# def greetings(name, gret = "good morning"):
#     print(f"{gret} {name}")
    
    
# greetings("animesh") # it will print animesh and then the default variable
# greetings("animesh", "Sexy") # this will print animesh and the new gret value string 


# # one start takes many data and make it tuple and 
# # two star makes any name document 

# def marks_distribution(*scores, **student_name):
#     print("student information", student_name)
    
#     total_marks = sum(scores)
#     print(total_marks)
    
    
# marks_distribution(10, 12, 12, name = "animesh")
    
    

 

# squares = [x ** 2 for x in range(4)]

# print(squares)


#  try catch in python 


# def safe_devide(x , y):
#     try:
#         return x / y 
#     except ZeroDivisionError:
#         print("unable to devide")
#         return None
#     finally:
#         print("devison done")
        
# print(safe_devide(12, 0))



















 
 
 
 
 
 
 