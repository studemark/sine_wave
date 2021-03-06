#Code by Stuart Demarkles
#Program that generates a sine wave which is made up of 20 random waves
#You can change num_waves to generage any number of waves

import random
y_size = 600
y_offset = y_size / 2
move = 20
num_waves = 0  #Number of waves is from 0

sinlists = []

def add_sin_list(sin_param):
    sin_param.insert(0, (random.randrange(1, 50), random.randrange(10, 1000))) #(sin amplitude, sin period)

def mult_sins(sin_param):
    sinlists.append(sin_param)

def setup():
    size(1200, 600)
    noStroke()
    frameRate(60)
    global r
    global g
    global b
    global num_waves
    r = random.randrange(0, 250)
    g = random.randrange(0, 250)
    b = random.randrange(0, 250)
    sin_counter = 0
    sin_count2 = 0
    sin_param = []
    while sin_counter <= num_waves:
        while sin_count2 <= 19:
            add_sin_list(sin_param)
            sin_count2 += 1
        mult_sins(sin_param)
        sin_param = []
        #print(len(sin_param))
        sin_counter += 1
        sin_count2 = 0
        
def draw():
    global sinlists
    global y_offset
    global move
    global num_waves
    global r
    global g
    global b
    comp_counter = 0
    comp2 = 0
    background(0, 0, 0)
    fill(r, g, b)
    while comp2 <= num_waves:
        for center_x in range(0, 1210, 20):
            center_y = 0
            comp_counter = 0
            while comp_counter <= 19:
                center_y += ((sin((center_x + move) * PI / sinlists[comp2][comp_counter][1])) * sinlists[comp2][comp_counter][0])   
                comp_counter += 1
            y = y_offset - center_y                                              #Simple axis computations, resulting in a 'y-axis'
            ellipse(center_x, y, 20, 20)                                        #Drawing the ellipses based on the sin wave function
        #print(y)
        comp2 += 1
    move += 2

 