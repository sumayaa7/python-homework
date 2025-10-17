#1
import numpy as np
lst = [12.23, 13.32, 100, 36.32]
arr = np.array(lst)
print("Original List:", lst)
print("One-dimensional NumPy array:", arr)


#Create 3x3 Matrix (2→10)
matrix = np.arange(2, 11).reshape(3, 3)
print("3x3 Matrix:\n", matrix, "\n")


#Null Vector (10) & Update Sixth Value
vec = np.zeros(10)
print("Original Null Vector:", vec)
vec[6] = 11
print("Updated Vector:", vec, "\n")

#Array from 12 to 38
arr_12_38 = np.arange(12, 38)
print("Array from 12 to 38:", arr_12_38, "\n")

#Convert Array to Float Type
arr_int = np.array([1, 2, 3, 4])
arr_float = arr_int.astype(float)
print("Original array:", arr_int)
print("Converted to float:", arr_float, "\n")

#Celsius to Fahrenheit Conversion
celsius = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])
fahrenheit = (celsius * 9 / 5) + 32
print("Values in Centigrade degrees:", celsius)
print("Values in Fahrenheit degrees:", fahrenheit, "\n")

# Append Values to Array
arr_append = np.array([10, 20, 30])
new_arr = np.append(arr_append, [40, 50, 60, 70, 80, 90])
print("Original array:", arr_append)
print("After append:", new_arr, "\n")

#  Array Statistical Functions
rand_arr = np.random.rand(10)
print("Array:", rand_arr)
print("Mean:", np.mean(rand_arr))
print("Median:", np.median(rand_arr))
print("Standard deviation:", np.std(rand_arr), "\n")

#  Find min and max in 10x10 array
arr_10x10 = np.random.rand(10, 10)
print("Min value:", arr_10x10.min())
print("Max value:", arr_10x10.max(), "\n")

#  Create a 3x3x3 array with random values
arr_3x3x3 = np.random.rand(3, 3, 3)
print("3x3x3 Random Array:\n", arr_3x3x3)
