import unittest

from src.strings.greetings import Greetings


class TestGreetings(unittest.TestCase):

    def test_hello(self):
        greetings = Greetings()
        ans = greetings.hello("John")
        self.assertEqual(ans, "Hello John")


if __name__ == '__main__':
    unittest.main()
