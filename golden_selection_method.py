#coding=utf-8
import math
import function


#func
def golden_selection_method(function_number):
    const = (3 - math.sqrt(5)) / 2
    A = function.intervals[function_number][0]
    B = function.intervals[function_number][1]
    epcila = 0.01
    x1 = A + const * (B - A)
    x2 = A + B - x1
    length = B - A
    iteration_counter = 0
    while (length > epcila):
        f_x1 = function.getFunctionValue(x1, function_number)
        f_x2 = function.getFunctionValue(x2, function_number)
        if f_x1 <= f_x2:
            B = x2
            x2 = x1
            x1 = A + B - x1
        elif f_x1 > f_x2:
            A = x1
            x1 = x2
            x2 = A + B - x2
        length = B - A
        iteration_counter += 1
    print(f'[МЕТОД ЗОЛОТОГО СЕЧЕНИЯ] x1 = {x1}; x2 = {x2}; x_min = {(x1 + x2) / 2}, total_iterations = {iteration_counter}')