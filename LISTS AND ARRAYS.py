import numpy as np
import pandas as pd

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

print("List 1:", list1)
print("List 2:", list2)

array1 = np.array(list1)
array2 = np.array(list2)

print("Array 1:", array1)
print("Array 2:", array2)

print("Type of list1:", type(list1))
print("Type of array1:", type(array1))

multiplication = array1 * array2
print("Multiplication of arrays:", multiplication)

division = array1 / array2
print("Division of arrays:", division)

power = np.power(array1, 2)
print("Power of array1:", power)

addition = array1 + array2
print("Addition of Two: array1 + array2 =", addition)

sin_values = np.sin(array1)
print("Sine of array1:", sin_values)

log_values = np.log(array1)
print("Log of array1:", log_values)

log2_values = np.log2(array1)
print("Log2 of array1:", log2_values)

exp_values = np.exp(array1)
print("Exponential of array1:", exp_values)