import random
import numpy as np
import math
from Linked_list import Node
import matplotlib.pyplot as plt

class Continent():

    def __init__(self, name, mapsize_touple, size_continent, start_pos=None, start_vector=None, circle_vector=None):
        self.name = name
        self.mapsize_touple = mapsize_touple
        if start_pos != None:
            self.start_pos = start_pos
            self.start_node = Node(self.start_pos)
            self.vectors = self.start_node
        else:
            #self.start_pos = (random.randint(0, self.mapsize_touple[0]), random.randint(0, self.mapsize_touple[1]))
            self.start_pos = (500,500) # Bättre att generera i mitten och sen flytta hela kontinenten
            self.start_node = Node(self.start_pos)
            self.vectors = self.start_node

        self.circle_vector = (0,0) # Implementera senare
        self.size_continent = size_continent
        self.vector_size = 800*size_continent/mapsize_touple[0] # Fixa så den beror på storleken av kontinenten
    
    def generate(self):
        point = self.start_pos
        next_point = (self.start_pos[0] + random.uniform(-1,1)*self.vector_size, self.start_pos[1] + random.uniform(-1,1)*self.vector_size)
        new_node = Node(next_point)
        self.vectors.add_next(new_node)
        self.vectors = new_node
        
        self.circle_vector = (point, next_point)
        steps_away = 1

        while True: # Byt till kondition sen
            
            point_holder = next_point
            next_point = self.generate_new_point(point, next_point)
            point = point_holder
            self.circle_vector = (self.start_pos, next_point) # Behövs inte
            new_node = Node(next_point)
            self.vectors.add_next(new_node)
            self.vectors = new_node

            steps_away += 1

            if math.sqrt((next_point[0] - self.start_pos[0])**2 + (next_point[1] - self.start_pos[1])**2) < self.vector_size and steps_away > 20:
                
                self.vectors.add_next(self.start_node)
                self.vectors = self.start_node
                break
        self.fix_intersects()            

    def generate_new_point(self, point1, point2):
        length = random.uniform(0, 1) * self.vector_size
        if self.get_length_vector(self.circle_vector)/self.size_continent > 3:
            point1 = self.scale_vector(point2, self.start_pos, self.vector_size)
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

    def fix_intersects(self): # Loppar igenom alla nodsen och kolla om x och y koordinaterna intersectar
        working_node = self.start_node.get_next()
        working_node_next = working_node.get_next()
        
        while working_node_next is not self.start_node:
            node_1 = working_node_next.get_next()
            node_2 = node_1.get_next()
    
            while node_2.get_next() is not self.start_node:
                print('Working node: ' + str(working_node.get_data()))
                print('Working node next: ' + str(working_node_next.get_data()))
                print('node 1: ' + str(node_1.get_data()))
                print('node 2 ' + str(node_2.get_data()))
                print('start_node' + self.start_node.get_data())
                if self.crosses((working_node, working_node_next), (node_1, node_2)):
                    
                    working_node.add_next(node_2)
                    working_node = node_2
                    working_node_next = working_node.get_next()
                    break
                node_1 = node_1.get_next()
                node_2 = node_1.get_next()
            working_node = working_node.get_next()
            working_node_next = working_node.get_next()


    def crosses(self, vector1, vector2):
        (x1, y1) = vector1[0].get_data()
        (x2, y2) = vector1[1].get_data()
        (x3, y3) = vector2[0].get_data()
        (x4, y4) = vector2[1].get_data()
        s_factor = (x1 - x2, y1 - y2)
        t_factor = (x3 - x4, y3 - y4)
        right_side = np.array([x3 - x1, y3 - y1])
        left_side = np.array([[s_factor[0], -t_factor[0]], [s_factor[1], -t_factor[1]]])
        solution = np.linalg.inv(left_side).dot(right_side)
        s = solution[0]
        t = solution[1]
        if 0 <= s <= 1 and 0 <= t <= 1:
            return True
        else:
            return False
        
    def plot(self): #Funkar
        plt.figure(figsize=(10, 10))
        x = []
        y = []
        start_point = self.vectors
        (x_temp, y_temp) = start_point.get_data()
        x.append(x_temp)
        y.append(y_temp)
        start_point = start_point.get_next()
        while start_point is not self.start_node:
            (x_temp, y_temp) = start_point.get_data()
            x.append(x_temp)
            y.append(y_temp)
            start_point = start_point.get_next()
        (x_temp, y_temp) = start_point.get_data()
        x.append(x_temp)
        y.append(y_temp)
        
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
    while True:
        test_cont = Continent('test', (1000,1000), 200)
        test_cont.generate()
        test_cont.plot()

test()