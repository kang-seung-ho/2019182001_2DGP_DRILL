from pico2d import *
open_canvas()

character=load_image('sprite.png')
frame=0

def render(location, x,y ,frame):
    clear_canvas()
    character.clip_draw(frame*60,location,60,60,x,y,120,120)
    update_canvas()
    frame=(frame+1)%8
    delay(0.01)
    get_events()

for x in range(20,750+1,5):
    frame=(frame+1)%8
    render(60,x,40,frame)

for y in range(0,550+1,5):
    frame=(frame+1)%8
    render(0,750,y,frame)
    

for x in range(750,20-1,-5):
    frame=(frame+1)%8
    render(120,x,550,frame)
    
for y in range(550,40-1,-5):
    frame=(frame+1)%8
    render(180,20,y,frame)

close_canvas()
