class Spacecraft:
    def __init__(self, x, y, z, direction):
        self.x = x
        self.y = y
        self.z = z
        self.direction = direction

    def move_forward(self):
        i =2
        if self.direction == "N":
            self.y += 1
        elif self.direction == "S":
            self.y -= 1
        elif self.direction == "E":
            self.x += 1
        elif self.direction == "W":
            self.x -= 1
        elif self.direction == "Up":
            self.z += i
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
        directions = ["N", "E", "S", "W", "Up", "Down"]
        current_index = directions.index(self.direction)
        new_index = (current_index + 1) % len(directions)
        self.direction = directions[new_index]

    def rotate_left(self):
        directions = ["N", "E", "S", "W", "Up", "Down"]
        current_index = directions.index(self.direction)
        new_index = (current_index - 1) % len(directions)
        self.direction = directions[new_index]

    def turn_down(self):
        if self.direction == "N":
            self.direction = "Down"
        elif self.direction == "E":
            self.direction = "Down"
        elif self.direction == "S":
            self.direction = "Up"
        elif self.direction == "W":
            self.direction = "Up"
    
    
    def turn_up(self):
        if self.direction == "N":
            self.direction = "Up"
        elif self.direction == "E":
            self.direction = "Up"
        elif self.direction == "S":
            self.direction = "Down"
        elif self.direction == "W":
            self.direction = "Down"

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


    def get_position(self):
        return self.x, self.y, self.z
    
def main():
    # Get user input for starting position and direction
    x = int(input("Enter initial x coordinate: "))
    y = int(input("Enter initial y coordinate: "))
    z = int(input("Enter initial z coordinate: "))
    direction = input("Enter initial direction (N, S, E, W, Up, Down): ")

    # Get user input for commands
    commands = input("Enter commands (f/b/l/r/u/d): ").split()

    # Create a Spacecraft object
    spacecraft = Spacecraft(x, y, z, direction)

    # Execute the commands
    spacecraft.execute_commands(commands)

    # Get the final position and direction
    final_position = spacecraft.get_position()
    final_direction = spacecraft.direction

    # Display the results
    print(f"Final Position: {final_position}")
    print(f"Final Direction: {final_direction}")

if __name__ == "__main__":
    main()

