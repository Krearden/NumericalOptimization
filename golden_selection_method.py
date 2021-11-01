#coding=utf-8
import math

#variables
const = (3 - math.sqrt(5)) / 2
A = 1.2
B = 4.0
epcila = 0.01


#func
def get_x1(A, B, const):
    return A + const * (B - A)

def get_x2(A, B, const):
    return A + B - get_x1(A, B, const)

def getFunctionValue(x):
    return (5 * math.sin(2 * x) + x*x)


#main
x1 = get_x1(A, B, const)
x2 = get_x2(A, B, const)
x1_znach = getFunctionValue(x1)
x2_zhach = getFunctionValue(x2)
lenght = B - A
iteration_counter = 0
while (lenght > epcila):
    x1_znach = getFunctionValue(x1)
    x2_zhach = getFunctionValue(x2)
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
    print(f'x1 = {x1}; x2 = {x2}; iteration_number = {iteration_counter}')