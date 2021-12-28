#coding=utf-8

import matplotlib.pyplot as plt

#functions
def getFunctionValue(x):
    return x ** 4 + 5 * x ** 3 + 4 * x ** 2 - 4 * x + 1


#main
greySegments = {
    (0, 0, 0, 0): -4,
    (0, 0, 0, 1): -3.6875,
    (0, 0, 1, 1): -3.375,
    (0, 0, 1, 0): -3.0625,
    (0, 1, 1, 0): -2.75,
    (0, 1, 1, 1): -2.4375,
    (0, 1, 0, 1): -2.125,
    (0, 1, 0, 0): -1.8125,
    (1, 1, 0, 0): -1.5,
    (1, 1, 0, 1): -1.1875,
    (1, 1, 1, 1): -0.875,
    (1, 1, 1, 0): -0.5625,
    (1, 0, 1, 0): -0.25,
    (1, 0, 1, 1): 0.0625,
    (1, 0, 0, 1): 0.375,
    (1, 0, 0, 0): 0.6875

}

binarySegments = {
    (0, 0, 0, 0): -4,
    (0, 0, 0, 1): -3.6875,
    (0, 0, 1, 0): -3.0625,
    (0, 0, 1, 1): -3.375,
    (0, 1, 0, 0): -1.8125,
    (0, 1, 0, 1): -2.125,
    (0, 1, 1, 0): -2.75,
    (0, 1, 1, 1): -2.4375,
    (1, 0, 0, 0): 0.6875,
    (1, 0, 0, 1): 0.375,
    (1, 0, 1, 0): -0.25,
    (1, 0, 1, 1): 0.0625,
    (1, 1, 0, 0): -1.5,
    (1, 1, 0, 1): -1.1875,
    (1, 1, 1, 0): -0.5625,
    (1, 1, 1, 1): -0.875
}

grey_values = list(greySegments.values())
binary_values = list(binarySegments.values())

f_x_values = []

for i in range(len(grey_values)):
    f_x_values.append(getFunctionValue(grey_values[i]))
plt.plot(grey_values, f_x_values, "go-")
plt.title('График зависимости f(x) от кода Грея')
plt.savefig('grey.png', dpi=500, bbox_inches='tight')
plt.close()

f_x_values = []
for i in range(len(binary_values)):
    f_x_values.append(getFunctionValue(binary_values[i]))
plt.plot(grey_values, f_x_values, "b*-")
plt.title('График зависимости f(x) от двоичного кода')
plt.savefig('binary.png', dpi=500, bbox_inches='tight')
plt.close()

plt.show()


