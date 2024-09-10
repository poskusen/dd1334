import random
import numpy as np
import math
from vector import Vector
import matplotlib.pyplot as plt


class Continent:

    def __init__(self, name, mapsize_touple, size, startpos=None, start_vector=None, circle_vector=None):
        self.name = name
        self.start_pos = startpos
        self.mapsize_touple = mapsize_touple
        self.start_vector = start_vector
        self.circle_vector = circle_vectortest_vector_1
        self.size = size
        self.vector_size = 100
        self.vectors = []  # Store all generated vectors for plotting

    def generate_continent(self, size):
        '''Hopefully makes a continent!'''
        self.start_pos = (random.randint(0, self.mapsize_touple[0]/2), random.randint(0, self.mapsize_touple[1]/2))
        next_pos = (self.start_pos[0] + random.uniform(-self.size/self.vector_size, self.size/self.vector_size), self.start_pos[1] + random.uniform(-self.size/self.vector_size, self.size/self.vector_size))
        self.vectors.append(next_pos)
        current_pos = next_pos

        #while self.circle_vector.get_length() < self.size:
            #next_pos = self.generate_new_pos()
            #self.vectors.append(next_pos)
        
        while self.vector[-1] != self.startpos:
            next_pos = self.generate_new_pos(current_pos)
            self.vectors.append(next_pos)
            current_pos = next_pos

    def generate_new_pos(self, current_pos, tendency = None): # fixa så att vinkeln väljs så vi inte går ut
       
        if Vector(current_pos, self.vectors[-1]).get_length() < self.size/100: # If we are close enough, just return the start position
            return self.vectors[-1]
        else:
            length_new_vector = random.random()*(self.size/self.vector_size)
            extended_vector = Vector(self.vectors[-1], self.vectors[-2]).get_extended_vector(length_new_vector)
            random_angle = random.gauss(0,1.5)*math.pi/10-math.pi/30
            
            x_rotated = extended_vector[0][0] + math.cos(random_angle)*(extended_vector[1][0]-extended_vector[0][0])
            y_rotated = extended_vector[0][1] + math.sin(random_angle)*(extended_vector[1][1]-extended_vector[0][1])
            return (self.vectors[-1],(x_rotated, y_rotated))


    def vectorangle(self, firstvectorobject, secondvectorobject):
        '''Calculates the angle between two vectors'''
        u = (firstvectorobject.secondpos[0] - firstvectorobject.firstpos[0],
             firstvectorobject.secondpos[1] - firstvectorobject.firstpos[1])
        v = (secondvectorobject.secondpos[0] - secondvectorobject.firstpos[0],
             secondvectorobject.secondpos[1] - secondvectorobject.firstpos[1])

        dot_product = u[0] * v[0] + u[1] * v[1]
        norm_v = np.linalg.norm(v)
        norm_u = np.linalg.norm(u)

        if norm_u == 0 or norm_v == 0:

            return 0  # To avoid division by zero, we return 0 angle

        cos_theta = dot_product / (norm_u * norm_v)
        cos_theta = max(-1, min(1, cos_theta))  # Clamp value
        angle_radians = math.acos(cos_theta)

        vectorangle = math.degrees(angle_radians)
        return vectorangle

    def plot_vectors(self):
        '''Plot the vectors in 2D space'''
        plt.figure(figsize=(10, 10))
        for start, end in self.vectors:
            plt.plot([start[0], end[0]], [start[1], end[1]], marker='o')

        plt.xlim(0, self.mapsize_touple[0])
        plt.ylim(0, self.mapsize_touple[1])
        plt.title(f'Vectors for {self.name}')
        plt.xlabel('X coordinate')
        plt.ylabel('Y coordinate')
        plt.grid()
        plt.show()


def test():
    kontinenten = Continent("cool", mapsize_touple=(1000, 1000), size = 200)
    kontinenten.generate_continent()
    kontinenten.plot_vectors()  # Call the plotting function


test()
