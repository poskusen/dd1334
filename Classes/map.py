from continent import Continent
import random

class Map:

    def _init_(self, amount_continents, continent_scale, pop_scale, river_scale, mountain_scale, temp_scale, rain_scale, mapsize = (1000, 1000)):
        self.mapsize = mapsize
        self.amount_continents = amount_continents
        self.continent_scale = continent_scale    #Generates a number of continents 1-x Based on a scale of 1-100
        self.pop_scale = pop_scale
        self.river_scale = river_scale
        self.mountain_scale = mountain_scale
        self.temp_scale = temp_scale
        self.rain_scale = rain_scale


    def get_mapsize(self):
        return self.mapsize
    
    def generate_map(self):
        self.generatecontinent(self.amount_continents)
    
    def generate_continents(self, amount_continents, continent_scale):
        self.continent_list = []
        error_range = 300
        size_variance = 100

        for i in range(amount_continents):
            size_continent = random.randint(continent_scale - size_variance, continent_scale + size_variance)
            continent = Continent(self.mapsize, size_continent)
            while continent.get_size() > continent_scale + error_range or continent.get_size() < continent_scale - error_range:
                continent = Continent(self.mapsize, size_continent)
            continent.generate_content()
            self.continent_list.append(continent)
            
    def get_continents(self):
        return self.continent_list


    

