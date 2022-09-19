import turtle as t

def top():
    t.setheading(90)
    t.forward(50)
    t.stampe()

def down():
    t.setheading(270)
    t.forward(50)
    t.stampe()

def left():
    t.setheading(180)
    t.forward(50)
    t.stampe()

def right():
    t.setheading(0)
    t.forward(50)
    t.stampe()

def restart():
    t.reset()

t.shape("turtle")

t.onkeypress(top, 'w')
t.onkeypress(down, 's')
t.onkeypress(left, 'a')
t.onkeypress(right, 'd')
t.onkeypress(restart, 'Escape')

t.listen()
