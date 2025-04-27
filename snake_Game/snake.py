from turtle import Turtle
import random


COLOR = ["red", "blue" , "purple" , "pink" , "orange", "cyan", "white","green","yellow","brown"]

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVING_SPEED = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.snake_body = []
        self.createsnake()
        self.head = self.snake_body[0]


    def createsnake(self):
        for position in STARTING_POSITION:
            self.add_body(position)


    def add_body(self , position):
        snake = Turtle(shape="circle")
        snake.penup()
        snake.color(random.choice(COLOR))
        snake.goto(position)
        self.snake_body.append(snake)

    def extend(self):
        self.add_body(self.snake_body[-1].position())

    def move(self):
        for body_part in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[body_part - 1].xcor()
            new_y = self.snake_body[body_part - 1].ycor()
            self.snake_body[body_part].goto(new_x, new_y)
        self.snake_body[0].forward(MOVING_SPEED)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset_snake(self):
        for bodyparts in self.snake_body:
            bodyparts.goto(1000,1000)
        self.snake_body.clear()
        self.createsnake()
        self.head = self.snake_body[0]
