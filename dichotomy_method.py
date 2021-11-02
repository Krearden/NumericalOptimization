#coding=utf-8
import math
import function


#func
def getFunctionValue(x):
    return (5 * math.sin(2 * x) + x*x)

def dichotomy_method(function_number):
    epcila = 0.01
    delta = epcila / 2 - 10 ** (-5)
    A = function.intervals[function_number][0]
    B = function.intervals[function_number][1]
    length = B - A
    iteration_counter = 0
    while (length > epcila):
        center = (A + B) / 2
        x1 = center - delta
        x2 = center + delta
        x1_func_val = function.getFunctionValue(x1, function_number)
        x2_func_val = function.getFunctionValue(x2, function_number)
        if x1_func_val <= x2_func_val:
            B = x2
        elif x2_func_val < x1_func_val:
            A = x1
        length = B - A
        iteration_counter += 1
    print(f'x1 = {x1}; x2 = {x2}; total_iterations = {iteration_counter}')

