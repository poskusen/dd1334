import random

class Continent:

    def __init__(self, name, startpos, mapsizetouple):
        self.name = name
        self.startpos = startpos
        self.mapsizetouple = mapsizetouple
    def generatestartpos(self):
        self.startpos = (random.randint(self.mapsizetouple[0], self.mapsizetouple[1]))


def test():
    kontinenten = Continent("cool", mapsizetouple=(1000,1000))
    x = Continent.generatestartpos()
    print(x)



test()

