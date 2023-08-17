
    def test_execute_commands(self):
        spacecraft = Spacecraft(0, 0, 0, "N")
        commands = ["f", "r", "u", "b", "l"]
        spacecraft.execute_commands(commands)
        self.assertEqual(spacecraft.get_position(), (0, 1, -1))
        self.assertEqual(spacecraft.get_direction(), "N")