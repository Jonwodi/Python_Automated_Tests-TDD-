import unittest

from hello_world import hello

class HelloWorldTest(unittest.TestCase):
  def test_say_hello(self):
    expected = "Hello World!"
    self.assertEqual(hello(), expected)

if __name__ == "__main__":
    unittest.main()