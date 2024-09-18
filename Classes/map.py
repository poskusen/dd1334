from continent import Continent

class Map:

    def _init_(self, amount_continents, continentscale, popscale, riverscale, mountainscale, tempscale, rainscale, mapsize = (1000, 1000)):
        self.generatemapsize(mapsize)
        self.mapsize = mapsize
        self.amount_continents = amount_continents
        self.continentscale = continentscale    #Generates a number of continents 1-x Based on a scale of 1-100
        self.popscale = popscale
        self.riverscale = riverscale
        self.mountainscale = mountainscale
        self.tempscale = tempscale
        self.rainscale = rainscale


    def get_mapsize(self):
        return self.mapsize
    
    def generatemapsize(self, mapsize):
        self.mapsizex = mapsize[0]
        self.mapsizey = mapsize[1]
        self.mapsizetouple = (self.mapsizex, self.mapsizey)

    def generatemap(self):
        self.generatecontinent(self.amount_continents)
    
    def generate_continents(self, amount_continents):
        for i in range(amount_continents):

    def generate_rivers(self):
        pass
    
    def get_river()

