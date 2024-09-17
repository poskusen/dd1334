import random
import numpy as np
import math
from vector import Vector

class Continent:

    def __init__(self, name, mapsizetouple, startpos=None, startvector=None, currentvector=None, circlevector=None):
        self.name = name
        self.startpos = startpos
        self.mapsizetouple = mapsizetouple
        self.startvector = startvector
        self.currentvector = currentvector

        self.circlevector = circlevector

    def generatestartpos(self):
        '''Generates a random starting position for the first continent-vector'''
        self.startpos = (random.randint(0, self.mapsizetouple[0]), random.randint(0, self.mapsizetouple[1]))

    def generatecontinent(self):
        '''Hopefully makes a continent!'''
        self.generatestartpos()
        startpos = self.startpos

        secondpos = (startpos[0] + random.randint(1,10),startpos[1] + random.randint(1,10)) #Make sure that the first vector is pointed upwards and not 0
        self.startvector = Vector(startpos, secondpos)
        self.currentvector = self.startvector

        self.circlevector = Vector(startpos,secondpos)

        for i in range(10):
            next_pos = self.generatexypos()
            self.circlevector.secondpos = next_pos

            new_vector = Vector(self.currentvector.secondpos,next_pos)
            self.currentvector.nextvector = new_vector
            self.currentvector = new_vector


    def generatexypos(self):
        '''generate new xy-position without going outside the canvas and whitout generating a new vector with an angle greater than 90 or less than -90 degrees'''
        while True:
            print(self.currentvector.secondpos)
            xrandom = self.currentvector.secondpos[0] + random.randint(-15,15)
            yrandom = self.currentvector.secondpos[1] + random.randint(-15,15)

            if xrandom != 0 and yrandom != 0: #Make sure that we do not get the same position resulting in division by 0
                next_pos = (xrandom, yrandom)
                tempvector = Vector(self.currentvector.secondpos, next_pos)

                v = (tempvector.secondpos[0] - tempvector.firstpos[0], tempvector.secondpos[1] - tempvector.firstpos[1])
                norm_v = np.linalg.norm(v)


                if -90 < self.vectorangle(self.circlevector, tempvector) < 90 and 0 < next_pos[0] < self.mapsizetouple[0] and 0 <next_pos[1] < self.mapsizetouple[1] and norm_v != 0:
                    return next_pos
                    False




    def vectorangle(self, firstvectorobject, secondvectorobject):
        '''Calculates the angle between two vectors'''
        u = (firstvectorobject.secondpos[0] - firstvectorobject.firstpos[0], firstvectorobject.secondpos[1] - firstvectorobject.firstpos[1])
        v = (secondvectorobject.secondpos[0] - secondvectorobject.firstpos[0], secondvectorobject.secondpos[1] - secondvectorobject.firstpos[1])

        dot_product = u[0] * v[0] + u[1] * v[1]

        norm_v = np.linalg.norm(v)
        norm_u = np.linalg.norm(u)

        if norm_u == 0 or norm_v == 0:
            print("Gg")

        cos_theta = dot_product / (norm_u*norm_v)



        cos_theta = max(-1, min(1, cos_theta))

        angle_radians = math.acos(cos_theta)

        vectorangle = math.degrees(angle_radians)

        return vectorangle



def test():
    kontinenten = Continent("cool", mapsizetouple=(1000,1000))
    kontinenten.generatestartpos()
    kontinenten.generatecontinent()
    x = kontinenten.generatexypos()
    print(x)






