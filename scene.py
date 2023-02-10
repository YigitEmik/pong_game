from turtle import Turtle

class splitScreen(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.penup()
        self.shape('square')
        self.color('white')  
        self.pensize(3)
        self.hideturtle()
        self.setpos(0,400)
        
    def draw_line(self):
        while self.ycor() > -400:
            self.setheading(270)
            self.fd(10)
            self.pendown()
            self.fd(3)
            self.penup()
