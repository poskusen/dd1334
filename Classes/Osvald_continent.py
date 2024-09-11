import random
import numpy as np
import math
from vector import Vector
import matplotlib.pyplot as plt

class Continent():

    def __init__(self, name, mapsize_touple, size_continent, start_pos=None, start_vector=None, circle_vector=None):
        self.name = name
        self.mapsize_touple = mapsize_touple
        if start_pos != None:
            self.start_pos = start_pos
            self.vectors = []
            self.vectors.append(start_pos)
        else:
            #self.start_pos = (random.randint(0, self.mapsize_touple[0]), random.randint(0, self.mapsize_touple[1]))
            self.start_pos = (500,500) # Bättre att generera i mitten och sen flytta hela kontinenten
            self.vectors = []
            self.vectors.append(self.start_pos)
        self.circle_vector = (0,0) # Implementera senare
        self.size_continent = size_continent
        self.vector_size = 50 # Fixa så den beror på storleken av kontinenten
    
    def generate(self):
        point = self.start_pos
        next_point = (self.start_pos[0] + random.uniform(-1,1)*self.vector_size, self.start_pos[1] + random.uniform(-1,1)*self.vector_size)
        self.vectors.append(next_point)
        self.circle_vector = (point, next_point)
        steps_away = 1

        for i in range(50): # Byt till kondition sen
            point_holder = next_point
            next_point = self.generate_new_point(point, next_point)
            point = point_holder
            self.circle_vector = (point, next_point)
            self.vectors.append(next_point)
            steps_away += 1

            if math.sqrt((next_point[0] - self.start_pos[0])**2 + (next_point[1] - self.start_pos[1])**2) < self.vector_size*2 and steps_away > 6:
                self.vectors.append(self.start_pos)
                break
            

    def generate_new_point(self, point1, point2):
        length = random.uniform(1, 1) * self.vector_size
        if self.get_length_vector(self.circle_vector)/self.mapsize_touple[0] > 0.5:
            mu = math.pi*(1.2)
        else:
            mu = math.pi*(1.1)
        angle = random.gauss(math.pi*(1.1), math.pi/10) # Skapa en slumpmässig vinkel
        return self.rotate_vector(point1, point2, length, angle)

    def rotate_vector(self, point1, point2, length, angle): #point 1 and 2 är den senaste vektorn, alltså därifrån vi ska generera från
        fx = point2[0]
        fy = point2[1]
        x = point1[0]
        y = point1[1]

        x_rot = ((x - fx) * math.cos(angle)) - ((y - fy) * math.sin(angle)) + fx #rotatera kring fx och fy
        y_rot = ((x - fx) * math.sin(angle)) + ((y - fy) * math.cos(angle)) + fy

        # Skala vektorn
        dx = fx - x_rot
        dy = fy - y_rot
        curr_len = math.sqrt(dx**2 + dy**2)
        scale_factor = length/curr_len
        x_new = scale_factor*dx + x_rot
        y_new = scale_factor*dy + y_rot
        #fx fy fast punkt
        return (x_rot, y_rot)

    def closest_wall(point): #Kollar vilken riktning så vi inte direkt åker in i vägg
        pass

    def plot(self): #Funkar
        plt.figure(figsize=(10, 10))
        x, y = zip(*self.vectors)
        plt.plot(x, y, marker='o', linestyle='-')
        plt.xlim(0, self.mapsize_touple[0])
        plt.ylim(0, self.mapsize_touple[1])
        plt.title(f'Vectors for {self.name}')
        plt.xlabel('X coordinate')
        plt.ylabel('Y coordinate')
        plt.grid()
        plt.show()
    
    def get_length_vector(self, vector):
        return math.sqrt((vector[0][0] - vector[1][0])**2 + (vector[0][1] - vector[1][1])**2)

def test():
    test_cont = Continent('test', (1000,1000), 100)
    test_cont.generate()
    test_cont.plot()

test()