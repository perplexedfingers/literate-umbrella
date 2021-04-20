import unittest

from main import func, traverse


class TestCase(unittest.TestCase):
    def test_input_output(self):
        input_value = {
          'hired': {
            'be': {
              'to': {
                'deserve': 'I'
              }
            }
          }
        }

        expected = {
          'I': {
            'deserve': {
              'to': {
                 'be': 'hired'
              }
            }
          }
        }

        result = func(input_value)

        self.assertEqual(result, expected)

    def test_traverse(self):
        input = {'a': {'b': 'c'}}
        expected = ['a', 'b', 'c']
        result = traverse(input)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
