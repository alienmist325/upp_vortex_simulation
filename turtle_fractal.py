from turtle import Turtle


class L_System:
    def __init__(self, initial_string, angle_change=90, speed=5):
        self.rules = {}
        self.current_string = initial_string
        self.angle_change = angle_change
        self.turtle = Turtle()
        self.speed = speed
        self.turtle.speed(0)

    def add_rule(self, char, string):
        """
        Add a new rule, specifying what a given
        character should be replaced with.
        """

    def update(self):
        """
        Apply all the rules to generate a new string.
        """

    def __repr__(self):
        return self.current_string

    def print(self):
        """
        Convert the current string into Turtle instructions,
        and draw the result.
        """


def square_snowflake():
    system = L_System("M-M-M-M", 90)
    system.add_rule("+", "+")
    system.add_rule("-", "-")
    system.add_rule("M", "M-M+M+MM-M-M+M")
    return system


def tree():
    system = L_System("0", 45)
    system.add_rule("1", "11")
    system.add_rule("0", "1[-0]+0")
    return system
