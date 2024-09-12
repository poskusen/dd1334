import random
import numpy as np
import math
from vector import Vector
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 10))
test_vector_2 = ((200,200),(300,300))
test_vector_1 = ((100,100),(200,200))
length = 500
angle = math.pi

start_x = test_vector_1[0][0]
start_y = test_vector_1[0][1]
end_x = test_vector_1[1][0]
end_y = test_vector_1[1][1]

current_length = math.sqrt((start_x-end_x)**2 + (start_y - end_y)**2)

scale_factor = length/current_length
print(scale_factor)
x_l = scale_factor*(end_x - start_x)
y_l = scale_factor*(end_y - start_y)


longer_vector = ((start_x, start_y), (x_l, y_l))
def rotate_vector(point1, point2):
    pass





plt.plot([test_vector_1[0][0], test_vector_1[1][0]], [test_vector_1[0][1], test_vector_1[1][1]], marker='o')
plt.plot([longer_vector[0][0], longer_vector[1][0]], [longer_vector[0][1], longer_vector[1][1]], marker='o')
#plt.plot([new_vector[0][0], new_vector[1][0]], [new_vector[0][1], new_vector[1][1]], marker='o')
#plt.plot([start[0], end[0]], [start[1], end[1]], marker='o')

plt.xlim(0, 1000)
plt.ylim(0, 1000)
plt.title('test')
plt.xlabel('X coordinate')
plt.ylabel('Y coordinate')
plt.grid()
plt.show()