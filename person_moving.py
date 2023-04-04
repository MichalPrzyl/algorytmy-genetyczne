from globals import MAX_WIDTH, MAX_HEIGHT, PERSON_HEIGHT, PERSON_WIDTH
from math import floor

MOVING_SPEED = 5

class PersonMoving:
    def go_up(self):
        if self.position_y < 0:
            return
        self.position_y -= 1 * MOVING_SPEED
    
    def go_down(self):
        if self.position_y > MAX_HEIGHT - floor(PERSON_HEIGHT):
            return
        self.position_y += 1 * MOVING_SPEED

    def go_left(self):
        if self.position_x < 0:
            return
        self.position_x -= 1 * MOVING_SPEED

    def go_right(self):
        if self.position_x > MAX_WIDTH - floor(PERSON_WIDTH):
            return
        self.position_x += 1 * MOVING_SPEED