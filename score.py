from turtle import Turtle
ALIGNMENT = 'center'
FONT1 = ('BankGothic Md BT', 15, 'bold') # EG. INSTEAD OF in def __init__(self): | self.style1 = ('Franklin Gothic Book', 15, 'bold')
FONT2 = ('BankGothic Md BT', 15)
FONT3 = ('BankGothic Md BT', 17, 'bold')


class Score:

    def __init__(self):
        self.score_title_turtle = Turtle()
        self.score_title_turtle.hideturtle()
        self.score_title_turtle.pu()
        self.score_title_turtle.goto(x=0, y=280)
        self.score_title_turtle.color("white")
        self.score_title_turtle.pd()
        self.score_title_turtle.write(f"Current score: ", font=FONT1, align=ALIGNMENT)
        self.score_title_turtle.pu()
        self.score_turtle = Turtle()
        self.targets_scored = 0
        self.all_time_best = 0
        self.all_time_best_no = Turtle()
        self.all_time_best_score_shown = Turtle()

    def score(self):
        self.score_turtle.clear()
        self.score_turtle.reset()
        self.score_turtle.hideturtle()
        self.score_turtle.pu()
        self.score_turtle.goto(x=120, y=280)
        self.score_turtle.color("white")
        self.score_turtle.pd()
        self.score_turtle.write(f"{self.targets_scored}", font=FONT1, align=ALIGNMENT)
        self.score_turtle.pu()

    def all_time_best_score_header(self):
        self.all_time_best_score_shown.hideturtle()
        self.all_time_best_score_shown.pu()
        self.all_time_best_score_shown.goto(x=0, y=320)
        self.all_time_best_score_shown.color("yellow")
        self.all_time_best_score_shown.pd()
        self.all_time_best_score_shown.write(f"🏆 YOUR BEST SCORE: ", font=FONT3, align=ALIGNMENT)
        self.all_time_best_score_shown.pu()

    def all_time_best_score_number(self):
        self.all_time_best_no.clear()
        self.all_time_best_no.reset()
        self.all_time_best_no.pu()
        self.all_time_best_no.goto(x=170, y=320)
        self.all_time_best_no.color("yellow")
        self.all_time_best_no.pd()
        self.all_time_best_no.write(f"{self.all_time_best}", font=FONT3, align=ALIGNMENT)
        self.all_time_best_no.pu()
        self.all_time_best_no.hideturtle()

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

