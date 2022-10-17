from turtle import Turtle

ALIGNMENT = 'center'
FONT1 = ('BankGothic Md BT', 15, 'bold') # EG. INSTEAD OF in def __init__(self): | self.style1 = ('Franklin Gothic Book', 15, 'bold')
FONT2 = ('BankGothic Md BT', 15)
FONT3 = ('BankGothic Md BT', 17, 'bold')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.goto(x=0, y=280)
        self.color("white")
        self.pd()
        self.write(f"Current score: ", font=FONT1, align=ALIGNMENT)
        self.pu()
        self.goto(x=0, y=320)
        self.color("yellow")
        self.pd()
        self.write(f"🏆 YOUR BEST SCORE: ", font=FONT3, align=ALIGNMENT)
        self.pu()
        self.score_turtle = Turtle()
        self.current_score = 0
        self.display_high_score()

    def update_current_score(self):
        self.score_turtle.clear()
        self.score_turtle.reset()
        self.score_turtle.hideturtle()
        self.score_turtle.pu()
        self.score_turtle.goto(x=120, y=280)
        self.score_turtle.color("white")
        self.score_turtle.pd()
        self.score_turtle.write(f"{self.current_score}", font=FONT1, align=ALIGNMENT)
        self.score_turtle.pu()
        self.display_high_score()

    def display_high_score(self):
        with open("high_score.txt") as high_score_file:
            self.high_score = high_score_file.read()
        self.score_turtle.goto(x=170, y=320)
        self.score_turtle.color("yellow")
        self.score_turtle.pd()
        self.score_turtle.write(f"{self.high_score}", font=FONT3, align=ALIGNMENT)
        self.score_turtle.pu()

    def update_high_score(self):
        with open("high_score.txt", mode="w") as high_score_file:
            high_score_file.write(str(self.current_score))  # overwrites what's in high_score.txt, if anything
        self.display_high_score()

    def game_over(self):
        self.message = Turtle()
        self.message.hideturtle()
        self.message.pu()
        self.message.goto(0, 0)
        self.message.speed("slowest")
        self.message.color('red')
        self.message.pd()
        self.message.write("GAME OVER", font=FONT3, align='center')
        self.message.pu()
        self.message.goto(0, -50)
        self.message.pd()
        self.message.write(f"Click anywhere to play again \n       or press 'q' to exit", font=FONT1, align='center')
        self.message.hideturtle()
