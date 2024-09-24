import random
import math
import matplotlib.pyplot as plt
from matplotlib.path import Path


class Village:
    def __init__(self, continent, river_lists, village_scale, village_names = []):
        self.continent = continent
        self.river_lists = river_lists
        self.village_scale = village_scale  # Number from 1-100

        self.village_count = None
        self.village_river_count = None
        self.village_coast_count = None

        self.count_rivers = len(river_lists)
        self.count_continent_vectors = len(continent)

        self.village_locations = []

        # Set counts for villages based on the continent size and scale
        if self.village_count is None:
            self.village_count = int(self.count_continent_vectors * 0.8 * self.village_scale / 100)
            self.village_river_count = int(self.village_count * 0.6)  # At least one river village
            self.village_coast_count = int(self.village_count * 0.4)  # At least one coast village
            self.village_random_location_count = int(self.village_count * 0.4)  # At least one random village

        # Check if there are rivers before generating river villages
        if self.count_rivers > 0:
            self.generate_river_village()

        self.generate_random_villages()
        self.generate_coast_village()
        if len(village_names) != 0:
            self.set_names(village_names)

    def is_too_close(self, new_location, min_distance=5):
        """Check if new village location is too close to existing villages."""
        for village in self.village_locations:
            distance = math.sqrt((village[0] - new_location[0]) ** 2 + (village[1] - new_location[1]) ** 2)
            if distance < min_distance:
                return True
        return False

    def generate_river_village(self):
        """Generates villages near rivers."""
        for _ in range(self.village_river_count):
            iter = 0
            max_iter = 100
            while True:
                river = random.randint(0, self.count_rivers - 1)
                river_length = len(self.river_lists[river])

                # Ensure there's enough length to select a position
                if river_length < 2:
                    iter += 1
                    if iter > max_iter:

                        break  # Exit the loop when too many attempts have been made
                    continue  # Skip this river if not enough points

                river_pos = random.randint(1, river_length - 1)  # Use range safely
                river_coords = self.river_lists[river][river_pos]
                village_coords = (river_coords[0] + random.randint(-1, 1), river_coords[1] + random.randint(-1, 1))

                # Check if this village is too close to others
                if not self.is_too_close(village_coords):
                    self.village_locations.append(village_coords)
                    break  # Exit the loop when a valid location is found
                else:
                    iter += 1
                    if iter > max_iter:

                        break

    def generate_coast_village(self):
        """Generates random villages near the coast."""
        for _ in range(self.village_coast_count):
            iter = 0
            max_iter = 1000
            while True and iter < max_iter:
                coast = self.continent[random.randint(0, self.count_continent_vectors - 1)]
                iter += 1
                # Check if this village is too close to others
                if not self.is_too_close(coast):
                    self.village_locations.append(coast)
                    break  # Exit the loop when a valid location is found

    def generate_random_villages(self):
        """Generates random villages within the continent boundaries."""
        for _ in range(self.village_random_location_count):
            iter = 0
            max_iter = 1000
            while True and iter < max_iter:
                # Generate random coordinates
                x = random.uniform(min(x for x, _ in self.continent), max(x for x, _ in self.continent))
                y = random.uniform(min(y for _, y in self.continent), max(y for _, y in self.continent))
                village_coords = (x, y)
                iter += 1
                # Check if the random coordinates are inside the continent
                if self.is_point_inside_continent(village_coords):
                    self.village_locations.append(village_coords)
                    break  # Exit the loop if the point is valid

    def is_point_inside_continent(self, point):
        """Checks if a point is inside the continent defined by its vertices."""
        path = Path(self.continent)
        return path.contains_point(point)
    
    def get_cities_list(self):
        return self.village_locations
    
    def set_names(self, village_names):
        new_list = []
        for village in self.village_locations:
            named_village = [village, random.choice(village_names)]
            new_list.append(named_village)
        self.village_locations = new_list


