from turtle import Screen
import time

from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # turns the animation off to make all the snake segments line up. 0 sets it off

snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

game_is_running = True
while game_is_running:
    screen.update()  # Update method will refresh the screen with all segments
    time.sleep(0.07)  # Animate ths snake to make it appear it is moving faster
    snake.move_snake()

    # When the snake eats food
    if snake.head.distance(food) < 20:
        food.refresh_food()
        snake.extend()
        score.increase_score()
        score.update_score()

    # When the snake hits the wall
    snake_x_cor = snake.head.xcor()
    snake_y_cor = snake.head.ycor()
    if snake_x_cor > 285 or snake_x_cor < -285 or snake_y_cor > 285 or snake_y_cor < -285:
        score.reset()
        snake.reset()

    # When the snake hits itself
    for segment in snake.SNAKE[1:]:  # Will check every segment of the snake except the head
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
