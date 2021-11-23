#coding=utf-8
import math
import function


#func
def getX(A, B, k):
    return (A + k * ((B - A) / 4))

def dichotomy_method_SECOND(function_number):
    epcila = 0.01
    A = function.intervals[function_number][0]
    B = function.intervals[function_number][1]
    x_1_1 = getX(A, B, 1)
    x_2_1 = getX(A, B, 2)
    length = B - A
    iteration_counter = 0
    while (length > epcila):
        x_1 = getX(A, B, 1)
        x_2 = getX(A, B, 2)
        x_3 = getX(A, B, 3)
        f_x1 = function.getFunctionValue(x_1, function_number)
        f_x2 = function.getFunctionValue(x_2, function_number)
        f_x3 = function.getFunctionValue(x_3, function_number)
        if f_x1 <= f_x2:
            B = x_2
            x_2 = x_1
        elif f_x2 <= f_x3:
            A = x_1_1
            B = x_3
        elif f_x2 > f_x3:
            A = x_2_1
            x_2 = x_3
        length = B - A
        iteration_counter += 1
        if iteration_counter > 100:
            break
    print(f"[МЕТОД ДИХОТОМИИ - 2ой вариант NEED TEST] x_min = {x_2}, total iterations = {iteration_counter}")




