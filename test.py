import unittest
from spacecraft import Spacecraft

class TestSpacecraftMethods(unittest.TestCase):
    def test_move_forward(self):
        spacecraft = Spacecraft(0, 0, 0, "N")
        spacecraft.move_forward()
        self.assertEqual(spacecraft.y, 1)
    
    def test_rotate_right(self):
        spacecraft = Spacecraft(0, 0, 0, "N")
        spacecraft.rotate_right()
        self.assertEqual(spacecraft.direction, "E")

    def test_move_backward(self):
        spacecraft = Spacecraft(0, 1, 0, "N")
        spacecraft.move_backward()
        self.assertEqual(spacecraft.y, 0)

    def test_move_backward(self):
        spacecraft = Spacecraft(0, 0, 0, "S")
        spacecraft.move_backward()
        self.assertEqual(spacecraft.y, 1)
    
    def test_turn_up(self):
        spacecraft = Spacecraft(0, 0, 0, "N")
        spacecraft.turn_up()
        self.assertEqual(spacecraft.direction, "U")

    def test_turn_down(self):
        spacecraft = Spacecraft(0, 0, 0, "N")
        spacecraft.turn_down()
        self.assertEqual(spacecraft.direction, "D")

    def test_rotate_left_N(self):
        spacecraft = Spacecraft(0, 0, 0, "N")
        spacecraft.rotate_left()
        self.assertEqual(spacecraft.direction, "W")

    def test_rotate_left_E(self):
        spacecraft = Spacecraft(0, 0, 0, "E")
        spacecraft.rotate_left()
        self.assertEqual(spacecraft.direction, "N")

    def test_rotate_left_S(self):
        spacecraft = Spacecraft(0, 0, 0, "S")
        spacecraft.rotate_left()
        self.assertEqual(spacecraft.direction, "E")

    def test_rotate_left_W(self):
        spacecraft = Spacecraft(0, 0, 0, "W")
        spacecraft.rotate_left()
        self.assertEqual(spacecraft.direction, "S")


    



if __name__ == '__main__':
    unittest.main()
