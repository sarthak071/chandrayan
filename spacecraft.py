class Spacecraft:
    def __init__(self, x, y, z, direction):
        self.x = x
        self.y = y
        self.z = z
        self.direction = direction

    def move_forward(self):
        if self.direction == "N":
            self.y += 1
    
    def rotate_right(self):
        directions = ["N", "E", "S", "W"]
        current_index = directions.index(self.direction)
        new_index = (current_index + 1) % len(directions)
        self.direction = directions[new_index]
    
    def move_backward(self):
        if self.direction == "N":
            self.y -= 1
        elif self.direction == "E":
            self.x -= 1
        elif self.direction == "S":
            self.y += 1
        elif self.direction == "W":
            self.x += 1