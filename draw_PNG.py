#from Classes.map import map
import math
from PIL import Image as img, ImageFont, ImageDraw
from Classes.continent import Continent
from Classes.continent import Node
import time

color_text = (255, 255, 255, 0)

def draw_map(map):
    start = time.time()
    (width, height) = map.get_mapsize()
    image = img.new("RGBA", (width, height), color = 'white')
    draw = ImageDraw.Draw(image)
    size_map = map.get_mapsize()

    continents = map.get_continents()
    rivers = []
    cities = []
    mountain_chains = []
    mountains = []
    roads = []
    villages = []
    for cont in continents:
        rivers = rivers + cont.get_rivers()
        cities = cities + cont.get_cities()
        mountain_chains = mountain_chains + cont.get_mountain_chains()
        mountains = mountains + cont.get_mountains()
        roads = roads + cont.get_roads()
        villages = villages + cont.get_villages()
        draw_continent(draw, cont)

    for river in rivers:
        draw_river(draw, river)

    for city in cities:
        city_size = city[1]
        city_pos = city[0]
        city_name = city[2]
        draw_city(draw, city_pos, city_size, name = city_name, image = image)

    for village in villages:
        village_pos = village[0]
        village_size = village[1]
        draw_city(draw, village_pos, village_size)

    for road in roads:
        draw_road(draw, road)

    for mountain_chain in mountain_chains:
        draw_mountain_chain(draw, mountain_chain)

    for mountain in mountains:
        mountain_pos = mountain[0]
        mountain_size = mountain[1]
        mountain_name = mountain[2]
        draw_mountain(draw, mountain_pos, mountain_size, name = mountain_name, image = image)

    draw_oceans(size_map, image, draw, continents)
    image.show()
    image.save('test_image.png')
    end = time.time()
    print('Göra karta tid: ' + end - start)
    

def draw_continent(draw, continent):
    continent_width = 4
    colour_continent = (255,0,0)

    list_points = continent.get_point_list()
    
    for i in range(0, len(list_points) - 1):
        draw_vector(draw, (list_points[i], list_points[i + 1]), continent_width, colour_continent)
    

def draw_city(draw, pos, population, name = None, image = None):
    city_color = (0, 0, 255, 255)
    pos = (250, 250)  # Center of the dot
    size = population/100  # Radius of the dot

# Define the bounding box for the ellipse (circle)
    bounding_box = [
        (pos[0] - size, pos[1] - size), 
        (pos[0] + size, pos[1] + size)   
    ]
    
    draw.ellipse(bounding_box, fill=city_color)

    if name is not None:
        draw_text(image, pos, name, 1000, size)

def draw_river(draw, river):
    color_river = (0, 0, 255, 255)
    size_river = 3
    for vector in river:
        draw_vector(draw, vector, size_river, color_river)

def draw_road(draw, road):
    color_road = (0, 0, 255, 255)
    size_road = 3
    for vector in road:
        draw_vector(draw, vector, size_road, color_road)

def draw_mountain_chain(draw, vector): #Olika storlekar på berg längs med vektorn
    pass

def draw_mountain(draw, pos, size, name = None, image = None): #implementera snyggar berg
    mountain_color = (0, 0, 255, 255)
   
   # Radius of the dot

    # Define the bounding box for the ellipse (circle)
    bounding_box = [
        (pos[0] - size, pos[1] - size), 
        (pos[0] + size, pos[1] + size)   
    ]
    
    draw.ellipse(bounding_box, fill = mountain_color)

    if name is not None:
        draw_text(image, pos, name, 1000, size) # Fixa size och canvas_size
    


    
def draw_vector(draw, vector, size = 2, colour = (255, 0, 0, 255)): # Works
    draw.line(vector, fill = colour, width = size)
    
def draw_text(image, pos, text, size_canvas, object_size):
    font_size = int((10/size_canvas)*object_size)
    font = ImageFont.truetype("arial.ttf", font_size)
    text_draw = ImageDraw.Draw(image)
    text_draw.text(pos, text, font = font, fill = 'black')

def draw_oceans(map_size, image, draw, continents):

    mask = img.new("L", (map_size[0],map_size[1]), 0)

    draw_mask = ImageDraw.Draw(mask)

    areas = []
    for cont in continents:
        areas.append(cont.get_list_point())

    for area in areas:
       draw_mask.polygon(area, fill=255)

    inverted_mask = img.eval(mask, lambda x: 255 - x)

    
    draw.bitmap((0, 0), inverted_mask, fill="blue")

    image.paste("white", (0, 0), mask=mask)


    
def main():
    draw_map()

main()