from turtle import Turtle, Screen
import time
screen = Screen()


class Snake:
    def __init__(self):
        self.STEP_LENGTH = 20
        self.TILES_COORDINATES = [(0, 0), (-self.STEP_LENGTH, 0), (-(self.STEP_LENGTH * 2), 0)]

    def initial_snake(self, x, y):
        screen.tracer(0)
        self.snake_body = []
        for x, y in self.TILES_COORDINATES:
            new_turtle = Turtle(shape="square") # instead of seperate: new_turtle.shape("square")
            new_turtle.pu()
            new_turtle.color("white")
            new_turtle.goto(x, y)
            self.snake_body.append(new_turtle)

    def go_north(self):
        if self.snake_body[0].heading() != 270:
            self.snake_body[0].setheading(90)

    def go_west(self):
        if self.snake_body[0].heading() != 0:
            self.snake_body[0].setheading(180)

    def go_south(self):
        if self.snake_body[0].heading() != 90:
            self.snake_body[0].setheading(270)

    def go_east(self):
        if self.snake_body[0].heading() != 180:
            self.snake_body[0].setheading(0)

    def move(self):
        screen.update()
        time.sleep(0.1)  # slowing the snake down after each step
        for tile_index in range(len(self.snake_body)-1, 0, -1):
            #start at last element, finish at first element, step = -1 so a negative for loop,
            # starts from the end of the snake body to avoid visible breaks between each square turtle when moving
            ### instead of starting at the first snake turtle: for tile in self.snake_body: | tile.forward(20)
            self.snake_body[tile_index].pu()
            self.snake_body[tile_index].color("white")
            move_to_x = self.snake_body[tile_index -1].xcor()
            move_to_y = self.snake_body[tile_index -1].ycor()
            self.snake_body[tile_index].goto(move_to_x, move_to_y)
        self.snake_body[0].forward(self.STEP_LENGTH)
        screen.listen()
        if screen.onkey(self.go_north, "Up") or screen.onkey(self.go_north, "w"):
            self.snake_body[0].goto(+0, +self.STEP_LENGTH)
        elif screen.onkey(self.go_west, "Left") or screen.onkey(self.go_west, "a"):
            self.snake_body[0].goto(-self.STEP_LENGTH, +0)
        elif screen.onkey(self.go_south, "Down") or screen.onkey(self.go_south, "s"):
            self.snake_body[0].goto(+0, -self.STEP_LENGTH)
        elif screen.onkey(self.go_east, "Right") or screen.onkey(self.go_east, "d"):
            self.snake_body[0].goto(+self.STEP_LENGTH, +0)



