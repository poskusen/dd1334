import random
import math
import matplotlib.pyplot as plt

class Village():
    def __init__(self, continent, river_lists, village_scale=100):
        self.continent = continent
        self.river_lists = river_lists
        self.village_scale = village_scale  # Number from 1-100

        self.village_count = None
        self.village_river_count = None
        self.village_coast_count = None

        self.count_rivers = len(river_lists)
        self.count_continent_vectors = len(continent)

        self.village_locations = []



        # 70% of Villages close to Rivers, 30% Close to Coastlines and also and some stand alone villages
        if self.village_count is None:
            self.village_count = int(self.count_continent_vectors * 0.8 * self.village_scale / 100)
            self.village_river_count = int(self.village_count * 0.6) + 1
            self.village_coast_count = int(self.village_count * 0.4) + 1
            self.village_random_location_count = int(self.village_count * 0.4) + 1


    def is_too_close(self, new_location, min_distance=5):
        """Check if new village location is too close to existing villages."""
        for village in self.village_locations:
            distance = math.sqrt((village[0] - new_location[0]) ** 2 + (village[1] - new_location[1]) ** 2)
            if distance < min_distance:
                return True
        return False

    def generate_river_village(self):
        """Generates villages near rivers."""
        for i in range(self.village_river_count):
            while True:
                river = random.randint(0, self.count_rivers - 1)
                river_pos = random.randint(1, len(self.river_lists[river]) - 1)

                river_cords = self.river_lists[river][river_pos]
                village_cords = (river_cords[0] + random.randint(-1, 1), river_cords[1] + random.randint(-1, 1))

                # Check if this village is too close to others
                if not self.is_too_close(village_cords):
                    self.village_locations.append(village_cords)

                    break

    def generate_coast_village(self):
        """Generates random villages near the coast"""
        for i in range(self.village_coast_count):
            while True:
                coast = self.continent[random.randint(0, self.count_continent_vectors - 1)]

                # Check if this village is too close to others
                if not self.is_too_close(coast):
                    self.village_locations.append(coast)
                    break

    def generate_random_villages(self):
        """Generates random villages within the continent boundaries."""
        for i in range(self.village_random_location_count):
            while True:
                # Generate random coordinates
                x = random.uniform(min(x for x, _ in self.continent), max(x for x, _ in self.continent))
                y = random.uniform(min(y for _, y in self.continent), max(y for _, y in self.continent))
                village_cords = (x, y)

                # Check if the random coordinates are inside the continent
                if self.is_point_inside_continent(village_cords):
                    self.village_locations.append(village_cords)
                    break  # Exit the while loop if the point is valid

    def is_point_inside_continent(self, point):
        """Checks if a point is inside the continent defined by its vertices."""
        from matplotlib.path import Path

        path = Path(self.continent)
        return path.contains_point(point)

