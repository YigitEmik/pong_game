from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.speed(6)
        self.penup()
        self.dirVer = "up" #Vertical Direction
        self.dirHor = "right" #Horizontal Direction
        
    def move(self):
        match self.dirHor:
            case "right":
                match self.dirVer:
                    case "up":
                        x = self.xcor() + 10
                        y = self.ycor() + 10
                        self.setpos(x,y)
                        if self.ycor() >= 400:
                            self.dirVer = "down"
                    case "down":
                        x = self.xcor() + 10
                        y = self.ycor() - 10
                        self.setpos(x,y)
                        if self.ycor() <= -390:
                            self.dirVer = "up"
            case "left":
                match self.dirVer:
                    case "up":
                        x = self.xcor() - 10
                        y = self.ycor() + 10
                        self.setpos(x,y)
                        if self.ycor() >= 400:
                            self.dirVer = "down"
                    case "down":
                        x = self.xcor() - 10
                        y = self.ycor() - 10
                        self.setpos(x,y)
                        if self.ycor() <= -390:
                            self.dirVer = "up"
    def resetPos(self):
        self.goto(0,0)
            
        