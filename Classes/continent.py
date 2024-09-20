import random
import numpy as np
import math
from river import River
from mountain import Mountain_chain
from mountain import Mountain
from village import Village
#from roads import Road
from city import city

import matplotlib.pyplot as plt


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def add_next(self, Node):
        self.next = Node

    def get_next(self):
        return self.next

    def get_data(self):
        return self.data

    def leads_to_end(self, end_node):
        max_iteration = 1000
        iterations = 0
        node = self.get_next()
        while node.get_data() is not end_node and iterations < max_iteration:
            iterations += 1
            node = node.get_next()
        if node.get_data() is end_node:
            return True
        else:
            return False


class Continent():
    def __init__(self, mapsize_touple, size_continent, start_pos=None, start_vector=None, circle_vector=None,
                 name='None'):
        self.extreme_point = None
        self.name = name
        self.mapsize_touple = mapsize_touple
        if start_pos != None:
            self.start_pos = start_pos
            self.start_node = Node(self.start_pos)
            self.vectors = self.start_node
        else:
            self.start_pos = (500, 500)  # Start position
            self.start_node = Node(self.start_pos)
            self.vectors = self.start_node

        self.circle_vector = (0, 0)  # Implement later
        self.size_continent = size_continent
        self.vector_size = 500 * size_continent / mapsize_touple[0]

        self.points_list = []  # Initialize points_list here

    def generate(self):
        point = self.start_pos
        next_point = (self.start_pos[0] + random.uniform(-1, 1) * self.vector_size,
                      self.start_pos[1] + random.uniform(-1, 1) * self.vector_size)
        new_node = Node(next_point)
        self.start_node.add_next(new_node)
        self.vectors = new_node

        self.circle_vector = (point, next_point)
        steps_away = 1

        while True:  

            point_holder = next_point
            next_point = self.generate_new_point(point, next_point)
            point = point_holder
            self.circle_vector = (self.start_pos, next_point)  
            new_node = Node(next_point)
            self.vectors.add_next(new_node)
            self.vectors = new_node

            steps_away += 1

            if math.sqrt((next_point[0] - self.start_pos[0]) ** 2 + (
                    next_point[1] - self.start_pos[1]) ** 2) < self.vector_size and steps_away > 20:
                self.vectors.add_next(self.start_node)
                self.vectors = self.start_node
                break
        # if not self.fix_intersects():
        # self.generate()
        while self.intersects_exists():
            self.fix_intersects()

        self.extreme_point = self.get_extreme_points()
        print(self.get_size())

    def generate_content(self):
        self.points_list = self.get_point_list(False)  # Populate points_list
        self.rivers = River(self.points_list)
        self.villages = Village(self.points_list, self.rivers.river_lists)
        self.mountain_chains = Mountain_chain(self.points_list)
        self.mountains = Mountain(self.points_list)


    def get_rivers(self):
        return self.rivers

    def get_mountains(self):
        return self.mountains

    def get_roads(self):
        return self.roads

    def get_villages(self):
        return self.villages

    def get_cities(self):
        return self.cities

    def get_size(self):
        size = abs((self.extreme_point[0] - self.extreme_point[2]) * (self.extreme_point[1] - self.extreme_point[3]))
        print(size)
        return size


    def generate_new_point(self, point1, point2):
        length = random.uniform(0, 1) * self.vector_size
        if self.get_length_vector(self.circle_vector) / self.size_continent > 3:
            point1 = self.scale_vector(point2, self.start_pos, self.vector_size)
            mu = -math.pi * 0.3
        else:
            mu = math.pi * (1.1)
        angle = random.gauss(mu, math.pi / 10)  # Skapa en slumpmässig vinkel, pi är rakt framåt
        return self.rotate_vector(point1, point2, length, angle)

    def rotate_vector(self, point1, point2, length,
                      angle):  # point 1 and 2 är den senaste vektorn, alltså därifrån vi ska generera från
        '''Roterar vektor point1, point2 med angle'''
        fx = point2[0]
        fy = point2[1]
        x = point1[0]
        y = point1[1]

        x_rot = ((x - fx) * math.cos(angle)) - ((y - fy) * math.sin(angle)) + fx  # rotatera kring fx och fy
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
        curr_len = math.sqrt(dx ** 2 + dy ** 2)

        scale_factor = length / curr_len
        x_new = scale_factor * (x_rot - fx)
        y_new = scale_factor * (y_rot - fy)

        # fx fy fast punkt
        return (x_new + fx, y_new + fy)

    def angle_vectors(self, vector1, vector2):
        dx1 = vector1[1][0] - vector1[0][0]
        dy1 = vector1[1][1] - vector1[0][1]
        dx2 = vector2[1][0] - vector2[0][0]
        dy2 = vector2[1][1] - vector2[0][1]

        dot_product = dx1 * dx2 + dy2 * dy1
        length_1 = self.get_length_vector(vector1)
        length_2 = self.get_length_vector(vector2)
        return math.acos(dot_product / (length_1 * length_2))

    def fix_intersects(self):  # Loppar igenom alla nodsen och kolla om x och y koordinaterna intersectar
        working_node = self.start_node.get_next()
        working_node_next = working_node.get_next()

        while working_node_next.get_data() is not self.start_pos:
            node_1 = working_node_next.get_next()
            node_2 = node_1.get_next()
            while node_1.get_data() is not self.start_pos:
                if self.crosses((working_node, working_node_next), (node_1, node_2)):
                    if node_1.leads_to_end(self.start_pos):
                        working_node.add_next(node_1)
                        working_node = node_1
                    else:
                        working_node.add_next(node_2)
                        working_node = node_2
                    break

                node_1 = node_1.get_next()
                node_2 = node_1.get_next()
            working_node = working_node.get_next()
            working_node_next = working_node.get_next()

    def intersects_exists(self):  # Loppar igenom alla nodsen och kolla om x och y koordinaterna intersectar
        working_node = self.start_node.get_next()
        working_node_next = working_node.get_next()

        while working_node_next.get_data() is not self.start_pos:
            node_1 = working_node_next.get_next()
            node_2 = node_1.get_next()
            while node_1.get_data() is not self.start_pos:
                if self.crosses((working_node, working_node_next), (node_1, node_2)):
                    return True
                node_1 = node_1.get_next()
                node_2 = node_1.get_next()
            working_node = working_node.get_next()
            working_node_next = working_node.get_next()
        return False

    def crosses(self, vector1, vector2):
        (x1, y1) = vector1[0].get_data()
        (x2, y2) = vector1[1].get_data()
        (x3, y3) = vector2[0].get_data()
        (x4, y4) = vector2[1].get_data()
        s_factor = (x2 - x1, y2 - y1)
        t_factor = (x4 - x3, y4 - y3)
        right_side = np.array([x3 - x1, y3 - y1])
        left_side = np.array([[s_factor[0], -t_factor[0]], [s_factor[1], -t_factor[1]]])
        det = np.linalg.det(left_side)
        if abs(det) < 1e-10:  # Small tolerance to handle floating point errors
            return False  # Consider as no intersection in this special case
        solution = np.linalg.inv(left_side).dot(right_side)

        s = solution[0]
        t = solution[1]
        if 0 <= s <= 1 and 0 <= t <= 1:
            return True
        else:
            return False

    def plot(self):
        plt.figure(figsize=(10, 10))
        x = []
        y = []

        # Plot the continent
        start_point = self.start_node
        while True:
            (x_temp, y_temp) = start_point.get_data()
            x.append(x_temp)
            y.append(y_temp)
            start_point = start_point.get_next()
            if start_point == self.start_node:
                break

        plt.plot(x, y, marker='o', linestyle='-', color='blue', markersize=5)
        plt.scatter(x[0], y[0], color='red', label='Start Point', zorder=5)
        plt.plot([x[-1], x[0]], [y[-1], y[0]], color='blue', linestyle='-')

        # Plot the rivers
        for river in self.rivers.river_lists:
            river_x, river_y = zip(*river)
            plt.plot(river_x, river_y, color='cyan', linestyle='-', linewidth=2)

        # Plot the villages
        for village in self.villages.village_locations:
            plt.scatter(village[0], village[1], color='red', marker='o', zorder=4)

        # Plot the mountains
        for mountain_range in self.mountain_chains.mountains_list:
            mountain_x, mountain_y = zip(*mountain_range)  # Unzip mountain points
            plt.scatter(mountain_x, mountain_y, color='green', marker='^', zorder=3)

        for mountain in self.mountains.big_mountains:
            plt.scatter(mountain[0], mountain[1], color='grey', marker='^', zorder=5,s=400 )

        plt.xlim(min(x) - 100, max(x) + 100)
        plt.ylim(min(y) - 100, max(y) + 100)
        plt.title(f'Vectors for {self.name}')
        plt.xlabel('X coordinate')
        plt.ylabel('Y coordinate')
        plt.grid()
        plt.legend()
        plt.show()

    def get_length_vector(self, vector):
        return math.sqrt((vector[0][0] - vector[1][0]) ** 2 + (vector[0][1] - vector[1][1]) ** 2)

    def get_start_node(self):
        return self.start_node

    def get_point_list(self, done=True):
        ''' Returns the continent as a list of points, starting with start position and ending with start position'''
        if not done:
            start_node = self.start_node
            list_nodes = [start_node.get_data()]
            working_node = start_node.get_next()
            while working_node.get_data() is not self.start_pos:
                list_nodes.append(working_node.get_data())
                working_node = working_node.get_next()
            list_nodes.append(working_node.get_data())
            return list_nodes
        else:
            return self.points_list

    def get_extreme_points(self):
        ''' Returns the most four most extreme points in continent max_x, max_y, min_x, min_y'''
        if self.extreme_point is None:
            
            max_x, max_y, min_x, min_y = float('-inf'), float('-inf'), float('inf'), float('inf')
            start_node = self.start_node
            value_node = start_node.get_data()
            if max_x < value_node[0]:
                max_x = value_node[0]
            elif min_x > value_node[0]:
                min_x = value_node[0]
            if max_y < value_node[1]:
                max_y = value_node[1]
            elif min_y > value_node[1]:
                min_y = value_node[1]
            working_node = start_node.get_next()
            value_node = working_node.get_data()

            while value_node is not self.start_pos:
                if max_x < value_node[0]:
                    max_x = value_node[0]
                elif min_x > value_node[0]:
                    min_x = value_node[0]
                if max_y < value_node[1]:
                    max_y = value_node[1]
                elif min_y > value_node[1]:
                    min_y = value_node[1]
                working_node = working_node.get_next()
                value_node = working_node.get_data()
            return max_x, max_y, min_x, min_y
        else:
            return self.extreme_point

    def move_continent(self, delta_x, delta_y):
        for i in range(0, len(self.points_list)):
            self.points_list[i][0], self.points_list[i][1] = self.points_list[i][0] + delta_x, self.points_list[i][
                1] + delta_y


def test():
    test_cont = Continent((1500, 1500), 120)
    test_cont.generate()
    test_cont.generate_content()  # Generate villages, rivers, and mountains

    test_cont.plot()  # Plot continent, rivers, villages, and mountains
    

test()




