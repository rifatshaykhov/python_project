# Globals for the directions
# Change the values as you see fit
EAST = 3
NORTH = 0
WEST = 9
SOUTH = 6


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.x = x_pos
        self.y = y_pos
        self.coordinates = (self.x, self.y)

    def move(self, string):
        counter = self.direction
        for i in string:
            if i == 'R':
                counter += 3
            elif i == 'L':
                counter -= 3
            elif i == 'A':
                if self.direction == NORTH:
                    self.y += 1
                elif self.direction == SOUTH:
                    self.y -= 1
                elif self.direction == EAST:
                    self.x += 1
                elif self.direction == WEST:
                    self.x -= 1

            if counter != self.direction:
                if counter > 9:
                    counter = 0
                elif counter < 0:
                    counter = 9
                self.direction = counter

        self.coordinates = (self.x, self.y)
