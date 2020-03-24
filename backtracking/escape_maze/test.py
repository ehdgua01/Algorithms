import unittest

from .escape_maze import escape_maze


class TestCase(unittest.TestCase):
    def test_escape_maze(self):
        # fmt: off
        maze = (
            "#S#####\n"
            "# # # #\n"
            "#   # #\n"
            "### # #\n"
            "#   #G#\n"
            "#     #"
        )
        # fmt: on
        self.assertEqual(
            escape_maze(maze),
            [
                (1, 0),
                (1, 1),
                (1, 2),
                (2, 2),
                (3, 2),
                (3, 3),
                (3, 4),
                (3, 5),
                (4, 5),
                (5, 5),
                (5, 4),
            ],
        )
