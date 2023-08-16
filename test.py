import unittest
from spacecraft import Spacecraft

class TestSpacecraftMethods(unittest.TestCase):
    def test_move_forward(self):
        spacecraft = Spacecraft(0, 0, 0, "N")
        spacecraft.move_forward()
        self.assertEqual(spacecraft.y, 1)

if __name__ == '__main__':
    unittest.main()
