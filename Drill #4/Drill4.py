import turtle

line = 0

while (line < 6):
    turtle.goto(0, 100*line)
    turtle.pendown()
    turtle.forward(500)
    line = line+1
    turtle.penup()

line = 0
turtle.left(90)

while (line < 6):
    turtle.goto(100*line, 0)
    turtle.pendown()
    turtle.forward(500)
    line = line+1
    turtle.penup()

turtle.exitonclick()
   

    
