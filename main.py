from turtle import Turtle, Screen
from snake import Snake
from target import Target
from board import Board
from score import Score

screen = Screen()
screen.setup(width=600, height=800)
screen.bgcolor("black") #screen bg color
screen.title("🐍 Snake") #window header
board = Board()
board.borders()
score = Score()
snake = Snake()
snake.initial_snake(x=0, y=0)
target = Target()
target.random_display()
game_over = False


def restart(mouseclickx, mouseclicky):
    # why these "mouseclickx, mouseclicky" are needed:
    # https://stackoverflow.com/questions/48869611/turtle-onscreenclick-not-behaving-as-expected
    score.current_score = 0
    score.score_turtle.reset()
    score.message.reset()
    score.message.hideturtle()
    board.borders_turtle.clear()
    board.borders()
    target.random_display()
    for turtle in range(len(snake.snake_body)):
        snake.snake_body[turtle].hideturtle()
    snake.initial_snake(x=0, y=0)
    for turtle in snake.snake_body:
        turtle.reset()
        turtle.color("white")
        turtle.pu()
    game(game_over)

def game(game_over):
    while not game_over:
        screen.update()
        snake.move()
        '''If snake eats the target'''
        if snake.snake_body[0].distance(target) < 15: #if the snake head is within 15 pixels of the target
            score.current_score += 1

            if score.current_score > int(score.high_score): #score.all_time_best:
                score.update_high_score()
            add_tile_x = snake.snake_body[len(snake.snake_body) - 1].xcor()
            add_tile_y = snake.snake_body[len(snake.snake_body) - 1].ycor()
            add_turtle = Turtle(shape="square")  # instead of seperate: new_turtle.shape("square")
            add_turtle.pu()
            add_turtle.color("white")
            add_turtle.goto(add_tile_x, add_tile_y)
            snake.snake_body.append(add_turtle)
            target.hideturtle()
            target.random_display()
        score.update_current_score()
        '''If snake eats itself'''
        for i in range(3, len(snake.snake_body) - 1): #skipping the head bc that's the 1st collision point, starting with
                                # tile 4 (index 3) bc thats the first tile the head can reach if it turns around on itself
            if snake.snake_body[0].distance(snake.snake_body[i]) < 15:
                game_over = True
                if score.current_score > score.all_time_best:
                    score.all_time_best = score.current_score
                score.game_over()
                '''Restart the game'''
                screen.onkey(screen.bye, "q")  # Register function exit to event "q" key press
                screen.onclick(restart)
                screen.listen()
        '''If snake hits the wall'''
        if snake.snake_body[0].xcor() >= 275 or snake.snake_body[0].xcor() <= -275 or snake.snake_body[0].ycor() >= 275 or snake.snake_body[0].ycor() <= -275:
            game_over = True
            score.game_over()
            '''Restart the game'''
            screen.onkey(screen.bye, "q")  # Register function exit to event "q" key press
            screen.onclick(restart)
            screen.listen()


game(game_over)
screen.mainloop()


screen.exitonclick()
