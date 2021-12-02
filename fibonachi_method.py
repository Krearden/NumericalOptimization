#coding=utf-8
import math

#variables
import function


#func
def getFibonacchi_number(k):
    return int(1/math.sqrt(5) * ((((1 + math.sqrt(5)) / 2) ** k) - (((1 - math.sqrt(5)) / 2) ** k)))

def fibonacci_method(function_number):
    A = function.intervals[function_number][0]
    B = function.intervals[function_number][1]
    epcila = 0.01
    n = math.log(((math.sqrt(5) * (B - A)) / epcila), math.e) / math.log(((1 + math.sqrt(5)) / 2), math.e) - 3
    n = int(n)
    for i in range(n):
        x_1 = A + (getFibonacchi_number(n + 1 - i) / getFibonacchi_number(n + 3 - i)) * (B - A)
        x_2 = A + (getFibonacchi_number(n + 2 - i) / getFibonacchi_number(n + 3 - i)) * (B - A)
        f_x1 = function.getFunctionValue(x_1, function_number)
        f_x2 = function.getFunctionValue(x_2, function_number)
        if f_x1 <= f_x2:
            B = x_2
            x_2 = x_1
            x_1 = A + B - x_1
        elif f_x1 > f_x2:
            A = x_1
            x_1 = x_2
            x_2 = A + B - x_2
    print(f"[МЕТОД ФИБОНАЧЧИ] x_1 = {x_1}, x_2 = {x_2}, x_min = {(A + B) / 2}, total iterations = {n}")
