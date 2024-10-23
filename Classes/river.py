import random
import math
import numpy as np
from matplotlib.path import Path

class River:
    def __init__(self, continent, river_scale, size_continent=100, river_pos = None):
        self.continent = continent
        self.river_scale = river_scale
        self.rivers_count = None
        self.river_lists = []
        self.river_positions = []
        self.river_size = size_continent / self.count_vectors()
        if river_pos == None:
            if self.rivers_count is None:
                river_percent = 0.3 * river_scale / 100
                self.rivers_count = int(self.count_vectors() * river_percent)

            for i in range(self.rivers_count):
                pos = random.randint(0, (self.count_vectors()) - 1)
                self.river_positions.append(pos)

            self.generate_river()
        else:
            self.river_lists = river_pos

    def generate_river(self):
        """Generates rivers_count rivers and appends them to river_lists"""
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
        """Generate"""
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
    
    def get_river_list(self):
        return self.river_lists




