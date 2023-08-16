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
    
    def test_turn_up(self):
        spacecraft = Spacecraft(0, 0, 0, "N")
        spacecraft.turn_up()
        self.assertEqual(spacecraft.direction, "U")



if __name__ == '__main__':
    unittest.main()
