#coding=utf-8
import math
import function


#func
def bruteforce_method(function_number):
    A = function.intervals[function_number][0]
    B = function.intervals[function_number][1]
    length = B - A
    n = length / 0.01
    n = int(n)
    minimum_value = math.inf
    minimum_x = None
    for i in range(n):
        X_i = A + i * (length / n)
        value_of_X_i = function.getFunctionValue(X_i, function_number)
        if value_of_X_i < minimum_value:
            minimum_value = value_of_X_i
            minimum_x = X_i
    print(f'[МЕТОД ПЕРЕБОРА] x_min = {minimum_x}, total iterations = {n}')

