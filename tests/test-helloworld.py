import unittest

class HelloWorldTestCase(unittest.TestCase):
    def test_helloworld_equals_helloworld(self):
        # this test should pass fairly consistently
        self.assertEqual('Hello world!', 'Hello world!')

if __name__ == '__main__':
    unittest.main()
