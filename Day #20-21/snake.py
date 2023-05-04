from turtle import Turtle

move_dis = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
START_POSITION = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
        self.turtle_list = []
        self.pos = 0
        self.create_snake()
        self.head = self.turtle_list[0]

    def add_tail(self, pos):
        start_turtle = Turtle("square")
        start_turtle.color("white")
        start_turtle.penup()
        start_turtle.goto(pos)
        self.turtle_list.append(start_turtle)

    def create_snake(self):
        for position in START_POSITION:
            self.add_tail(position)

    def extend(self):
        self.add_tail(self.turtle_list[-1].position())

    def move(self):
        for t in range(len(self.turtle_list) - 1, 0, -1):
            new_x = self.turtle_list[t - 1].xcor()
            new_y = self.turtle_list[t - 1].ycor()
            self.turtle_list[t].goto(new_x, new_y)
        self.head.forward(move_dis)

    def collision(self):
        for t in range(len(self.turtle_list) - 1, 1, -1):
            if self.head.distance(self.turtle_list[t]) < 10:
                return True
        return False

    def reset(self):
        for seg in self.turtle_list:
            seg.goto(1000,1000)
        self.turtle_list.clear()
        self.create_snake()
        self.head = self.turtle_list[0]

    # turning the head of the snake, so it will move in a specific heading
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

