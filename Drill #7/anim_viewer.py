from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('dora.png')
x = 0
frame = 0

while (x < 800):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 245, 0, 245, 313, x, 190)
    update_canvas()
    frame = (frame + 1) % 4
    x += 5
    delay(0.05)
    get_events()

close_canvas()
