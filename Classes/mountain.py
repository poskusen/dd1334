import matplotlib.pyplot as plt
import random
import math
from matplotlib.path import Path


class Mountain_chain():

    def __init__(self, continent, mountain_scale):

        self.continent = continent
        self.mountain_scale = mountain_scale

        self.mountains_count = None

        self.mountains_list = [] #A list containing lists of the mountain ranges, A position in this list represent a mountain range, that position has a list in it with scattered positions of mountains

        # Create a Path object from the continent coordinates
        self.path = Path(self.continent)

        if self.mountains_count is None:
            self.mountains_count = int(len(self.continent)*0.4*self.mountain_scale/100)

        self.generate_mountain_range()

    def generate_mountain_range(self):
        """Generates a number of mountain ranges"""
        for i in range(self.mountains_count):
            while True:
                # Generate random coordinates
                x = random.uniform(min(x for x, _ in self.continent), max(x for x, _ in self.continent))
                y = random.uniform(min(y for _, y in self.continent), max(y for _, y in self.continent))
                mountain_cords = (x, y)

                # Check if the random coordinates are inside the continent
                if self.is_point_inside_continent(mountain_cords):
                    mountains = []

                    for i in range(50):
                        x_point = random.gauss(mountain_cords[0], 10)
                        y_point = random.gauss(mountain_cords[1], 5)

                        mountain = (x_point, y_point)

                        if self.is_point_inside_continent(mountain):
                            mountains.append((x_point, y_point))

                    self.mountains_list.append(mountains)

                    break  # Exit the while loop if the point is valid

    def is_point_inside_continent(self, point):
        """Checks if a point is inside the continent defined by its vertices."""
        path = Path(self.continent)
        return path.contains_point(point)
    
    def get_mountain_chains(self):
        return self.mountains_list

class Mountain():
    def __init__(self, continent, mountain_scale, mountain_names_select = []):
        self.continent = continent
        self.mountain_scale = mountain_scale

        self.big_mountains = []
        self.mountain_names_select = mountain_names_select
        self.mountains_count = int(len(self.continent) * 0.2 * self.mountain_scale/100)
        self.generate_big_mountains()

    def generate_big_mountains(self):
        for i in range(self.mountains_count):
            while True:
                # Generate random coordinates
                x = random.uniform(min(x for x, _ in self.continent), max(x for x, _ in self.continent))
                y = random.uniform(min(y for _, y in self.continent), max(y for _, y in self.continent))
                mountain_cords = (x, y)

                # Check if the random coordinates are inside the continent
                if self.is_point_inside_continent(mountain_cords):
                    if len(self.mountain_names_select) != 0:
                        mountain_name = random.choice(self.mountain_names_select)
                        self.big_mountains.append((mountain_cords, mountain_name))
                    else: 
                        self.big_mountains.append(mountain_cords)
                    break

    def is_point_inside_continent(self, point):
        """Checks if a point is inside the continent defined by its vertices."""
        path = Path(self.continent)
        return path.contains_point(point)


    def get_mountain_list(self):
        
        return self.big_mountains