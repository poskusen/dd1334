from Classes.continent import Continent

class Map:

    def _init_(self, mapsizex, mapsizey, mapsizetouple, continentscale, popscale, mapsize, riverscale, mountainscale, tempscale, rainscale, continent):
        self.mapsizex = mapsizex
        self.mapsizey = mapsizey
        self.mapsizetouple = mapsizetouple

        self.continentscale = continentscale    #Generates a number of continents 1-x Based on a scale of 1-100
        self.popscale = popscale
        self.mapsize = mapsize
        self.riverscale = riverscale
        self.mountainscale = mountainscale
        self.tempscale = tempscale
        self.rainscale = rainscale

        self.continent = continent


    def generatemapsize(self, mapsize):
        self.mapsizex = 1000
        self.mapsizey = 1000
        self.mapsizetouple = (self.mapsizex, self.mapsizey)

    def generatecontinent(self, continentscale): #Or Fetch continent, depends on where the generative process is supposed to be locatied
        self.continent = Continent(self.mapsizetouple)
