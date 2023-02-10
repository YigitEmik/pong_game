import turtle as t
from scene import splitScreen
from player import Player
from ball import Ball
from scoreboard import ScoreBoard
import time

#Screen
screen = t.Screen()
screen.setup(800,800)
screen.bgcolor('black')
screen.tracer(0)
screen.title('Pong')

#Game values
game_is_on = True


#Players
player1 = Player((-380,0))
player2 = Player((380,0))
ball = Ball()

#Scene
score = ScoreBoard()
split_screen = splitScreen()
split_screen.draw_line()
screen.listen()
round = 0
while game_is_on:
    if round == 0:
        time.sleep(0.1)
    else:
        time.sleep(0.04)
    screen.update()
    screen.onkeypress(player1.goUp, 'Up')
    screen.onkeypress(player2.goUp, 'w')
    screen.onkeypress(player1.goDown, 'Down')
    screen.onkeypress(player2.goDown, 's')
    ball.move()
    if ball.distance(player1) < 40:
        ball.dirHor = "right"
    if ball.distance(player2) < 30:
        ball.dirHor = "left"
    if ball.xcor() > 400:
        round += 1
        ball.resetPos()
        score.scoreUpP1()
    if ball.xcor() < -400:
        round += 1
        ball.resetPos()
        score.scoreUpP2()
    if score.p1_score == 10:
        score.endGame("Player 1")
        game_is_on = False
    if score.p2_score == 10:
        score.endGame("Player 2")
        game_is_on = False
        
    
    
    
























screen.exitonclick()



