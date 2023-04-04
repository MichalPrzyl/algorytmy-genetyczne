import random
from math import floor
from brain import Brain
from person_moving import PersonMoving
from globals import PERSON_WIDTH, PERSON_HEIGHT


class Person(PersonMoving):

    position_x: int
    position_y: int

    height: int
    width: int

    def __init__(self):
        self.position_x = random.randrange(0 + floor(PERSON_WIDTH/2), 800 - floor(PERSON_WIDTH/2))
        self.position_y = random.randrange(0 + floor(PERSON_HEIGHT/2), 800 - floor(PERSON_HEIGHT/2))
        self.height = PERSON_HEIGHT
        self.width = PERSON_WIDTH

        self.brain = Brain()
        self.get_action()

    def get_action(self):
        self.action = random.choice(self.brain.action_options)

    def do_action(self):
        if self.action == "go_up":
            self.go_up()
        elif self.action == "go_down":
            self.go_down()
        elif self.action == "go_left":
            self.go_left()
        elif self.action == "go_right":
            self.go_right()
