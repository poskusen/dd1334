import random
import math
import matplotlib.pyplot as plt


class Continent():

    def __init__(self, name, mapsize_touple, size_continent, start_pos=None):
        self.name = name
        self.mapsize_touple = mapsize_touple
        if start_pos is not None:
            self.start_pos = start_pos
        else:
            # Start in the middle of the map
            self.start_pos = (500, 500)
        self.vectors = [self.start_pos]
        self.size_continent = size_continent
        self.vector_size = 800 * size_continent / mapsize_touple[0]  # Scale vector size based on continent size

    def generate(self):
        point = self.start_pos
        next_point = (self.start_pos[0] + random.uniform(-1, 1) * self.vector_size,
                      self.start_pos[1] + random.uniform(-1, 1) * self.vector_size)
        self.vectors.append(next_point)
        steps_away = 1

        while True:
            point_holder = next_point
            next_point = self.generate_new_point(point, next_point)

            point = point_holder
            self.vectors.append(next_point)
            steps_away += 1

            # Stop when the shape comes near the starting point and has enough steps
            if math.sqrt((next_point[0] - self.start_pos[0]) ** 2 + (
                    next_point[1] - self.start_pos[1]) ** 2) < self.vector_size and steps_away > 10:
                self.vectors.append(self.start_pos)
                break

        # After generation, remove intersections
        self.remove_intersections()

        # Then reconnect nearby points to form a continuous continent
        self.reconnect_points()

    def generate_new_point(self, point1, point2):
        length = random.uniform(0, 1) * self.vector_size
        mu = math.pi * 1.1
        angle = random.gauss(mu, math.pi / 10)  # Generate a random angle
        return self.rotate_vector(point1, point2, length, angle)

    def rotate_vector(self, point1, point2, length, angle):
        '''Rotates vector point1 -> point2 by angle'''
        fx, fy = point2
        x, y = point1

        x_rot = ((x - fx) * math.cos(angle)) - ((y - fy) * math.sin(angle)) + fx
        y_rot = ((x - fx) * math.sin(angle)) + ((y - fy) * math.cos(angle)) + fy

        # Scale the vector
        return self.scale_vector(point2, (x_rot, y_rot), length)

    def scale_vector(self, point1, point2, length):
        '''Returns a point that scales the vector from point1 to point2 to a given length'''
        fx, fy = point1
        x_rot, y_rot = point2
        dx = fx - x_rot
        dy = fy - y_rot
        curr_len = math.sqrt(dx ** 2 + dy ** 2)

        scale_factor = length / curr_len
        x_new = scale_factor * (x_rot - fx)
        y_new = scale_factor * (y_rot - fy)

        return (x_new + fx, y_new + fy)

    def get_length_vector(self, p1, p2):
        return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

    def remove_intersections(self):
        ''' Check for intersections between all vector pairs and remove intersecting vectors '''
        i = 0
        vectors_to_keep = [self.vectors[0]]  # Always keep the starting point
        while i < len(self.vectors) - 2:
            keep = True
            for j in range(i + 2, len(self.vectors) - 1):  # Check non-adjacent vectors for intersections
                if self.check_intersection(self.vectors[i], self.vectors[i + 1], self.vectors[j], self.vectors[j + 1]):
                    keep = False
                    break
            if keep:
                vectors_to_keep.append(self.vectors[i + 1])
            i += 1

        # Add the last vector (closing the loop)
        vectors_to_keep.append(self.vectors[-1])
        self.vectors = vectors_to_keep  # Update vectors after removing intersections

    def check_intersection(self, p1, p2, p3, p4):
        ''' Check if line segment (p1, p2) intersects with line segment (p3, p4) '''

        def orientation(p, q, r):
            val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
            if val == 0:
                return 0  # collinear
            elif val > 0:
                return 1  # clockwise
            else:
                return 2  # counterclockwise

        def on_segment(p, q, r):
            return min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and min(p[1], r[1]) <= q[1] <= max(p[1], r[1])

        o1 = orientation(p1, p2, p3)
        o2 = orientation(p1, p2, p4)
        o3 = orientation(p3, p4, p1)
        o4 = orientation(p3, p4, p2)

        if o1 != o2 and o3 != o4:
            return True

        if o1 == 0 and on_segment(p1, p3, p2):
            return True

        if o2 == 0 and on_segment(p1, p4, p2):
            return True

        if o3 == 0 and on_segment(p3, p1, p4):
            return True

        if o4 == 0 and on_segment(p3, p2, p4):
            return True

        return False

    def reconnect_points(self):
        ''' Reconnect points that are close to each other after removing intersections '''
        threshold_distance = self.vector_size * 1.5  # Set a threshold distance to reconnect points
        i = 0
        while i < len(self.vectors) - 1:
            if self.get_length_vector(self.vectors[i], self.vectors[i + 1]) > threshold_distance:
                # If points are far apart, insert a new point between them
                mid_point = ((self.vectors[i][0] + self.vectors[i + 1][0]) / 2,
                             (self.vectors[i][1] + self.vectors[i + 1][1]) / 2)
                self.vectors.insert(i + 1, mid_point)
            i += 1

    def plot(self):
        ''' Plots the generated continent '''
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


def test():
    for i in range(10):
        test_cont = Continent('test', (1000, 1000), 100)
        test_cont.generate()
        test_cont.plot()
        print(test_cont.vectors)


test()
