#coding=utf-8
import math

intervals = {1: [-0.6, 1.5], 2: [1.2, 4.0], 3: [-1.3, 1.0], 4: [-1.3, 0.5], 5: [0.2, 0.8]}

def getFunctionValue(x, k):
    if k == 1:
        if x <= 1:
            return x*x
        elif x > 1:
            return 2 * x - 1
    elif k == 2:
        return (5 * math.sin(2 * x) + x * x)
    elif k == 3:
        return x**6
    elif k == 4:
        if x < 0:
            return -2 * x
        elif x >= 0:
            return 87 * x
    elif k == 5:
        return x*x + 16/x