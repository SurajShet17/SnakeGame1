from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_measure = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.speed("fastest")
        self.penup()
        self.goto(x=250, y=270)
        self.color("White")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"🐍Suraj's Snake Game🐍 SCORE = {self.score_measure} HIGH SCORE {self.high_score}  ",
                   align="right", font=("Courier", 12, "normal"))

    def reset(self) -> None:
        if self.score_measure > self.high_score:
            self.high_score = self.score_measure
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))

        self.score_measure = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score_measure += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(x=00, y=0)
    #     self.write(arg="Game Over", align = "center", font=("Courier", 16, "normal"))


