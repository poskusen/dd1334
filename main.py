from Classes.map import Map
<<<<<<< HEAD

=======
#from Classes.map import map
import math
from PIL import Image as img



def draw(map):
    size = (1000,1000)
    new_image = img.new('RGB', size, color='white')
    canvas = new_image.load()
    new_vector_1 = ((100,200),(200,300))
    new_vector_2 = ((100,200),(50,300))
    new_vector_3 = ((100,200),(200,100))
    new_vector_4 = ((100,200),(50,100))

    draw_vector(canvas, new_vector_1, (255,0,0), 8)
    #draw_vector(canvas, new_vector_2, (255,255,0), 1)
    #draw_vector(canvas, new_vector_3, (255,0,255), 1)
    #draw_vector(canvas, new_vector_4, (0,255,255), 1)

    new_image.save('test_image.png')

def draw_vector(canvas, vector, colour, size): #Works
    ''' draws a vector on the canvas '''
    distance_x = vector[1][0] - vector[0][0]
    distance_y = vector[1][1] - vector[0][1]
    loop = 0
    xloop = True

    if abs(distance_x) > abs(distance_y): #Check if x or y is changed the most, to draw using that as loop variable.
        loop = distance_x
        x_loop = True
    else:
        loop = distance_y
        x_loop = False

    start_x = vector[0][0]
    start_y = vector[0][1]
    if x_loop: #check which direction to draw in and if we are going backwards or forwards.
        angle = distance_y/distance_x
        if distance_x > 0:
            step = 1
        else:
            step = -1
        for i in range(0, loop, step):
            for j in range(1, size + 1):
                canvas[start_x + i, start_y + round(i*angle) + j] = colour
    else:
        angle = distance_x/distance_y
        if distance_y > 0:
            step = 1
        else:
            step = -1
        for i in range(0, loop, step):
                for j in range(1,size+1):
                    canvas[start_x + round(i*angle) + j, start_y + i] = colour





def main():
    map = Map()
    map.generatemapsize()
    draw()

main()
>>>>>>> ff119dff761eeeb28a2e69d9bb0c9a8d2425f8bc
