class Spacecraft:
    def __init__(self, x, y, z, direction):
        self.x = x
        self.y = y
        self.z = z
        self.direction = direction

    def move_forward(self):
        if self.direction == "N":
            self.y += 1
        elif self.direction == "S":
            self.y -= 1
        elif self.direction == "E":
            self.x += 1
        elif self.direction == "W":
            self.x -= 1
        elif self.direction == "Up":
            self.z += 1
        elif self.direction == "Down":
            self.z -= 1

    def move_backward(self):
        if self.direction == "N":
            self.y -= 1
        elif self.direction == "E":
            self.x -= 1
        elif self.direction == "S":
            self.y += 1
        elif self.direction == "W":
            self.x += 1
        elif self.direction == "Up":
            self.z -= 1  # Decrease z for "Up"
        elif self.direction == "Down":
            self.z += 1  # Increase z for "Down"


    def rotate_right(self):
        directions = ["N", "E", "S", "W"]
        current_index = directions.index(self.direction)
        new_index = (current_index + 1) % len(directions)
        self.direction = directions[new_index]

    def rotate_left(self):
        directions = ["N", "E", "S", "W" ]
        current_index = directions.index(self.direction)
        new_index = (current_index - 1) % len(directions)
        self.direction = directions[new_index]

    def turn_down(self):
        if self.direction == "N":
            self.direction = "D"
        elif self.direction == "E":
            self.direction = "D"
        elif self.direction == "S":
            self.direction = "U"

        elif self.direction == "W":
            self.direction = "U"
    

    
    def turn_up(self):
        if self.direction == "N":
            self.direction = "U"
        elif self.direction == "E":
            self.direction = "U"
        elif self.direction == "S":
            self.direction = "D"
        elif self.direction == "W":
            self.direction = "D"

    def execute_commands(self, commands):
        for command in commands:
            if command == "f":
                self.move_forward()
            elif command == "b":
                self.move_backward()
            elif command == "l":
                self.rotate_left()
            elif command == "r":
                self.rotate_right()
            elif command == "u":
                self.turn_up()
            elif command == "d":
                self.turn_down()


 
