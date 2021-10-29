#coding=utf-8
import math

#variables for work
epcila = 0.01
delta = epcila/2 - 0.0001
A = 1.2
B = 4.0

#Main part of the script
def getFunctionValue(x):
    return (5 * math.sin(2 * x) + x*x)

length = B - A
iteration_counter = 0
while (length > epcila):
    center = (A + B)/2
    x1 = center - delta
    x2 = center + delta
    x1_func_val = getFunctionValue(x1)
    x2_func_val = getFunctionValue(x2)
    if x1_func_val < x2_func_val:
        B = x2
    elif x2_func_val < x1_func_val:
        A = x1
    length = B - A
    iteration_counter += 1
    print(f'x1 = {x1}; x2 = {x2}; iteration_number = {iteration_counter}')