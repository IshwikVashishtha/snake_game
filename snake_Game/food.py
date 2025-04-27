from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_wid=0.8 , stretch_len=0.8)
        self.color("green")
        self.speed("fastest")
        random_x =  randint(-280 , 280)
        random_y =  randint(-280 , 280)
        self.goto(random_x , random_y)

    def refresh(self):
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(random_x, random_y)
