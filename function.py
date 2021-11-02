#coding=utf-8
import math

intervals = {1: [-0.6, 1.5], 2: [1.2, 4.0], 3: [-1.3, 1.0], 4: [-1.3, 0.5], 5: [0.2, 0.8]}

def getFunctionValue(x, k):
    if k == 1:
        pass
    elif k == 2:
        return (5 * math.sin(2 * x) + x * x)
    elif k == 3:
        return x**6
    elif k == 4:
        pass
    elif k == 5:
        return x*x + 16/x