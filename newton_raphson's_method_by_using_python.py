# -*- coding: utf-8 -*-
"""Newton Raphson's Method by using python

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Su2-nj7nn3Jc4n3m9b354l0bGDF3rY7z
"""

## Finding the square root of a number using newton raphsons method

#x**2=N
#f(x)=x^2-N=0
#f_dash_x(2*x)

def f_x(x,N):
  return x**2-N
def f_dash_x(x):
  return(2*x)

N=100
x_=2
for repeat in range(1000):
  x_=x_-f_x(x_,N)/f_dash_x(x_)

x_

#2
def f_x(x,N):
  return x**2-N
def f_dash_x(x):
  return(2*x)

N=625
x_=2
for repeat in range(100):
  x_=x_-f_x(x_,N)/f_dash_x(x_)

x_

#lets check 
N**0.5

