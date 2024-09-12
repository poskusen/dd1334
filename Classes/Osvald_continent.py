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
        self.vector_size = 800*size_continent/mapsize_touple[0] # Fixa så den beror på storleken av kontinenten
    
    def generate(self):
        point = self.start_pos
        next_point = (self.start_pos[0] + random.uniform(-1,1)*self.vector_size, self.start_pos[1] + random.uniform(-1,1)*self.vector_size)
        self.vectors.append(next_point)
        self.circle_vector = (point, next_point)
        steps_away = 1

        while True: # Byt till kondition sen
            point_holder = next_point
            next_point = self.generate_new_point(point, next_point)
            point = point_holder
            self.circle_vector = (self.start_pos, next_point) # Behövs inte
            self.vectors.append(next_point)
            steps_away += 1

            if math.sqrt((next_point[0] - self.start_pos[0])**2 + (next_point[1] - self.start_pos[1])**2) < self.vector_size and steps_away > 10:
                self.vectors.append(self.start_pos)
                break
            

    def generate_new_point(self, point1, point2):
        length = random.uniform(0, 1) * self.vector_size
        if self.get_length_vector(self.circle_vector)/self.size_continent > 3:
            point1 = self.scale_vector(point2, self.start_pos, self.vector_size)
            print('nu')
            mu = -math.pi*0.3
        else:
            mu = math.pi*(1.1)
        angle = random.gauss(mu, math.pi/10) # Skapa en slumpmässig vinkel, pi är rakt framåt
        return self.rotate_vector(point1, point2, length, angle)

    def rotate_vector(self, point1, point2, length, angle): #point 1 and 2 är den senaste vektorn, alltså därifrån vi ska generera från
        '''Roterar vektor point1, point2 med angle'''
        fx = point2[0]
        fy = point2[1]
        x = point1[0]
        y = point1[1]

        x_rot = ((x - fx) * math.cos(angle)) - ((y - fy) * math.sin(angle)) + fx #rotatera kring fx och fy
        y_rot = ((x - fx) * math.sin(angle)) + ((y - fy) * math.cos(angle)) + fy

        # Skala vektorn
        return self.scale_vector(point2, (x_rot, y_rot), length)
    
    def scale_vector(self, point1, point2, length):
        ''' Returnerar en punkt, vektorn blir startpunkten till den punkten'''
        fx = point1[0]
        fy = point1[1]
        x_rot = point2[0]
        y_rot = point2[1]
        dx = fx - x_rot
        dy = fy - y_rot
        curr_len = math.sqrt(dx**2 + dy**2)

        scale_factor = length/curr_len
        x_new = scale_factor*(x_rot - fx)
        y_new = scale_factor*(y_rot - fy)

        #fx fy fast punkt
        return (x_new + fx, y_new + fy)

    def angle_vectors(self, vector1, vector2):
        dx1 = vector1[1][0] - vector1[0][0]
        dy1 = vector1[1][1] - vector1[0][1]
        dx2 = vector2[1][0] - vector2[0][0]
        dy2 = vector2[1][1] - vector2[0][1]

        dot_product = dx1*dx2 + dy2*dy1
        length_1 = self.get_length_vector(vector1)
        length_2 = self.get_length_vector(vector2)
        return math.acos(dot_product/(length_1*length_2))

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
    for i in range(10):
        test_cont = Continent('test', (1000,1000), 100)
        test_cont.generate()
        test_cont.plot()

test()