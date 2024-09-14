import matplotlib.pyplot as plt
import random
import math
import numpy as np
from matplotlib.path import Path

class River:
    def __init__(self, continent, river_scale=100, size_continent=100):
        self.continent = continent
        self.river_scale = river_scale
        self.rivers_count = None
        self.river_lists = []
        self.river_positions = []
        self.river_size = size_continent / self.count_vectors()

        if self.rivers_count is None:
            river_percent = 0.3 * river_scale / 100
            self.rivers_count = int(self.count_vectors() * river_percent)

        for i in range(self.rivers_count):
            pos = random.randint(0, (self.count_vectors()) - 1)
            self.river_positions.append(pos)

    def generate_river(self):
        """Gemerates rovers_count rivers and appends them to river_lists"""
        for i in range(self.rivers_count):
            temp_river = []
            river_pos = self.river_positions[i]
            pos_1 = self.continent[river_pos]
            pos_2 = self.continent[river_pos - 1]
            direction = self.normal_vector(pos_1, pos_2)

            mid_point = self.midpoint(pos_1, pos_2)

            pos_3 = (mid_point[0] + direction[0], mid_point[1] + direction[1])
            temp_river.append(mid_point)

            for _ in range(50):  # Generate 30 river vectors
                next_pos = self.generate_xy_pos(pos_3, mid_point, pos_3)
                if self.is_within_continent(next_pos):  # Check if the next position is within the continent
                    temp_river.append(next_pos)
                mid_point = pos_3
                pos_3 = next_pos

            self.river_lists.append(temp_river)

    def generate_xy_pos(self, last_touple, u1, u2):
        """Genera"""
        while True:
            xrandom = last_touple[0] + random.randint(-5, 5)
            yrandom = last_touple[1] + random.randint(-5, 5)

            if xrandom != 0 and yrandom != 0:
                next_pos = (xrandom, yrandom)

                v = (xrandom - last_touple[0], yrandom - last_touple[1])
                norm_v = np.linalg.norm(v)

                first_vector = (u2[0] - u1[0], u2[1] - u1[1])
                tempvector = (xrandom - last_touple[0], yrandom - last_touple[1])

                if -30 < self.vectorangle(first_vector, tempvector) < 30 and norm_v != 0:
                    return next_pos

    def vectorangle(self, first_vector, second_vector):
        u = first_vector
        v = second_vector
        dot_product = u[0] * v[0] + u[1] * v[1]
        norm_v = np.linalg.norm(v)
        norm_u = np.linalg.norm(u)

        if norm_u == 0 or norm_v == 0:
            return 0

        cos_theta = dot_product / (norm_u * norm_v)
        cos_theta = max(-1, min(1, cos_theta))
        angle_radians = math.acos(cos_theta)

        return math.degrees(angle_radians)

    def normal_vector(self, p1, p2):
        direction_vector = (p2[0] - p1[0], p2[1] - p1[1])
        normal = (-direction_vector[1], direction_vector[0])
        magnitude = math.sqrt(normal[0] ** 2 + normal[1] ** 2)

        if magnitude != 0:
            normal = (normal[0] / magnitude, normal[1] / magnitude)
            normal = (normal[0] * -5, normal[1] * -5)
        else:
            normal = (0, 0)

        return normal

    def midpoint(self, point1, point2):
        mid_x = (point1[0] + point2[0]) / 2
        mid_y = (point1[1] + point2[1]) / 2
        return (mid_x, mid_y)

    def count_vectors(self):
        return len(self.continent)

    def is_within_continent(self, point):
        # Create a path from the continent points
        path = Path(self.continent)
        return path.contains_point(point)


def plot_continent_and_rivers(continent, river_lists):
    plt.figure(figsize=(10, 10))

    # Plot the continent
    continent_x, continent_y = zip(*continent)
    plt.plot(continent_x, continent_y, color='green', label='Continent', linewidth=2)

    # Plot the rivers with thicker lines
    for river in river_lists:
        river_x, river_y = zip(*river)
        plt.plot(river_x, river_y, color='blue', linewidth=2, linestyle='-', label='River')

    plt.title('Continent and Rivers')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.axis('equal')
    plt.grid()
    plt.legend()
    plt.show()


def test():
    continent = [(500, 500), (561.0320489811663, 496.76426233680036), (614.6723780055507, 536.163370800318),
                 (644.0822612505784, 567.1471724315649), (662.5499586980152, 585.7461098734568),
                 (662.6786905682109, 586.1011225956856), (653.3303362417543, 618.954828820058),
                 (625.7282457881066, 693.6354948271372), (613.4196220928332, 729.5127538935301),
                 (597.3321915440589, 756.2401294664818), (574.4593951463479, 775.1386188767792),
                 (562.0202255523436, 778.0442973529632), (506.75438593080906, 733.1540091973247),
                 (503.18114278654167, 729.5095661794837), (455.53683199771416, 707.8886412192259),
                 (444.2925867059378, 694.7874314835107), (439.8039075548508, 619.0313982222536),
                 (455.64769693279703, 568.5868069515998), (484.29588455909953, 562.1353332826781), (500, 500)]

    test_river = River(continent)
    print(test_river.count_vectors())
    print(test_river.river_positions)

    test_river.generate_river()
    print(test_river.river_lists)

    # Plot the continent and rivers
    plot_continent_and_rivers(continent, test_river.river_lists)



test()
