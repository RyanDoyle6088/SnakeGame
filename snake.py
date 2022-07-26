from turtle import Turtle, Screen

MOVE_DISTANCE = 20
POSITIONS = [0, 90, 180, 270]

class Snake:

    def __init__(self):

        self.segments = []
        self.x = 0
        self.y = 0
        self.set_up_snake()
        self.head = self.segments[0]

    def set_up_snake(self):
        """Sets up our snake with 3 segments"""
        for turtle in range(3):
            self.add_segment(turtle)

    def move_snake(self):
        """Moves our snake using user key commands"""
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def add_segment(self, turtle):
        snake_segment = Turtle("square")
        snake_segment.pu()
        snake_segment.color("white")
        snake_segment.setpos(self.x, self.y)
        self.x -= 20
        self.segments.append(snake_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def up(self):

        if self.head.heading() != POSITIONS[3]:
            self.head.setheading(POSITIONS[1])

    def down(self):

        if self.head.heading() != POSITIONS[1]:
            self.head.setheading(POSITIONS[3])

    def right(self):

        if self.head.heading() != POSITIONS[2]:
            self.head.setheading(POSITIONS[0])

    def left(self):

        if self.head.heading() != POSITIONS[0]:
            self.head.setheading(POSITIONS[2])
