from turtle import Screen
from snake import Snake
from food import Food
from score import Scorebord
import time



screen = Screen()
screen.setup(width=600 , height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.listen()
screen.tracer(0)



# starting_position = [(0,0),(-20 , 0) ,(-40 , 0)]
# snake_body = []
# for position in starting_position:
#     snake = Turtle(shape="square")
#     snake.penup()
#     snake.color("cyan")
#     snake.goto(position)
#     snake_body.append(snake)
snake = Snake()
food = Food()
score = Scorebord()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")




is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    # for body_part in range(len(snake_body) -1,0,-1 ):
    #     new_x = snake_body[body_part-1].xcor()
    #     new_y = snake_body[body_part - 1].ycor()
    #     snake_body[body_part].goto(new_x , new_y)
    # snake_body[0].forward(20)
    snake.move()
    # Detecting the collision of head and food
    if snake.head.distance(food) < 15 :
        food.refresh()
        snake.extend()
        score.increase_score()


    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
         score.reset_score()
         snake.reset_snake()

    #detect collision with tail
    for bodypart in snake.snake_body[1:]:
        if snake.head.distance(bodypart) <10:
            score.reset_score()
            snake.reset_snake()








screen.exitonclick()
