from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.p1_score = 0
        self.p2_score = 0
        self.writePlayer()
        self.sety(300)
        
        self.write(f'{self.p1_score}     {self.p2_score}', False, align='center', font=('Courier', 70, 'bold'))
    def scoreUpP1(self):
        self.clear()
        self.p1_score += 1
        self.write(f'{self.p1_score}     {self.p2_score}', False, align='center', font=('Courier', 70, 'bold'))
    
    def scoreUpP2(self):
        self.clear()
        self.p2_score += 1
        self.write(f'{self.p1_score}     {self.p2_score}', False, align='center', font=('Courier', 70, 'bold'))
    
    def endGame(self,player):
        self.goto(0,0)
        self.write(f'Game Over {player} won!', False, align='center', font=('Courier', 30, 'bold'))
    def writePlayer(self):
        self.write(f'Player 1 - (W, S)       Player 2 - (Up, Down)', False, align='center', font=('Courier', 20, 'bold'))