
from turtle import *
import random
 
toto=Turtle()
toto.shape('turtle')
toto.color('blue')

screen=Screen()

## challenge1->to draw a square
#    toto.forward(100)
#    toto.right(90)
#    toto.forward(200)
#    toto.right(90)
#    toto.forward(200)
#    toto.right(90)
#    toto.forward(200)

#for _ in range(4):
#    toto.forward(100)
#    toto.right(90)
  
## challenge2-> draw dashed line
#for i in range(10):
#    toto.forward(10)
#    toto.penup()
#    toto.forward(10)
#    toto.pendown()

## challenge3-> draw diffrent shapes

#for i in range(3):
#    toto.forward(100)
#    toto.right(120)
#toto.left(360)    
#for i in range(4):
#    toto.forward(100)
#    toto.right(90)
#for i in range(5):
#    toto.forward(100)
#    toto.right(72)
#for i in range(6):
#    toto.forward(100)
#    toto.right(60)
#for i in range(7):
#    toto.forward(100)
#    toto.right(180-128.57)
#for i in range(8):
#    toto.forward(100)
#    toto.right(45)
#for i in range(9):
#    toto.forward(100)
#    toto.right(40)
#for i in range(10):
#    toto.forward(100)
#    toto.right(180-144)

#       or

#colors=["linen", "seashell", "misty rose", "pink", "light pink", "hot pink", "hot pink", "pale violet red"]
#def draw_shape(sides):
#    angle=360/sides
#    toto.color(random.choice(colors))
#    toto.speed(0)
#    for i in range(sides):
#        toto.forward(100)
#        toto.right(angle)   
#    return draw_shape(sides+1)

#draw_shape(3)

##challenge4-> Random Walk

#def isInScreen(w, t):
#    if random.random() > 0.1:
#        return True
#    else:
#        return False
#colors=["linen", "seashell", "misty rose", "pink", "light pink", "hot pink", "hot pink", "pale violet red"]
#directions=[0,90,180,270]

#for _ in range(2000):
#    toto.color(random.choice(colors))
#    toto.forward(30)
#    toto.speed(0)
#    toto.pensize(5)
#    toto.setheading(random.choice(directions))

## challenge5-> Genrate random colors
#directions=[0,90,180,270]

#for _ in range(200):
    
#    toto.color(random.randint(0,255),
#    random.randint(0,255),
#    random.randint(0,255))
#    toto.forward(30)
#    toto.speed(0)
#    toto.pensize(5)
#    toto.setheading(random.choice(directions))

## Challenge6-> circle spiral
colors=["linen", "seashell", "misty rose", "pink", "light pink", "hot pink", "hot pink", "pale violet red"]
def draw_spirograph(size):
    for _ in range(360//size):
        toto.speed(0)
        toto.color(random.choice(colors))
        toto.pensize(2)
        toto.circle(100)
        toto.setheading(toto.heading()+size)

draw_spirograph(5)

screen.exitonclick()

