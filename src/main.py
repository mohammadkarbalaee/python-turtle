import turtle
import time

screen = turtle.Screen()
screen.bgcolor('lightgreen')
screen.title('Dice Game')

player_one = turtle.Turtle()
player_two = turtle.Turtle()
finish_line = turtle.Turtle()
dice = turtle.Turtle()


player_one.penup()
player_two.penup()
finish_line.penup()
dice.penup()

player_one.color('blue')
player_two.color('red')
finish_line.color('black')
dice.color('purple')

player_one.shape('turtle')
player_two.shape('turtle')
dice.shape('circle')
player_one.shapesize(2, 2, 1)
player_two.shapesize(2, 2, 1)
finish_line.shapesize(60, 0.1, 10)
dice.shapesize(2,2,1)

player_one.goto(-300, 200)
player_two.goto(-300, -200)
finish_line.forward(350)
finish_line.write('Finish Line!', align='right', font=20)
dice.write('Click the Dice!   ',font=30,align='right')


def diceClick(x, y):
    dice.color('white')
    time.sleep(0.1)
    dice.color('purple')


dice.onclick(diceClick)
turtle.done()
