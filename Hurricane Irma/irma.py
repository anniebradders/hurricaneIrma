import turtle
import csv

def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.gif")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return (t, wn, map_bg_img)

from tkinter import *

def irma():
    """Animates the path of hurricane Irma
    """
    (t, wn, map_bg_img) = irma_setup()

    # your code to animate Irma here
    ##opens the file so it can read the data inside##
    with open('irma.csv', 'r') as csvfile:
            straight = [line.strip() for line in csvfile.readlines()]
            straight = straight[1:]
            straight = [line.split(',') for line in straight]
            straight = [line[2:5] for line in straight]
        ##lifts the pen so that it doesnt draw while it gets in position inline with the data##
    t.penup()

    start = straight[0]
    yaxis = start[0]
    xaxis = start[1]

    yaxis = float(yaxis)
    xaxis = float(xaxis)

    t.hideturtle()

    t.setx(xaxis)
    t.sety(yaxis)

    elements = len(straight)
    for i in range(elements):

        update = straight[i]

        y = update[0]
        x = update[1]

        category = update[2]
        category = int(category)

        x = float(x)
        y = float(y)

        if category < 74:
            t.width(0.5)
            t.pencolor("white")
        
        elif category < 74 and category <= 95:
            t.width(1)
            t.pencolor("blue")
            t.write("1", font=("Arial", 10))
            
        elif category >= 96 and category <= 110:
            t.width(3)
            t.pencolor("green")
            t.write("2", font=("Arial", 10))
            
        elif category >=110 and category <= 129:
            t.width(5)
            t.pencolor("yellow")
            t.write("3", font=("Arial", 10))
            
        elif category >= 130 and category <= 156:
            t.width(7)
            t.pencolor("orange")
            t.write("4", font=("Arial", 10))
            
        elif category >= 156:
            t.width(9)
            t.pencolor("red")
            t.write("5", font=("Arial", 10))

        
        t.showturtle()
        t.pendown()
        t.goto(x, y)

    wn.exitonclick()
        


    # end code - leave this at the very end, or else your application will hang
    turtle.done()

if __name__ == "__main__":
    irma()
