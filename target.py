from turtle import Turtle
import random

class Target(Turtle): # Target class inherits from the Turtle class (which becomes the superclass)

    def __init__(self):
        super().__init__()
        self.shape("circle") # instead of creating a new object: self.new_target = Turtle("circle") bc in Turtle class object is already created
        self.pu()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5, outline=None)
        self.color("orange")
        self.speed("fastest")
        self.random_display()

    def random_display(self):
        new_target_x = random.randrange(-260, 280, step=20) #randrange instead of randint to include the step so that target is created in the middle of 20x20 which is the size of a single snake turtle
        new_target_y = random.randrange(-260, 280, step=20)
        self.goto(new_target_x, new_target_y)
        self.showturtle()


