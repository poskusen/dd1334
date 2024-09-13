import matplotlib.pyplot as plt
import random
import math
import numpy as np


class river:
    def __init__(self, continent, river_weight=100, size_continent=100):  # river_weight assumed to be value 1-100
        self.continent = continent
        self.river_weight = river_weight

        self.rivers_count = None
        self.river_lists = []
        self.river_positions = []

        self.river_size = size_continent / self.count_vectors()  # Make up some arbitrary way to generate river_size

        if self.rivers_count is None:
            river_percent = 0.2 * river_weight / 100  # Calculates how many vectors in continent that will have a river, max 40% (CAN BE CHANGED)
            self.rivers_count = int((self.count_vectors() * river_percent))  # Number of rivers can be dynamic

        for i in range(self.rivers_count):  # Appends the river positions (positions in the vector list)
            pos = random.randint(0, (self.count_vectors()) - 1)
            self.river_positions.append(pos)

    def generate_river(self):
        for i in range(self.rivers_count):
            temp_river = []
            river_pos = self.river_positions[i]
            pos_1 = self.continent[river_pos]
            pos_2 = self.continent[river_pos - 1]
            direction = self.normal_vector(pos_1, pos_2)

            mid_point = self.midpoint(pos_1, pos_2)

            pos_3 = (
                mid_point[0] + direction[0], mid_point[1] + direction[1])  # This is the initialized vector for the river

            temp_river.append(mid_point)  # First vector first position that intersects continent border
            temp_river.append(pos_3)  # First vector second position

            for _ in range(30):  # Makes 30 river vectors
                next_pos = self.generate_xy_pos(pos_3, mid_point, pos_3)
                temp_river.append(next_pos)

                mid_point = pos_3
                pos_3 = next_pos

            self.river_lists.append(temp_river)

    def generate_xy_pos(self, last_touple, u1, u2):
        '''Generate new xy-position without going outside the canvas and without generating a new vector with an angle greater than 90 or less than -90 degrees.'''
        while True:
            xrandom = last_touple[0] + random.randint(-5, 5)
            yrandom = last_touple[1] + random.randint(-5, 5)

            if xrandom != 0 and yrandom != 0:  # Make sure that we do not get the same position resulting in division by 0
                next_pos = (xrandom, yrandom)

                v = (xrandom - last_touple[0], yrandom - last_touple[1])
                norm_v = np.linalg.norm(v)

                first_vector = (u2[0] - u1[0], u2[1] - u1[1])  # First Vector
                tempvector = (xrandom - last_touple[0], yrandom - last_touple[1])

                if -30 < self.vectorangle(first_vector, tempvector) < 30 and norm_v != 0:
                    return next_pos

    def vectorangle(self, first_vector, second_vector):
        u = first_vector
        v = second_vector
        '''Calculates the angle between two vectors.'''
        dot_product = u[0] * v[0] + u[1] * v[1]

        norm_v = np.linalg.norm(v)
        norm_u = np.linalg.norm(u)

        # Check for zero vectors
        if norm_u == 0 or norm_v == 0:
            return 0  # or any value that makes sense for your application

        cos_theta = dot_product / (norm_u * norm_v)

        cos_theta = max(-1, min(1, cos_theta))

        angle_radians = math.acos(cos_theta)

        vectorangle = math.degrees(angle_radians)

        return vectorangle

    def normal_vector(self, p1, p2):
        # Calculate the direction vector
        direction_vector = (p2[0] - p1[0], p2[1] - p1[1])

        # Calculate the normal vector (90 degrees counterclockwise)
        normal = (-direction_vector[1], direction_vector[0])

        # Calculate the magnitude of the normal vector
        magnitude = math.sqrt(normal[0] ** 2 + normal[1] ** 2)

        # Normalize the normal vector (make it unit length)
        if magnitude != 0:
            normal = (normal[0] / magnitude, normal[1] / magnitude)
            normal = (
                normal[0] * -5, normal[1] * -5)  # Without - and 5 they are pointing in the wrong direction + too small
        else:
            normal = (0, 0)  # Handle the case where the magnitude is zero

        return normal

    def midpoint(self, point1, point2):
        """Calculate the midpoint between two points."""
        mid_x = (point1[0] + point2[0]) / 2
        mid_y = (point1[1] + point2[1]) / 2
        return (mid_x, mid_y)

    def count_vectors(self):
        """Return number of vectors in continent."""
        return len(self.continent)


def plot_continent_and_rivers(continent, river_lists):
    plt.figure(figsize=(10, 10))

    # Plot the continent
    continent_x, continent_y = zip(*continent)
    plt.plot(continent_x, continent_y, color='green', label='Continent', linewidth=2)

    # Plot the rivers with thicker lines
    for river in river_lists:
        river_x, river_y = zip(*river)
        plt.plot(river_x, river_y, color='blue', linewidth=2, linestyle='-', label='River')  # Increased linewidth to 2

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

    test_river = river(continent)
    print(test_river.count_vectors())
    print(test_river.river_positions)

    test_river.generate_river()
    print(test_river.river_lists)

    # Plot the continent and rivers
    plot_continent_and_rivers(continent, test_river.river_lists)


test()
