#Write a NumPy program to find the most frequent value in an array x
given below.
a=[1,2,3,4,3,2,4,5,3,3]
import numpy as np
x = np.random.randint(0, 10, 40)
print("Original array:")
print(x)
print("Most frequent value in the above array:")
print(np.bincount(x).argmax())
