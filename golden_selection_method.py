#coding=utf-8
import math
import function


#func
def get_x1(A, B, const):
    return A + const * (B - A)

def get_x2(A, B, const):
    return A + B - get_x1(A, B, const)

def golden_selection_method(function_number):
    const = (3 - math.sqrt(5)) / 2
    A = function.intervals[function_number][0]
    B = function.intervals[function_number][1]
    epcila = 0.01
    x1 = get_x1(A, B, const)
    x2 = get_x2(A, B, const)
    lenght = B - A
    iteration_counter = 0
    while (lenght > epcila):
        x1_znach = function.getFunctionValue(x1, function_number)
        x2_zhach = function.getFunctionValue(x2, function_number)
        if x1_znach > x2_zhach:
            A = x1
            x1 = x2
            x2 = get_x2(A, B, const)
        elif x1_znach < x2_zhach:
            B = x2
            x2 = x1
            x1 = get_x1(A, B, const)
        lenght = B - A
        iteration_counter += 1
    print(f'[МЕТОД ЗОЛОТОГО СЕЧЕНИЯ] x1 = {x1}; x2 = {x2}; total_iterations = {iteration_counter}')

