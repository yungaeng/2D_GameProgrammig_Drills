from pico2d import *


open_canvas()
background = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
Rrunning = False
Lrunning = False
x = 800//2
y = 600//2
frame = 0
xdir = 0
ydir = 0
pex = True

def handle_events():
    global Lrunning
    global Rrunning
    global x
    global y
    global xdir
    global ydir
    global pex
    events = get_events()
    for event in events:

        if event.type == SDL_QUIT:
            pex = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            pex = False

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                xdir += 1
                Rrunning = True
            elif event.key == SDLK_LEFT:
                Lrunning = True
                xdir -= 1
            elif event.key == SDLK_UP:
                ydir += 1
            elif event.key == SDLK_DOWN:
                ydir -= 1
            elif event.key == SDLK_ESCAPE:
                Rrunning = False
                Lrunning = False

        elif event.type == SDL_KEYUP:
            running = False
            if event.key == SDLK_RIGHT:
                xdir -= 1
            elif event.key == SDLK_LEFT:
                xdir += 1
            elif event.key == SDLK_UP:
                ydir -= 1
            elif event.key == SDLK_DOWN:
                ydir += 1

    pass


while pex:
    clear_canvas()
    background.draw(200, 100)
    if Rrunning == True:
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
    elif Lrunning == True:
        character.clip_draw(frame * 0, 0, 100, 100, x, y)
    elif Rrunning == False:
        character.clip_draw(frame * 100, 200, 100, 100, x, y)
    elif Rrunning == False:
        character.clip_draw(frame * 100, 150, 100, 100, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    x += xdir * 5
    y += ydir * 4
    delay(0.01)
close_canvas()

