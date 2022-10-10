import pico2d
import logo_state
import play_state

pico2d.open_canvas()

states = [logo_state, play_state]
for state in states:
    state.enter()
while state.running:
    states.handle_events()
    states.update()
    states.draw()
    states.exit()

pico2d.close_canvas()