import random
from vector import vector

class Continent:

    def __init__(self, name, mapsizetouple, startpos=None):
        self.name = name
        self.startpos = startpos
        self.mapsizetouple = mapsizetouple
    def generatestartpos(self):
        self.startpos = (random.randint(0, self.mapsizetouple[0]), random.randint(0, self.mapsizetouple[1]))

    def generatecontinent(self):
        vectorlist = []




def test():
    kontinenten = Continent("cool", mapsizetouple=(1000,1000))
    kontinenten.generatestartpos()
    print(kontinenten.startpos)




test()

