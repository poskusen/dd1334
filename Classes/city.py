import random

class city:
    def __init__(self, population, reference_object, other_cities):
        self.population = population
        self.reference_object = reference_object
        pos_reference = reference_object.get_pos()
        vector_reference = random.choice(pos_reference)
        


        self.ypos = ypos
        self.xpos = xpos

    def get_pos(self):
        return (self.xpos,self.ypos)
    
    def get_population(self):
        return self.population