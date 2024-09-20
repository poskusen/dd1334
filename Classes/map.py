from Classes.continent import Continent
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
        error_range = continent_scale*continent_scale
        size_variance = 100

        for i in range(amount_continents):
            size_continent = random.randint(continent_scale - size_variance, continent_scale + size_variance)
            continent = Continent(self.mapsize, size_continent)
            while continent.get_size() > error_range*2 + error_range or continent.get_size() < error_range*2 - error_range:
                continent = Continent(self.mapsize, size_continent)
            could_place = False
            while not could_place:
                could_place, move_x, move_y = self.place(continent)
            continent.move_continent(move_x, move_y)
            continent.generate_content()
            self.continent_list.append(continent)
            
    def get_continents(self):
        return self.continent_list
    
    def place(self, continent):
        edges = continent.get_extreme_points()
        move_x, move_y = random.uniform(-1,1)*500, random.uniform(-1,1)*500
        edges[0], edges[1], edges[2], edges[3] = edges[0] + move_x, edges[1] + move_y, edges[2] + move_x, edges[3] + move_y
        for cont in self.continent_list:
            check_edges = cont.get_extreme_points()
            if check_edges[0] > edges[0] > check_edges[2] or check_edges[0] > edges[2] > check_edges[2]:
                return False, None, None
            elif check_edges[1] > edges[1] > check_edges[3] or check_edges[1] > edges[3] > check_edges[3]:
                return False, None, None

        return True, move_x, move_y



    

