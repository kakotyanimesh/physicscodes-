#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 14:41:35 2026

@author: animeshkakoty
"""

import numpy as np 




# A = np.array([1, 2, 3, 4])

# print(A)

# print(A[0])
# print(A[-1])


"""
the python index start from 0 and with -1 it start backwards
    for 1 -> [0]
    for last 4 ---> [-1]
"""

'WE ARE PRITING NUMBERS B/W FIRST AND 2NS '
# print(A[0:2])


Z = np.array([1, 2, 3 ,4 ,5 , 6 , 7 , 8 ,9, 10])


print(Z[1:2])

print(Z[5])


P = np.array([1, 2, 5, 6])

print(P[0:3])

' THE COLUN : THIS SYMBOL THE FIRST ONE IS THE INDEX OF THE ARRAY AND THE sedond number is the index -1'



import matplotlib.pyplot as plt

# plt.plot(Z)


# when we are giving only one varible the matplot lib takes the indexes as the default x axis


# lets do with two variables 

k = np.array([1, 2, 3, 4 , 7, 8])

l = np.array([1, 2, 3, 4 , 5 ,6])

l = np.array([-1, 10, 15, 20, 25, 30])

l = np.array([1, 1.1, 1.2, 1.4, 1.5, 1.7])

# plt.plot(l, k)


# numpy array that runs from -PI to +PI



# linspce -> starting point , last piint and how many ponts i want to plot

X = np.linspace(-np.pi, np.pi, num = 100)


# the first is ploting the X, the second one is colour and the last one is line width for the graph

plt.plot(X, 'r', linewidth = 3)

plt.xlabel("index")
# that is for x axis label
plt.ylabel("X")
# this is for y axis label

plt.title("ANImesh plot")
# this is the plot name



# LETS Plot sin 

y = np.sin(X)

# plt.plot(X, y, 'r', linewidth = 3)

plt.xlabel("X")
plt.ylabel("sin(x)")

plt.title("sin curve")
plt.grid()




# plot the sin consine together

z = np.cos(X)

# plt.plot(X, z, 'r', linewidth = 3)

plt.xlabel("X")
plt.ylabel("sin(x)")

plt.title("sin curve")
plt.grid()


A = np.linspace(-np.pi, np.pi, num = 1000)
B = np.tan(A)

plt.plot(A, B, 'r')
plt.xlabel("X")
plt.ylabel("sin(x)")

plt.title("animesh")
plt.grid()


c = 1 / np.tan(A)

plt.plot(A, c, 'r')
plt.title("animesh cot")
