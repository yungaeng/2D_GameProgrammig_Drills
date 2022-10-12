import game_framework
import title_state
from pico2d import *

class Background:
    def __init__(self):
        self.image = load_image('background1.png')

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
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
    delay(0.01)

boy = None
backgound = None
running = True


def enter():
    global boy, background, running
    boy = Boy()
    backgound = Background()
    running = True

def playexiit():
    global boy, background, running
    del boy
    del backgound

def update():
    boy.update()

def draw():
    clear_canvas()
    backgound.draw()
    boy.draw()
