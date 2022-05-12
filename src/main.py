import turtle
import time
import random

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
dice.color('black')

player_one.shape('turtle')
player_two.shape('turtle')
dice.shape('circle')
player_one.shapesize(3, 3, 1)
player_two.shapesize(3, 3, 1)
finish_line.shapesize(60, 0.1, 10)
dice.shapesize(2, 2, 1)

player_one.goto(-300, 200)
player_two.goto(-300, -200)
finish_line.forward(350)
finish_line.write('Finish Line!    ', align='right', font=20)
dice.write('Click the Dice!   ', font=30, align='right')

dice_nums = [1, 2, 3, 4, 5, 6]

turn = True

player_one.pendown()
player_two.pendown()


def diceClick(x, y):
    dice.color('white')
    time.sleep(0.1)
    dice.color('black')

    dice_num1 = random.choice(dice_nums)
    dice_num2 = random.choice(dice_nums)

    player_one.forward(5 * dice_num1)
    player_two.forward(5 * dice_num2)


dice.onclick(diceClick)

turtle.done()
