#from Classes.map import map
import math
from PIL import Image as img, ImageFont, ImageDraw
from Classes.continent import Continent
from Classes.continent import Node
import time
def draw_map(map):
    (width, height) = map.get_mapsize()
    image = img.new("RGBA", (width, height), color = 'white')
    draw = ImageDraw.Draw(image)
    continents = map.get_continents()
    rivers = []
    cities = []
    mountains = []
    roads = []
    villages = []
    for cont in continents:
        rivers = rivers + cont.get_rivers()
        cities = cities + cont.get_cities()
        mountains = mountains + cont.get_mountains()
        roads = roads + cont.get_roads()
        villages = villages + cont.get_villages()
        draw_continent(draw, cont)
    

def draw_continent(draw, continent):
    continent_width = 4
    colour_continent = (255,0,0)

    list_points = continent.get_point_list()
    start = time.time()
    for i in range(0, len(list_points) - 1):
        draw_vector(draw, (list_points[i], list_points[i + 1]), continent_width, colour_continent)
    end = time.time()
    print('kontinent: ' + end - start)

def draw_city(draw, pos, population):
    pass

def draw_river(canvas, pos, size, size_canvas):
    pass

def draw_mountain(canvas, pos, size, size_canvas):
    pass

def
    
def draw_vector(draw, vector, size = 2, colour = (255, 0, 0, 255)): # Works
    draw.line(vector, fill = colour, width = size)
    
def draw_text(image, pos, text, size_canvas, object_size):
    font_size = int((10/size_canvas)*object_size)
    font = ImageFont.truetype("arial.ttf", font_size)
    text_draw = ImageDraw.Draw(image)
    text_draw.text(pos, text, font = font, fill = 'black')


    
def main():
    draw_map()

main()