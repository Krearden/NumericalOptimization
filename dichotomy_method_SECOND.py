#coding=utf-8
import math
import function


#func
def getX(A, B, k):
    return (A + k * ((B - A) / 4))


#variables
epcila = 0.01
A = -1.3
B = 1.0
length = B - A


#main
x_1 = getX(A, B, 1)
x_2 = getX(A, B, 2)
x_3 = getX(A, B, 3)
x_1_copy = x_1
x_2_copy = x_2
while (length >= epcila):
    f_x1 = function.getFunctionValue(x_1, 3)
    f_x2 = function.getFunctionValue(x_2, 3)
    f_x3 = function.getFunctionValue(x_3, 3)
    if f_x1 <= f_x2:
        print(1)
        B = x_2
        x_2 = x_1
    elif f_x2 <= f_x3:
        print(2)
        A = x_1_copy
        B = x_3
    elif f_x2 > f_x3:
        print(3)
        A = x_2_copy
        x_2 = x_3
    length = B - A
    print(x_2)


