#Write a NumPy program to create a 10x10 matrix, in which the elements on the borders will be equal to 1, and inside 0.
import numpy as np
x = np.ones((10, 10))
x[1:-1, 1:-1] = 0
print(x)
