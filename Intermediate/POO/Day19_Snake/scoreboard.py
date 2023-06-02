from turtle import Turtle 
alignment = "center"
font = ("courier", 24, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("save_score.txt") as file:
            self.high_score = (file.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=alignment, font=font)
    
    def increment_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            # 
            self.high_score = self.score
            with open("save_score.txt", mode="w") as data:
                data.write(f"high score: {self.high_score}")
        self.score = 0
        self.update_scoreboard()


    # def game_over(self):
    #     self.clear()
    #     self.write(f"GAME OVER u score is : {self.score}", align=alignment, font=font)

    