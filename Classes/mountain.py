import matplotlib.pyplot as plt
import random
import math
from matplotlib.path import Path


class Mountain():

    def __init__(self, continent, mountain_scale = 100):

        self.continent = continent
        self.mountain_scale = mountain_scale

        self.mountains_count = None

        self.mountains_list = [] #A list containing lists of the mountain ranges, A position in this list represent a mountain range, that position has a list in it with scattered positions of mountains

        # Create a Path object from the continent coordinates
        self.path = Path(self.continent)

        if self.mountains_count is None:
            self.mountains_count = int(len(self.continent)*0.4*self.mountain_scale/100)

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
                        x_point = random.gauss(mountain_cords[0], 8)
                        y_point = random.gauss(mountain_cords[1], 5)

                        mountain = (x_point, y_point)

                        if self.is_point_inside_continent(mountain):
                            mountains.append((x_point, y_point))

                    self.mountains_list.append(mountains)

                    break  # Exit the while loop if the point is valid

    def is_point_inside_continent(self, point):
        """Checks if a point is inside the continent defined by its vertices."""
        from matplotlib.path import Path

        path = Path(self.continent)
        return path.contains_point(point)








def test():
    continent = [(500, 500), (561, 496), (614, 536),
                 (644, 567), (662, 585), (662, 586),
                 (653, 618), (625, 693), (613, 729),
                 (597, 756), (574, 775), (562, 778),
                 (506, 733), (503, 729), (455, 707),
                 (444, 694), (439, 619), (455, 568),
                 (484, 562), (500, 500)]

    river_lists = [[(449.914709351826, 701.3380363513683), (454.7088970390462, 696.0816365303778), (456.7088970390462, 694.0816365303778), (461.7088970390462, 691.0816365303778), (464.7088970390462, 687.0816365303778), (466.7088970390462, 682.0816365303778), (467.7088970390462, 679.0816365303778), (471.7088970390462, 674.0816365303778), (476.7088970390462, 670.0816365303778), (481.7088970390462, 666.0816365303778), (482.7088970390462, 665.0816365303778), (485.7088970390462, 663.0816365303778), (489.7088970390462, 658.0816365303778), (493.7088970390462, 654.0816365303778), (494.7088970390462, 653.0816365303778), (497.7088970390462, 652.0816365303778), (500.7088970390462, 652.0816365303778), (504.7088970390462, 654.0816365303778), (507.7088970390462, 658.0816365303778), (509.7088970390462, 661.0816365303778), (512.7088970390462, 666.0816365303778), (513.7088970390462, 671.0816365303778), (517.7088970390462, 676.0816365303778), (520.7088970390462, 680.0816365303778), (523.7088970390462, 682.0816365303778), (527.7088970390462, 683.0816365303778), (532.7088970390462, 682.0816365303778), (536.7088970390462, 683.0816365303778), (541.7088970390462, 683.0816365303778), (544.7088970390462, 682.0816365303778), (548.7088970390462, 680.0816365303778), (549.7088970390462, 679.0816365303778), (551.7088970390462, 675.0816365303778), (552.7088970390462, 671.0816365303778), (553.7088970390462, 666.0816365303778), (557.7088970390462, 661.0816365303778), (561.7088970390462, 657.0816365303778), (566.7088970390462, 652.0816365303778), (569.7088970390462, 649.0816365303778), (571.7088970390462, 646.0816365303778), (575.7088970390462, 641.0816365303778), (579.7088970390462, 637.0816365303778), (583.7088970390462, 633.0816365303778), (587.7088970390462, 631.0816365303778), (592.7088970390462, 628.0816365303778), (596.7088970390462, 627.0816365303778), (601.7088970390462, 628.0816365303778), (605.7088970390462, 630.0816365303778), (607.7088970390462, 630.0816365303778), (610.7088970390462, 630.0816365303778), (614.7088970390462, 630.0816365303778)], [(639.5292910149304, 656.2951618235976), (629.8393739398264, 649.5617611692053), (627.8393739398264, 645.5617611692053), (625.8393739398264, 641.5617611692053), (620.8393739398264, 637.5617611692053), (618.8393739398264, 635.5617611692053), (614.8393739398264, 631.5617611692053), (609.8393739398264, 626.5617611692053), (607.8393739398264, 624.5617611692053), (603.8393739398264, 619.5617611692053), (601.8393739398264, 617.5617611692053), (598.8393739398264, 612.5617611692053), (597.8393739398264, 610.5617611692053), (597.8393739398264, 608.5617611692053), (597.8393739398264, 606.5617611692053), (595.8393739398264, 602.5617611692053), (595.8393739398264, 601.5617611692053), (594.8393739398264, 597.5617611692053), (594.8393739398264, 594.5617611692053), (595.8393739398264, 590.5617611692053), (599.8393739398264, 585.5617611692053), (603.8393739398264, 580.5617611692053), (605.8393739398264, 575.5617611692053), (608.8393739398264, 570.5617611692053), (609.8393739398264, 566.5617611692053), (610.8393739398264, 562.5617611692053), (611.8393739398264, 560.5617611692053), (613.8393739398264, 558.5617611692053), (617.8393739398264, 554.5617611692053), (620.8393739398264, 550.5617611692053), (622.8393739398264, 548.5617611692053), (624.8393739398264, 547.5617611692053)], [(605.3759068184461, 742.8764416800059), (596.0920530633523, 739.2979543317786), (591.0920530633523, 739.2979543317786), (586.0920530633523, 737.2979543317786), (584.0920530633523, 736.2979543317786), (580.0920530633523, 736.2979543317786), (576.0920530633523, 735.2979543317786), (571.0920530633523, 736.2979543317786), (570.0920530633523, 736.2979543317786), (566.0920530633523, 738.2979543317786), (562.0920530633523, 739.2979543317786), (560.0920530633523, 739.2979543317786), (558.0920530633523, 738.2979543317786), (554.0920530633523, 735.2979543317786), (553.0920530633523, 733.2979543317786), (550.0920530633523, 729.2979543317786), (545.0920530633523, 725.2979543317786), (544.0920530633523, 724.2979543317786), (542.0920530633523, 723.2979543317786), (537.0920530633523, 721.2979543317786), (532.0920530633523, 717.2979543317786), (529.0920530633523, 715.2979543317786), (524.0920530633523, 712.2979543317786), (520.0920530633523, 709.2979543317786), (519.0920530633523, 707.2979543317786), (516.0920530633523, 705.2979543317786), (511.0920530633523, 704.2979543317786), (506.0920530633523, 705.2979543317786), (501.0920530633523, 706.2979543317786), (498.0920530633523, 707.2979543317786), (495.0920530633523, 708.2979543317786), (491.0920530633523, 708.2979543317786), (486.0920530633523, 706.2979543317786), (481.0920530633523, 702.2979543317786), (478.0920530633523, 699.2979543317786), (477.0920530633523, 696.2979543317786), (473.0920530633523, 692.2979543317786), (470.0920530633523, 690.2979543317786), (465.0920530633523, 689.2979543317786), (461.0920530633523, 690.2979543317786), (456.0920530633523, 690.2979543317786), (451.0920530633523, 688.2979543317786), (447.0920530633523, 688.2979543317786)], [(568.2398103493458, 776.5914581148712), (568.1024723690529, 767.7225298633375), (570.1024723690529, 762.7225298633375), (574.1024723690529, 757.7225298633375), (575.1024723690529, 753.7225298633375), (575.1024723690529, 752.7225298633375), (575.1024723690529, 748.7225298633375), (574.1024723690529, 746.7225298633375), (574.1024723690529, 743.7225298633375), (575.1024723690529, 741.7225298633375), (578.1024723690529, 738.7225298633375), (582.1024723690529, 736.7225298633375), (587.1024723690529, 735.7225298633375), (592.1024723690529, 736.7225298633375), (593.1024723690529, 736.7225298633375), (595.1024723690529, 736.7225298633375), (598.1024723690529, 735.7225298633375), (601.1024723690529, 735.7225298633375), (602.1024723690529, 735.7225298633375), (604.1024723690529, 736.7225298633375), (608.1024723690529, 737.7225298633375)], [(500.0, 500.0), (519.0, 499.0), (521.0, 500.0), (526.0, 500.0), (539.0, 499.0), (543.0, 498.0)], [(447.7258022438239, 593.8091025869267), (457.4960473177356, 600.3073555478186), (459.4960473177356, 604.3073555478186), (460.4960473177356, 606.3073555478186), (460.4960473177356, 608.3073555478186), (460.4960473177356, 610.3073555478186), (462.4960473177356, 614.3073555478186), (462.4960473177356, 616.3073555478186), (460.4960473177356, 620.3073555478186), (457.4960473177356, 625.3073555478186), (456.4960473177356, 626.3073555478186), (452.4960473177356, 630.3073555478186), (448.4960473177356, 632.3073555478186), (447.4960473177356, 632.3073555478186), (442.4960473177356, 634.3073555478186)]]

    village_locations = [(573.1024723690529, 757.7225298633375), (595.8393739398264, 602.5617611692053), (565.0920530633523, 737.2979543317786), (626.8393739398264, 640.5617611692053), (455.7088970390462, 695.0816365303778), (572.0920530633523, 736.2979543317786), (536.7088970390462, 683.0816365303778), (520.0, 498.0), (628.8393739398264, 649.5617611692053), (462.4960473177356, 614.3073555478186), (503, 729), (455, 707), (561, 496), (500, 500), (444, 694), (455, 568), (614, 536), (570.1855482075314, 552.1553135567679), (617.8998865596157, 547.7333835138373), (508.7432089011054, 540.4923408125211), (580.6185647255785, 582.3698554122053), (514.0437057818187, 510.12796134438804), (528.2575040701946, 698.0638985657672), (579.9361384418568, 683.7506247909023)]

    berg = Mountain(continent=continent)
    berg.generate_mountain_range()



test()