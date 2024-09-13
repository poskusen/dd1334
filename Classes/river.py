import matplotlib.pyplot as plt


class river:
    def __init__(self, continent, river_weight=100): #river_weight assumed to be value 1-100
        self.continent = continent
        self.river_weight = river_weight

        self.rivers_count = None
        self.river_list = None
        self.river_positions = None

        if self.rivers_count == None:
            river_percent = 0.4*river_weight/100 #Calculates how many vectors in continent that will have a river, max 40% (CAN BE CHANGED)
            self.rivers_count = int(self.count_vectors(self.continent)*river_percent) #Number of river can be dynamic by exchanging 0.25 with a user inserted value

        for i

    def generate_river(self):
        pass

    def count_vectors(self):
        """Return number of vectors in continent"""
        return len(self.continent)






def test():
    continent = [(500, 500), (561.0320489811663, 496.76426233680036), (614.6723780055507, 536.163370800318), (644.0822612505784, 567.1471724315649), (662.5499586980152, 585.7461098734568), (662.6786905682109, 586.1011225956856), (653.3303362417543, 618.954828820058), (625.7282457881066, 693.6354948271372), (613.4196220928332, 729.5127538935301), (597.3321915440589, 756.2401294664818), (574.4593951463479, 775.1386188767792), (562.0202255523436, 778.0442973529632), (506.75438593080906, 733.1540091973247), (503.18114278654167, 729.5095661794837), (455.53683199771416, 707.8886412192259), (444.2925867059378, 694.7874314835107), (439.8039075548508, 619.0313982222536), (455.64769693279703, 568.5868069515998), (484.29588455909953, 562.1353332826781), (500, 500)]

    test_river = river(continent)
    print(test_river.count_vectors())

test()