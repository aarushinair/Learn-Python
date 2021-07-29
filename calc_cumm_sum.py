#Write a NumPy program to calculate cumulative sum of the elements along a given axis, 
#sum over rows for each of the 3 columns and sum over columns for each of the 2 rows of a given 3x3 array.
import numpy as np
x = np.array([[1,2,3], [4,5,6]])
print("Original array: ")
print(x)
print("Cumulative sum of the elements along a given axis:")
r = np.cumsum(x)
print(r)
print("\nSum over rows for each of the 3 columns:")
r = np.cumsum(x,axis=0) 
print(r)
print("\nSum over columns for each of the 2 rows:")
r = np.cumsum(x,axis=1) 
print(r)
