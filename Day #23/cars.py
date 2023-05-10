from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Cars:
    def __init__(self):
        self.num_cars = 22
        self.move_distance = 0.1
        self.cars = []
        self.spawn_cars()

    def spawn_cars(self):
        for a in range(0, self.num_cars):
            new_car = Turtle()
            new_car.color(random.choice(COLORS))
            new_car.shape("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.goto(random.randint(-260, 260), random.randint(-230, 260))
            new_car.setheading(180)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)
            if car.xcor() < -280:
                car.goto(300, random.randint(-260, 260))

    def detect_collision(self, turt):
        for car in self.cars:
            if car.distance(turt) < 29 and turt.xcor() < (car.xcor() - 20):
                return True
            if car.distance(turt) < 20 and (car.ycor() + 10) > (turt.ycor() + 10) > (car.ycor() - 10):
                return True

    def level_up(self):
        self.move_distance *= 0.7
        if self.num_cars < 40:
            self.num_cars += 1
        self.spawn_cars()

    def clear_car(self):
        for car in self.cars:
            car.hideturtle()
        self.cars.clear()
