from Classes.continent import Continent
import random
from matplotlib.path import Path

class Map:

    def __init__(self, amount_continents, continent_scale, river_scale, mountain_scale, village_scale, mapsize = (1000, 1000), realm_name = 'Olles balla värld', mountain_names = [], village_names = [], create_new = True):
        self.mapsize = mapsize
        self.amount_continents = amount_continents
        self.continent_scale = continent_scale    #Generates a number of continents 1-x Based on a scale of 1-100
        self.river_scale = river_scale
        self.mountain_scale = mountain_scale
        self.village_scale = village_scale
        self.continent_list = []
        self.realm_name = realm_name

        if len(mountain_names) != 0:
            self.draw_mountain_name = True
        else:
            self.draw_mountain_name = False
        if len(village_names) != 0:
            self.draw_village_name = True
        else:
            self.draw_village_name = False
        if create_new:
            self.generate_map(mountain_names, village_names)

    def add_continent(self, continent, content):
        self.continent_list.append(Continent(self.mapsize, 1000, mountainscale=self.mountain_scale, villagescale=self.village_scale, riverscale=self.river_scale, content=content, point_list=continent))
            

    def draw_mountain_names(self):
        return self.draw_mountain_name

    def draw_village_names(self):
        return self.draw_village_name
    
    def get_mapsize(self):
        return self.mapsize
    
    def get_realm_name(self):
        return self.realm_name

    def get_continent_amount(self):
        return self.amount_continents
    
    def generate_map(self, mountain_names, village_names):
        self.generate_continents(self.amount_continents, self.continent_scale, mountain_names, village_names)
    
    def generate_continents(self, amount_continents, continent_scale, mountain_names, village_names):
        error_range = continent_scale*continent_scale
        size_variance = 50

        for i in range(amount_continents):
            size_continent = 220*continent_scale/100 # Subject to change
            continent = Continent(self.mapsize, size_continent, mountainscale=self.mountain_scale, villagescale=self.village_scale, riverscale=self.river_scale)
            continent.generate()
            condition = False
            
            while not condition:
                continent = Continent(self.mapsize, size_continent, mountainscale=self.mountain_scale, riverscale=self.river_scale, villagescale=self.village_scale)
                continent.generate()
                continent_vertices = len(continent.get_point_list())
                condition = continent_vertices > 20
            could_place = False
            deviation = 0
            while not could_place:
                could_place, deviation_extra = self.place_good(continent, deviation)
                deviation += deviation_extra

            continent.generate_content(mountain_names, village_names)
            self.continent_list.append(continent)
            
    def get_continents(self):
        return self.continent_list
    

    def place_good(self, continent, deviation_extra):
        deviation = self.mapsize[0]/10 + deviation_extra
        move_x, move_y = random.gauss(0, deviation), random.gauss(0, deviation)
        point_list = continent.move_continent(move_x, move_y)
        path_list = Path(point_list)
        success = True
        for cont in self.continent_list:
            check_list = cont.get_point_list()
            for point in check_list:
                if path_list.contains_point(point):
                    continent.move_continent(-move_x, -move_y)
                    return False, self.mapsize[0]/100
            if not success:
                break
        return True, 0




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