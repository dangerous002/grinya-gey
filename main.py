import turtle
import random

def printGrinya(t):
    t.speed(2)
    #буква г
    t.penup()
    t.setpos(-375, 250)
    t.pendown()
    t.pensize(20)
    t.pencolor('#08d453')
    t.forward(100)
    t.backward(100)
    t.right(90)
    t.forward(200)
    #буква р
    t.penup()
    t.left(90)
    t.forward(150)
    t.left(90)
    t.pendown()
    t.forward(200)
    t.right(90)
    t.circle(-50, 180)
    #буква и
    t.penup()
    t.left(180)
    t.forward(125)
    t.left(90)
    t.forward(100)
    t.pendown()
    t.left(180)
    t.forward(200)
    t.left(145)
    t.forward(240)
    t.right(145)
    t.forward(200)
    t.left(90)
    #буква н
    t.penup()
    t.forward(100)
    t.left(90)
    t.pendown()
    t.forward(200)
    t.penup()
    t.left(180)
    t.forward(100)
    t.left(90)
    t.pendown()
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(180)
    t.forward(200)
    #буква я
    t.penup()
    t.left(90)
    t.forward(80)
    t.left(60)
    t.pendown()
    t.forward(120)
    t.left(30)
    t.forward(100)
    t.left(270)
    t.circle(-50, -180)
    t.left(90)
    t.forward(110)
    t.penup()
    t.setpos(0, 0)

def printGey(fontSize, color, coordinateX, coordinateY, speed, t):
    t.penup()
    t.speed(speed)
    t.pencolor(color)
    t.setpos(coordinateX, coordinateY)
    t.write("ГЕЙ", "true", "right", font=("Arial", fontSize, 'normal'))

colors = [
    '#e314ac',
    '#e3e014',
    '#e33e14',
    '#4114e3',
    '#14e3c1',
    '#18e314',
    '#e3149e',
    '#4be314',
    '#a8e314',
]

t = turtle.Turtle()
t.screen.setup(800, 600)
t.screen.bgcolor('#414542')
printGrinya(t)

while True:
    color = colors[random.randint(0, 8)]
    fontSize = random.randint(28, 108)
    coordinateX = random.randint(-350, 400)
    coordinateY = random.randint(-275, 300)
    speed = random.randint(6, 18)

    printGey(fontSize, color, coordinateX, coordinateY, speed, t)


turtle.exitonclick()
