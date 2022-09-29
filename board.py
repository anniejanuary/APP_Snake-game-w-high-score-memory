from turtle import Turtle, Screen
screen = Screen()


class Board:

    def __init__(self):
        self.borders_turtle = Turtle()

    def borders(self):
        self.borders_turtle.hideturtle()
        self.borders_turtle.pu()
        self.borders_turtle.color("white")
        screen.tracer(0)
        self.borders_turtle.goto(275, 275)
        self.borders_turtle.pd()
        self.borders_turtle.goto(-275, 275)
        self.borders_turtle.goto(-275, -275)
        self.borders_turtle.goto(275, -275)
        self.borders_turtle.goto(275, 275)
        self.borders_turtle.pu()
        screen.update()

