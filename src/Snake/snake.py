"""Classic snake game
"""

from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    """The Snake Game

    Returns:
        _type_: _description_
    """

    head: Turtle

    def __init__(self):
        self.segments: list[Turtle] = []
        self.create_snake()

    def create_snake(self):
        """Create the snake body"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)
        self.head = self.segments[0]
        self.head.color("green")

    def add_segment(self, position):
        """Increase the snake body

        Args:
            position (tuple): end position off snake body
        """
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Extend the snake body"""
        self.add_segment(self.segments[-1].position())

    def move(self) -> bool:
        """Move the snake

        Returns:
            bool: if hit the wall or it self then return False
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

        for segment in self.segments[1:]:
            if self.head.position() == segment.position():
                print("Snake hit it's own tail")
                return False
        if (
            not -300 < self.head.xcor() < 300
            or not -300 < self.head.ycor() < 300
        ):
            print("Snake hit the wall")
            return False
        return True

    def set_heading_up(self):
        """Change direction of snake"""
        if int(self.head.heading()) != DOWN:
            self.head.setheading(UP)

    def set_heading_down(self):
        """Change direction of snake"""
        if int(self.head.heading()) != UP:
            self.head.setheading(DOWN)

    def set_heading_left(self):
        """Change direction of snake"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def set_heading_right(self):
        """Change direction of snake"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        """Move snake out of frame and clear segments"""
        for index in range(len(self.segments) - 1, 0, -1):
            self.segments[index].goto(700, 700)
        self.head.goto(700, 700)
        self.segments: list[Turtle] = []
        self.create_snake()
