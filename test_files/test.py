import numpy as np

#define left-hand side of equation
left_side = np.array([[5, 4], [2, 6]])

#define right-hand side of equation
right_side = np.array([35, 36])

#solve for x and y
a = np.linalg.inv(left_side).dot(right_side)

print(a[1])
