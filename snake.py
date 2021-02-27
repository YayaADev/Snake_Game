from turtle import Screen, Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

FORWARD_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.SNAKE = []
        self.make_snake()
        self.head = self.SNAKE[0]

    def make_snake(self):

        for position in STARTING_POSITIONS:
            self.add_segment(position)
        screen = Screen()
        screen.update()

    def add_segment(self, position):
        square = Turtle("square")
        square.color("white")
        square.penup()
        square.goto(position)
        self.SNAKE.append(square)

    def move_snake(self):
        for seg in range(len(self.SNAKE) - 1, 0, -1):  # Loop from reverse order
            move_x = self.SNAKE[seg - 1].xcor()  # retrieving the second to last segment
            move_y = self.SNAKE[seg - 1].ycor()
            self.SNAKE[seg].goto(move_x, move_y)  # going to the second to last segment position
        self.head.forward(FORWARD_DISTANCE)

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

    def extend(self):
        self.add_segment(self.SNAKE[-1].position())

    def reset(self):
        for seg in self.SNAKE:
            seg.hideturtle()
            seg.goto(1000,1000)
        self.SNAKE.clear()
        self.make_snake()
        self.head = self.SNAKE[0]
