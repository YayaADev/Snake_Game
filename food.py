from turtle import Turtle
import random


class Food(Turtle):  # Inherits from the turtle class

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh_food()

    def refresh_food(self):
        self.goto(x=random.randint(-280, 280), y=random.randint(-280, 280))
