from pico2d import *

class Background1:
    def __init__(self):
        self.image = load_image('background1.png')

    def draw(self):
        self.image.draw(400, 30)

class Background2:
    def __init__(self):
        self.image = load_image('background2.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('char_sheet.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 1

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()


boy = Boy()
grass = Grass()
running = True

# game main loop code
while running:
    handle_events()

    boy.update()

    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()

    delay(0.05)

# finalization code
close_canvas()
