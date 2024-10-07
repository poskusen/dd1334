#from Classes.map import map
import math
from PIL import Image as img, ImageFont, ImageDraw
from Classes.continent import Continent
from Classes.continent import Node
from Classes.map import Map
import time
import random
from random import randint

color_text = (255, 255, 255, 0)

def draw_map(map, image_name = 'test_image.png'):
    (width, height) = map.get_mapsize()
    image = img.new("RGBA", (width, height), color='white')
    draw = ImageDraw.Draw(image)

    # Draw the blue ocean background first
    draw_oceans(draw, (width, height))

    continents = map.get_continents()
    rivers = []
    cities = []
    mountain_chains = []
    mountains = []
    roads = []
    villages = []

    for cont in continents:
        rivers.extend(cont.get_rivers().get_river_list())
        mountain_chains.extend(cont.get_mountain_chains().get_mountain_chains())
        mountains.extend(cont.get_mountains().get_mountain_list())
        villages.extend(cont.get_villages().get_cities_list())
        draw_continent(draw, cont)  # Draw continents after oceans

    for river in rivers:
        draw_river(draw, river)

    draw_names = map.draw_village_names()
    if draw_names:
        for village in villages:
            village_pos = village[0]
            village_size = 1
            village_name = village[1]
            draw_city(draw, village_pos, village_size, name = village_name, image=image)
    else:
        for village in villages:
            village_pos = village
            village_size = 1
            draw_city(draw, village_pos, village_size)

    for mountain_chain in mountain_chains:
        draw_mountain_chain(draw, mountain_chain)

    draw_names = map.draw_mountain_names()
    if not draw_names:
        for mountain in mountains:
            mountain_pos = mountain
            draw_mountain(draw, mountain_pos, 10, image=image)
    else:
        for mountain in mountains:
            mountain_pos = mountain[0]
            mountain_name = mountain[1]
            draw_mountain(draw, mountain_pos, 10, image=image, name = mountain_name)
    draw_realm_name(draw, image, map.get_realm_name(), (width, height))
    image.save(image_name)

    



def fill_continent(draw, continent, color=(0, 128, 0, 255)):
    list_points = continent.get_point_list()
    draw.polygon(list_points, fill=color)

def draw_continent(draw, continent):
    continent_width = 5
    colour_continent = (0, 100, 0)  # Outline color

    # Fill the continent
    fill_continent(draw, continent, color=(0, 180, 0))  # Fill with green

    list_points = continent.get_point_list()


    for i in range(0, len(list_points) - 1):
        draw_vector(draw, (list_points[i], list_points[i + 1]), continent_width, colour_continent)

    list_points = continent.get_point_list()

    for i in range(0, len(list_points) - 1):
        draw_vector(draw, (list_points[i], list_points[i + 1]), continent_width, colour_continent)


def draw_city(draw, pos, population, name=None, image=None):
    # Define colors
    hut_color = (139, 69, 19, 255)  # Brown color for the hut base
    roof_color = (255, 215, 0, 255)  # Yellow color for the roof (hayish)
    size = 10  # Base size for the hut, adjust as needed

    # Draw the square base of the hut
    hut_box = [
        (pos[0] - size // 2, pos[1] - size // 2),  # Bottom left
        (pos[0] + size // 2, pos[1] + size // 2)   # Top right
    ]
    draw.rectangle(hut_box, fill=hut_color)  # Draw the hut base

    # Draw the triangular roof on top
    roof = [
        (pos[0] - size // 2, pos[1] - size // 2),  # Bottom left (same as hut base)
        (pos[0], pos[1] - size),                     # Peak of the roof
        (pos[0] + size // 2, pos[1] - size // 2)   # Bottom right (same as hut base)
    ]
    draw.polygon(roof, fill=roof_color)  # Draw the roof

    # Draw the city name, if provided
    if name is not None:
        draw_text(image, pos, name, (1000, 1000), 1500)  # Optional: Draw the name


def draw_river(draw, river):
    # Define colors
    color_start = (0, 100, 255, 255)  # Start with a darker blue
    color_end = (173, 216, 230, 255)  # Light blue for the shallow areas
    base_size = 4  # Base width of the river

    for i in range(len(river) - 1):
        # Create a line segment from river[i] to river[i + 1]
        start_point = river[i]
        end_point = river[i + 1]

        # Calculate the control point for a gentle curve (less offset)
        control_x = (start_point[0] + end_point[0]) / 2  # Remove random offset
        control_y = (start_point[1] + end_point[1]) / 2 + random.randint(-5, 5)  # Slight Y-offset for some curvature

        # Draw the curved river using small line segments
        segments = 10  # Number of segments to approximate the curve
        previous_point = start_point  # Start with the first point

        for j in range(segments + 1):  # Include the last point
            # Interpolate between start_point and end_point
            t = j / segments
            curve_point = (
                (1 - t) * (1 - t) * start_point[0] + 2 * (1 - t) * t * control_x + t * t * end_point[0],
                (1 - t) * (1 - t) * start_point[1] + 2 * (1 - t) * t * control_y + t * t * end_point[1]
            )

            # Draw the line segment
            if j > 0:
                draw.line([previous_point, curve_point], fill=color_start, width=base_size)
            previous_point = curve_point

    # Optional: Add some reflection or shimmer effect
    for i in range(len(river) - 1):
        start_point = river[i]
        end_point = river[i + 1]
        shimmer_size = random.randint(1, 3)  # Random shimmer size
        draw.line([start_point[0], start_point[1] - shimmer_size, end_point[0], end_point[1] - shimmer_size],
                  fill=color_end, width=1)  # Light blue shimmer line



# draw_road(draw, road):
    #color_road = (0, 0, 255, 255)
    #size_road = 3
    #for vector in road:
        #draw_vector(draw, vector, size_road, color_road)

def draw_mountain_chain(draw, mountain_locations, size=3, color=(128, 128, 128, 255)):
    # Define colors
    mountain_color = color
    peak_color = (255, 255, 255, 255)  # White for the peak
    outline_color = (105, 105, 105, 255)  # Darker gray for the outline

    for location in mountain_locations:
        x, y = location

        # Calculate the points of the triangle (mountain)
        triangle = [
            (x, y - size),          # Top vertex
            (x - size, y + size),   # Bottom left vertex
            (x + size, y + size)    # Bottom right vertex
        ]

        # Draw the outline (darker gray) slightly offset downward
        outline_triangle = [
            (x, y - size + 2),      # Top vertex offset down
            (x - size, y + size + 2),  # Bottom left vertex offset down
            (x + size, y + size + 2)    # Bottom right vertex offset down
        ]
        draw.polygon(outline_triangle, fill=outline_color)

        # Draw the main mountain triangle
        draw.polygon(triangle, fill=mountain_color)

        # Draw the peak (white) with smaller size
        peak_size = size * 0.5  # Adjust the peak size (50% of the original)
        peak_triangle = [
            (x, y - peak_size),            # Adjusted top vertex
            (x - peak_size, y + size - peak_size),  # Adjusted bottom left vertex
            (x + peak_size, y + size - peak_size)   # Adjusted bottom right vertex
        ]
        draw.polygon(peak_triangle, fill=peak_color)




def draw_mountain(draw, pos, size, name=None, image=None):
    mountain_color = (128, 128, 128, 255)
    peak_color = (255, 255, 255, 255)  # White for the peak
    outline_color = (105, 105, 105, 255)  # Darker gray for the outline

    # Define the three vertices of the triangle (mountain)
    triangle = [
        (pos[0], pos[1] - size),          # Top vertex (peak)
        (pos[0] - size, pos[1] + size),   # Bottom left vertex
        (pos[0] + size, pos[1] + size)    # Bottom right vertex
    ]

    # Draw the outline (darker gray) slightly offset downward
    outline_triangle = [
        (pos[0], pos[1] - size + 2),          # Top vertex offset down
        (pos[0] - size, pos[1] + size + 2),   # Bottom left vertex offset down
        (pos[0] + size, pos[1] + size + 2)    # Bottom right vertex offset down
    ]
    draw.polygon(outline_triangle, fill=outline_color)

    # Draw the main mountain triangle
    draw.polygon(triangle, fill=mountain_color)

    # Draw the peak (white) at the very top, making it smaller
    peak_size = size * 0.2  # Adjust the peak size (30% of the original)
    peak_triangle = [
        (pos[0], pos[1] - size),              # Keep peak at the top
        (pos[0] - peak_size, pos[1] - size + peak_size),  # Adjusted bottom left vertex
        (pos[0] + peak_size, pos[1] - size + peak_size)   # Adjusted bottom right vertex
    ]
    draw.polygon(peak_triangle, fill = peak_color)

    if name is not None:
        draw_text(image, pos, name, (1000,1000), 1500)  # Optional: Draw the name

def draw_vector(draw, vector, size = 2, colour = (255, 0, 0, 255)): # Works
    draw.line(vector, fill = colour, width = size)
    
def draw_text(image, pos, text, size_canvas, object_size, font_name = 'arial.ttf', fill = 'black'):
    font_size = int((10/size_canvas[0])*object_size)
    font = ImageFont.load_default(font_size)
    # font = ImageFont.truetype(font_name, font_size)
    text_draw = ImageDraw.Draw(image)
    text_draw.text(pos, text, font = font, fill = fill)


def draw_oceans(draw, map_size):
    # Draw a gradient ocean background
    for y in range(map_size[1]):
        # Create a gradient effect from a darker blue at the top to a lighter blue at the bottom
        blue_intensity = int(30 + (y / map_size[1]) * (144 - 30))
        ocean_color = (0, blue_intensity, 255, 255)
        draw.line([(0, y), (map_size[0], y)], fill=ocean_color)

def draw_realm_name(draw, image, realm_name, size_canvas):
    pos = (size_canvas[0]/4, size_canvas[1]/50)
    font_realm = 'C:/Windows/Fonts/LHANDW.ttf'
    color_realm = 'black'
    draw_text(image, pos, realm_name, size_canvas, 5000, font_name = font_realm, fill = color_realm)




def test():
    mountain_names = ['mountain1', 'mountain2', 'mountain3']
    village_names = ['test1', 'test2', 'test3']
    karta = Map(3, 100, 50, 50, 50,  mapsize = (1000, 1000), mountain_names=mountain_names, village_names=village_names) #50 Is supposed to represent normal values
    draw_map(karta)

#test()