import turtle
def drawSnake(rad,angle,len,neckrad):
    for i in range(len):
        turtle.circle(rad,angle)
        turtle.circle(-rad,angle*8)
    turtle.circle(rad,angle/2)
    turtle.forward(rad/2)
    turtle.circle(neckrad,40)
    turtle.forward(rad/4)


if __name__ == "__main__":
    turtle.setup(1500,1400,0,0)
    turtle.pensize(5)
    turtle.pencolor('blue')
    turtle.seth(-40)
    drawSnake(50,270,15,15)
