from turtle import Turtle


class Display(Turtle):
    def __init__(self, x, y, state_name):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.color("black")
        self.write(f"{state_name}", align="center", font=("Arial", 8, "normal"))
