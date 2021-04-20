import unittest

from main import func


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

        result = func(input_value)

        expected = {
          'I': {
            'deserve': {
              'to': {
                 'be': 'hired'
              }
            }
          }
        }

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
