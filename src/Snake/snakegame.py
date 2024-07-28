"""The Classic Snake Game
"""

import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake


class SnakeGame:
    """The Classic Snake Game"""

    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Snake Game")
        self.screen.tracer(0)

        self.snake = Snake()
        self.food = Food()
        self.scoreboard = Scoreboard()
        self.screen.listen()

        self.screen.onkey(fun=self.snake.set_heading_up, key="Up")
        self.screen.onkey(fun=self.snake.set_heading_down, key="Down")
        self.screen.onkey(fun=self.snake.set_heading_left, key="Left")
        self.screen.onkey(fun=self.snake.set_heading_right, key="Right")

    def run(self):
        """Running the game"""
        game_is_on = True
        while game_is_on:
            self.screen.update()
            time.sleep(0.1)
            if not self.snake.move():
                game_is_on = self.scoreboard.game_over()
                self.reset()

            else:
                if self.snake.head.distance(self.food) < 15:
                    self.food.refresh()
                    self.scoreboard.increase_score()
                    self.snake.extend()

    def reset(self):
        """Reset snakebody and game score"""
        self.snake.reset()
        self.scoreboard.reset_score()
