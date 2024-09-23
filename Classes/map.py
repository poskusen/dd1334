from Classes.continent import Continent
import random

class Map:

    def __init__(self, amount_continents, continent_scale , river_scale, mountain_scale, village_scale, mapsize = (1000, 1000)):
        self.mapsize = mapsize
        self.amount_continents = amount_continents
        self.continent_scale = continent_scale    #Generates a number of continents 1-x Based on a scale of 1-100
        self.river_scale = river_scale
        self.mountain_scale = mountain_scale
        self.village_scale = village_scale
        self.continent_list = []
        self.generate_map()


    def get_mapsize(self):
        return self.mapsize
    
    def generate_map(self):
        self.generate_continents(self.amount_continents, self.continent_scale)
    
    def generate_continents(self, amount_continents, continent_scale):
        error_range = continent_scale*continent_scale
        size_variance = 50

        for i in range(amount_continents):
            size_continent = 220*continent_scale/100 #Subject to change
            continent = Continent(self.mapsize, size_continent,mountainscale=self.mountain_scale,villagescale=self.village_scale, riverscale=self.river_scale)
            continent.generate()
            condition = False
            
            while not condition:
                continent = Continent(self.mapsize, size_continent, mountainscale=self.mountain_scale, riverscale=self.river_scale, villagescale=self.village_scale)
                continent.generate()
                condition = continent.get_size() > error_range*2 + error_range or continent.get_size() < error_range*2 - error_range
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
        
        deviation = self.mapsize[0]/5
        move_x, move_y = random.gauss(0, deviation), random.gauss(0, deviation)
        edges[0], edges[1], edges[2], edges[3] = edges[0] + move_x, edges[1] + move_y, edges[2] + move_x, edges[3] + move_y
        for cont in self.continent_list:
            check_edges = cont.get_extreme_points()
            if check_edges[0] > edges[0] > check_edges[2] or check_edges[0] > edges[2] > check_edges[2]:
                return False, None, None
            elif check_edges[1] > edges[1] > check_edges[3] or check_edges[1] > edges[3] > check_edges[3]:
                return False, None, None

        return True, move_x, move_y



    

