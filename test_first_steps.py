"""
Numerik 22/23 (Jeffrey Bukieda 2430873, Tommy Riediger 2412359)
"""
from unittest import main, TestCase
from first_steps import add, subtract


class TestFirstSteps(TestCase):

    def test_add(self):
        self.assertEqual(add(5, 3), 8)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)


if __name__ == "__main__":
    main()
