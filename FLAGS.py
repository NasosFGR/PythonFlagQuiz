import turtle
import random
import time
bob = turtle.Turtle()
def lithuania():
    bob.fillcolor("yellow")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()
    bob.pu()
    bob.goto(0,-30)
    bob.pd()
    bob.fillcolor("green")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()
    bob.pu()
    bob.goto(0,-60)
    bob.pd()
    bob.fillcolor("red")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()
    bob.hideturtle()
def luxemburg():
    bob.fillcolor("red")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()
    bob.pu()
    bob.goto(0,-30)
    bob.pd()
    bob.fillcolor("white")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()
    bob.pu()
    bob.goto(0,-60)
    bob.pd()
    bob.fillcolor("light blue")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()
    bob.hideturtle()

def netherlands():

    bob.fillcolor("red")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()

    bob.pu()
    bob.goto(0,-30)
    bob.pd()

    bob.fillcolor("white")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()

    bob.pu()
    bob.goto(0,-60)
    bob.pd()

    bob.fillcolor("blue")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()

    bob.hideturtle()

def estonia():
    bob.fillcolor("blue")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()

    bob.pu()
    bob.goto(0,-30)
    bob.pd()

    bob.fillcolor("black")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()

    bob.pu()
    bob.goto(0,-60)
    bob.pd()

    bob.fillcolor("white")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()
    bob.hideturtle()




def bulgaria():

    bob.fillcolor("white")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()

    bob.pu()
    bob.goto(0,-30)
    bob.pd()

    bob.fillcolor("green")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()

    bob.pu()
    bob.goto(0,-60)
    bob.pd()

    bob.fillcolor("red")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()

    bob.hideturtle()

flags = [lithuania, luxemburg, netherlands, estonia, bulgaria]


life=3
points=0

while life > 0 and len(flags) > 0:
    bob.reset()
    flagchoice=random.choice(flags)
    flagchoice()
    answer=input("what's this flag?: ")

    flags.remove(flagchoice)

    if answer == flagchoice.__name__:
        print("good job")
        points =points+1
        print ("Your points:", points)
        print ("Your lives:", life)

    else:
        print("wrong")
        if points > 0:
            points -= 1
        else:
            points = 0
        life -= 1
        print("Your points:", points)
        print ("Your lives:", life)

turtle.done()








