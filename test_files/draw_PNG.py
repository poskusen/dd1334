#from Classes.map import map
import math
from PIL import Image as img, ImageFont, ImageDraw
from test_files.continent_gammal import Continent
from test_files.continent_gammal import Node
import time

def draw():
   
    size = (1000,1000)
    new_image = img.new('RGB', size, color='white')
    
    draw = ImageDraw.Draw(new_image)
    new_vector_1 = ((100,200),(200,300))
    new_vector_2 = ((100,200),(50,300))
    new_vector_3 = ((100,200),(200,100))
    new_vector_4 = ((100,200),(50,100))
    line_color = (255, 0, 0, 255)
    

    
    #draw_vector(canvas, new_vector_2, (255,255,0), 1)
    #draw_vector(canvas, new_vector_3, (255,0,255), 1)
    #draw_vector(canvas, new_vector_4, (0,255,255), 1)
    #draw_text(new_image, (500, 700), 'OsvaldBurg', 1000, 1000)

    new_image.save('test_image.png')
    

def draw_continent():
    start = time.time()
    size = (1000,1000)
    new_image = img.new('RGB', size, color='white')
    canvas = new_image.load()
    new_cont = Continent('test', (1000, 1000), 100)
    new_cont.generate()
    start_node = new_cont.get_start_node()
    first_node = start_node
    second_node = first_node.get_next()
    i = 0
    while first_node is not start_node or i == 0:
        draw_vector(canvas, (first_node.get_data(), second_node.get_data()), (255,0,0), 4)
        first_node = second_node
        second_node = second_node.get_next()
        i += 1
    new_image.save('test_image.png')
    end = time.time()
    print(end - start)
    
def draw_vector(image_object, vector, size, colour = (255, 0, 0, 255)): # Works
    draw = ImageDraw.Draw(image_object)
    draw.line(vector, fill=colour, size=2)
    ''' draws a vector on the canvas '''
    distance_x = int(vector[1][0] - vector[0][0])
    distance_y = int(vector[1][1] - vector[0][1])
    loop = 0
    xloop = True

    if abs(distance_x) > abs(distance_y): # Check if x or y is changed the most, to draw using that as loop variable.
        loop = distance_x
        x_loop = True
    else:
        loop = distance_y
        x_loop = False

    start_x = vector[0][0]
    start_y = vector[0][1]
    if x_loop: # check which direction to draw in and if we are going backwards or forwards.
        try:
            angle = distance_y/distance_x
        except:
            angle = 0
        if distance_x > 0:
            step = 1
        else:
            step = -1
        for i in range(-step, loop, step): 
            for j in range(1, size + 1): # add thickness
                canvas[start_x + i, start_y + round(i*angle) + j] = colour
    else:
        try:
            angle = distance_x/distance_y
        except:
            angle = 0
        if distance_y > 0:
            step = 1
        else:
            step = -1
        for i in range(-step, loop, step): 
                for j in range(1,size+1): # add thickness
                    canvas[start_x + round(i*angle) + j, start_y + i] = colour

def draw_text(image, pos, text, size_canvas, object_size):
    font_size = int((10/size_canvas)*object_size)
    font = ImageFont.truetype("arial.ttf", font_size)
    text_draw = ImageDraw.Draw(image)
    text_draw.text(pos, text, font = font, fill = 'black')



def draw_city(canvas, pos, size, size_canvas):
    pass
    



def main():
    draw()

main()