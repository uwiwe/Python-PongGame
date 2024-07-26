from turtle import Turtle
import random
import time


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,0)
        self.shape("circle")
        self.color("white")
        self.x_movement = 0.16
        self.y_movement = 0.08

    def move(self):
        new_x = self.xcor() + self.x_movement
        new_y = self.ycor() + self.y_movement
        self.goto(new_x, new_y)

    def bounce_y(self):
        if self.y_movement > 0:
            self.y_movement = random.uniform(0.16, 0.32)
        else:
            self.y_movement = random.uniform(-0.16, -0.32)
        self.y_movement *= -1

    def bounce_x(self):
        if self.x_movement > 0:
            self.x_movement = random.uniform(0.24, 0.38)
        else:
            self.x_movement = random.uniform(-0.24, -0.38)
        self.x_movement *= -1

    def change_direction(self):
        self.goto(0, 0)
        self.bounce_y()
        self.bounce_x()
        time.sleep(1.5)
