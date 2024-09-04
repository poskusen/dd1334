import random
from vector import Vector

class Continent:

    def __init__(self, name, mapsizetouple, startpos=None, startvector=None, currentvector=None):
        self.name = name
        self.startpos = startpos
        self.mapsizetouple = mapsizetouple
        self.startvector = startvector
        self.currentvector = currentvector

    def generatestartpos(self):
        self.startpos = (random.randint(0, self.mapsizetouple[0]), random.randint(0, self.mapsizetouple[1]))

    def generatecontinent(self):
        #We need to initiate two vectors to generate more vectors?
        startpos = self.startpos
        secondpos = (startpos[0]+random.randint(0,10),startpos[1]+random.randint(0,10)) #Make sure that the first vector is pointed upwards
        self.startvector = Vector(startpos, secondpos)




    def generatenextstep(self):
        angle = random.randint(0, 360)






hejheh



def test():
    kontinenten = Continent("cool", mapsizetouple=(1000,1000))
    kontinenten.generatestartpos()
    kontinenten.generatecontinent()
    print(kontinenten.startvector)
    print(kontinenten.startpos)





test()

