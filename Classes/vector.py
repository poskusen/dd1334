import math
class Vector:

    def __init__(self, firstpos, secondpos):
        self.firstpos = firstpos
        self.secondpos = secondpos

    def get_length(self):
        return math.sqrt((self.secondpos[0]-self.firstpos[0])^2 + (self.secondpos[1]-self.firstpos[1])^2)

    def get_extended_vector(self, size):
        return (self.secondpos, (self.secondpos[0] + self.secondpos[0] - self.firstpos[0], self.secondpos[1] + self.secondpos[1] - self.firstpos[1])) # Gör så att den är rätt längd

    def get_x_end(self):
        return self.secondpos[0]

    def get_y_end(self):
        return self.secondpos[1]

    def get_x_start(self):
        return self.firstpos[0]

    def get_y_start(self):
        return self.firstpos[1]
