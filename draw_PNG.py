from PIL import Image as img, ImageFont, ImageDraw
from Classes.map import Map
import random


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
            village_name = village[1]
            draw_city(draw, village_pos, name = village_name, image=image)
    else:
        for village in villages:
            village_pos = village
            village_size = 1
            draw_city(draw, village_pos, image=image)

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
    colour_continent = (0, 100, 0)
    fill_continent(draw, continent, color=(0, 180, 0))
    list_points = continent.get_point_list()

    for i in range(0, len(list_points) - 1):
        draw_vector(draw, (list_points[i], list_points[i + 1]), continent_width, colour_continent)

    list_points = continent.get_point_list()
    for i in range(0, len(list_points) - 1):
        draw_vector(draw, (list_points[i], list_points[i + 1]), continent_width, colour_continent)


def draw_city(draw, pos, name=None, image=None):
    # Define colors
    hut_color = (139, 69, 19, 255)
    roof_color = (255, 215, 0, 255)
    size = 10

    hut_box = [
        (pos[0] - size // 2, pos[1] - size // 2),
        (pos[0] + size // 2, pos[1] + size // 2)
    ]
    draw.rectangle(hut_box, fill=hut_color)


    roof = [
        (pos[0] - size // 2, pos[1] - size // 2),
        (pos[0], pos[1] - size),
        (pos[0] + size // 2, pos[1] - size // 2)
    ]
    draw.polygon(roof, fill=roof_color)
    if name is not None:
        draw_text(image, pos, name, (1000, 1000), 1500)


def draw_river(draw, river):
    # Define colors
    color_start = (0, 100, 255, 255)
    color_end = (173, 216, 230, 255)
    base_size = 4

    for i in range(len(river) - 1):

        start_point = river[i]
        end_point = river[i + 1]


        control_x = (start_point[0] + end_point[0]) / 2  # Remove random offset
        control_y = (start_point[1] + end_point[1]) / 2 + random.randint(-5, 5)


        segments = 10
        previous_point = start_point

        for j in range(segments + 1):

            t = j / segments
            curve_point = (
                (1 - t) * (1 - t) * start_point[0] + 2 * (1 - t) * t * control_x + t * t * end_point[0],
                (1 - t) * (1 - t) * start_point[1] + 2 * (1 - t) * t * control_y + t * t * end_point[1]
            )

            if j > 0:
                draw.line([previous_point, curve_point], fill=color_start, width=base_size)
            previous_point = curve_point

    for i in range(len(river) - 1):
        start_point = river[i]
        end_point = river[i + 1]
        shimmer_size = random.randint(1, 3)
        draw.line([start_point[0], start_point[1] - shimmer_size, end_point[0], end_point[1] - shimmer_size],
                  fill=color_end, width=1)

def draw_mountain_chain(draw, mountain_locations, size=3, color=(128, 128, 128, 255)):

    mountain_color = color
    peak_color = (255, 255, 255, 255)
    outline_color = (105, 105, 105, 255)

    for location in mountain_locations:
        x, y = location

        triangle = [
            (x, y - size),
            (x - size, y + size),
            (x + size, y + size)
        ]


        outline_triangle = [
            (x, y - size + 2),
            (x - size, y + size + 2),
            (x + size, y + size + 2)
        ]
        draw.polygon(outline_triangle, fill=outline_color)


        draw.polygon(triangle, fill=mountain_color)


        peak_size = size * 0.5
        peak_triangle = [
            (x, y - peak_size),
            (x - peak_size, y + size - peak_size),
            (x + peak_size, y + size - peak_size)
        ]
        draw.polygon(peak_triangle, fill=peak_color)

def draw_mountain(draw, pos, size, name=None, image=None):
    mountain_color = (128, 128, 128, 255)
    peak_color = (255, 255, 255, 255)
    outline_color = (105, 105, 105, 255)


    triangle = [
        (pos[0], pos[1] - size),
        (pos[0] - size, pos[1] + size),
        (pos[0] + size, pos[1] + size)
    ]


    outline_triangle = [
        (pos[0], pos[1] - size + 2),
        (pos[0] - size, pos[1] + size + 2),
        (pos[0] + size, pos[1] + size + 2)
    ]
    draw.polygon(outline_triangle, fill=outline_color)


    draw.polygon(triangle, fill=mountain_color)


    peak_size = size * 0.2  # Adjust the peak size (30% of the original)
    peak_triangle = [
        (pos[0], pos[1] - size),
        (pos[0] - peak_size, pos[1] - size + peak_size),
        (pos[0] + peak_size, pos[1] - size + peak_size)
    ]
    draw.polygon(peak_triangle, fill = peak_color)

    if name is not None:
        draw_text(image, pos, name, (1000,1000), 1500)

def draw_vector(draw, vector, size = 2, colour = (255, 0, 0, 255)): # Works
    draw.line(vector, fill = colour, width = size)
    
def draw_text(image, pos, text, size_canvas, object_size, font_name='arial.ttf', fill='black'):
    font_size = int((10 / size_canvas[0]) * object_size)
    try:
        font = ImageFont.truetype(font_name, font_size)
    except IOError:
        font = ImageFont.load_default()

    text_draw = ImageDraw.Draw(image)
    text_draw.text(pos, text, font=font, fill=fill)



def draw_oceans(draw, map_size):

    for y in range(map_size[1]):

        blue_intensity = int(30 + (y / map_size[1]) * (144 - 30))
        ocean_color = (0, blue_intensity, 255, 255)
        draw.line([(0, y), (map_size[0], y)], fill=ocean_color)


def draw_realm_name(draw, image, realm_name, size_canvas):
    pos = (size_canvas[0]/4, size_canvas[1]/50)
    font_realm = 'C:/Windows/Fonts/LHANDW.ttf'
    color_realm = 'black'
    draw_text(image, pos, realm_name, size_canvas, 5000, font_name = font_realm, fill = color_realm)
