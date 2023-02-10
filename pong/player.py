from turtle import Turtle

class Player(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.setpos(position)
        self.shapesize(5,1) # (5x20 = 100 width | 1x20 = 20 length)

    def goUp(self):
        y = self.ycor()
        if y < 340:
            self.sety(y+20)
    def goDown(self):
        y = self.ycor()
        if y > -340:
            self.sety(y-20)
    
        
        
        
        
        
    

    
    
        
        
    