from pico2d import *
import math
open_canvas()

grass=load_image('grass.png')
character=load_image('character.png')

x1=100
y1=100
x=0
y=0
angle=12
while(True):
    clear_canvas_now()
    grass.draw_now(400,30)   
    x=x1+200*math.cos(math.radians(angle))
    y=y1+200*math.sin(math.radians(angle))
    character.draw_now(x+300,y+200)
    angle=angle+12
    delay(0.01)
    


