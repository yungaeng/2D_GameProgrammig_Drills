from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

grass.draw_now(400,30)
character.draw_now(400,90)

x=400
y=90

th = 0
r = 250

while(x<800):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,90)
    x = x + 2
    delay(0.001)

while(y<600):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(800,y)
    y = y + 2
    delay(0.001)

while(x>0):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,600)
    x = x - 2
    delay(0.001)

while(y>0):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(0,y)
    y = y - 2
    delay(0.001)

while(x<400):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,90)
    x = x + 2
    delay(0.001)

for th in range(0,360):
    clear_canvas_now()
    grass.draw_now(400,30)
    x = math.sin(th) * r
    y = math.cos(th) * r
    character.draw_now(400 + x,300 + y)
    th = th + 1
    delay(0.5)

close_canvas()


