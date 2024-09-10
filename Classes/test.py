import random
import numpy as np
import math
from vector import Vector
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 10))
test_vector_2 = ((200,200),(300,300))
test_vector_1 = ((100,100),(200,200))
angle = math.pi

def rotate_vector(point1, point2):
    pass

for i in range(0,50):
    angle = random.gauss(0,1.5)*math.pi/10-math.pi/30
    x_rotated = test_vector_2[0][0] + math.cos(angle)*(test_vector_2[1][0]-test_vector_2[0][0])
    y_rotated = test_vector_2[0][1] + math.sin(angle)*(test_vector_2[1][1]-test_vector_2[0][1])
    new_vector = (test_vector_1[1],(x_rotated, y_rotated))
    plt.plot([new_vector[0][0], new_vector[1][0]], [new_vector[0][1], new_vector[1][1]], marker='o')
    
print(new_vector)

plt.plot([test_vector_1[0][0], test_vector_1[1][0]], [test_vector_1[0][1], test_vector_1[1][1]], marker='o')
#plt.plot([test_vector_2[0][0], test_vector_2[1][0]], [test_vector_2[0][1], test_vector_2[1][1]], marker='o')
plt.plot([new_vector[0][0], new_vector[1][0]], [new_vector[0][1], new_vector[1][1]], marker='o')
#plt.plot([start[0], end[0]], [start[1], end[1]], marker='o')

plt.xlim(0, 1000)
plt.ylim(0, 1000)
plt.title('test')
plt.xlabel('X coordinate')
plt.ylabel('Y coordinate')
plt.grid()
plt.show()