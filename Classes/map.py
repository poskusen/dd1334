from continent import Continent

class Map:

    def _init_(self, continentscale, popscale, mapsize, riverscale, mountainscale, tempscale, rainscale, continentlist):
        self.continentscale = continentscale    #Generates a number of continents 1-x Based on a scale of 1-100
        self.popscale = popscale
        self.mapsize = mapsize
        self.riverscale = riverscale
        self.mountainscale = mountainscale
        self.tempscale = tempscale
        self.rainscale = rainscale

        self.continentlist = continentlist

    def generatecontinent(self, continentscale): #Or Fetch continent, depends on where the generative process is supposed to be locatied

        return self.continentlist
