import random
import numpy as np
import math
from vector import Vector
import matplotlib.pyplot as plt


class Continent:

    def __init__(self, name, mapsizetouple, startpos=None, startvector=None, currentvector=None, circlevector=None):
        self.name = name
        self.startpos = startpos
        self.mapsizetouple = mapsizetouple
        self.startvector = startvector
        self.currentvector = currentvector
        self.circlevector = circlevector
        self.vectors = []  # Store all generated vectors for plotting

    def generatestartpos(self):
        '''Generates a random starting position for the first continent-vector'''
        self.startpos = (random.randint(0, self.mapsizetouple[0]), random.randint(0, self.mapsizetouple[1]))

    def generatecontinent(self):
        '''Hopefully makes a continent!'''
        self.generatestartpos()
        startpos = self.startpos

        secondpos = (startpos[0] + random.randint(1, 10), startpos[1] + random.randint(1, 10))  # First vector
        self.startvector = Vector(startpos, secondpos)
        self.currentvector = self.startvector
        self.circlevector = Vector(startpos, secondpos)

        # Store the first vector
        self.vectors.append((startpos, secondpos)) # Behöver vi verkligen stora, annars behöver de inte vara länkade

        for i in range(20):
            next_pos = self.generatexypos()
            self.circlevector.secondpos = next_pos

            new_vector = Vector(self.currentvector.secondpos, next_pos)
            self.currentvector.nexvector = new_vector
            self.currentvector = new_vector

            # Store the new vector
            self.vectors.append((self.currentvector.firstpos, next_pos))

    def generatexypos(self):
        '''Generate new xy-position without going outside the canvas and without generating a new vector with an angle greater than 90 or less than -90 degrees'''
        while True:

            xrandom = self.currentvector.secondpos[0] + random.randint(-15, 15)
            yrandom = self.currentvector.secondpos[1] + random.randint(-15, 15)

            if xrandom != 0 and yrandom != 0:  # Avoid division by 0
                next_pos = (xrandom, yrandom)
                tempvector = Vector(self.currentvector.secondpos, next_pos)

                v = (tempvector.secondpos[0] - tempvector.firstpos[0], tempvector.secondpos[1] - tempvector.firstpos[1])
                norm_v = np.linalg.norm(v)

                if (-90 < self.vectorangle(self.circlevector, tempvector) < 90 and
                        0 < next_pos[0] < self.mapsizetouple[0] and
                        0 < next_pos[1] < self.mapsizetouple[1] and
                        norm_v != 0):
                    return next_pos

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

        plt.xlim(0, self.mapsizetouple[0])
        plt.ylim(0, self.mapsizetouple[1])
        plt.title(f'Vectors for {self.name}')
        plt.xlabel('X coordinate')
        plt.ylabel('Y coordinate')
        plt.grid()
        plt.show()


def test():
    kontinenten = Continent("cool", mapsizetouple=(1000, 1000))
    kontinenten.generatestartpos()
    kontinenten.generatecontinent()
    kontinenten.plot_vectors()  # Call the plotting function


test()
