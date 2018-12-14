import turtle
import time

turtle.pensize(7)
turtle.pencolor('green')
turtle.fillcolor('blue')

turtle.begin_fill()


for i in range(100):
    turtle.forward(25)
    turtle.right(325)

turtle.end_fill()
time.sleep(2)

turtle.penup()
turtle.goto(-150,-120)
turtle.color('violet')
turtle.write('Done',font=('Arial',40,'bold'))
time.sleep(1)
