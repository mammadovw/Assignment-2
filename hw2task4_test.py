import unittest
from io import StringIO
from unittest.mock import patch
from random import randint
import Task_4

class TestMainFunction(unittest.TestCase):

    @patch('builtins.input', side_effect=["2021"])
    def test_main_input_calls(self, mock_input):
        Task_4.main() 
        expected_calls = ["Enter the year [ex. 2021]: "]
        # Check if input was called with the expected arguments
        self.assertEqual(mock_input.call_args_list, [unittest.mock.call(arg) for arg in expected_calls])

    def test_zodiac(self):
        data = {0:"Monkey", 1:"Rooster", 2:"Dog", 3:"Pig", 4:"Rat", 5:"Ox", 6:"Tiger", 7:"Hare", 8:"Dragon", 9:"Snake", 10:"Horse", 11:"Sheep"} 
        dates = [0 for i in range(12)]
        idx = 0
        while idx < 12:
            date = randint(1, 10000)
            if dates[date%12] == 0: 
                dates[date%12] = date
                idx += 1
        for test_case in dates:
            with patch('builtins.input', return_value=test_case), \
                 patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                Task_4.main()
            expected_output =  f'{test_case} is the year of the {data[test_case%12]}'
            self.assertEqual(mock_stdout.getvalue().strip(),expected_output)

    def test_invalid_year(self):
        test_cases = [
            {'input': -1, 'expected_output': 'Invalid year!'},
            {'input': -2021, 'expected_output': 'Invalid year!'},
        ]
        for test_case in test_cases:
            with patch('builtins.input', return_value=test_case['input']), \
                 patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                Task_4.main()
            self.assertEqual(mock_stdout.getvalue().strip(), test_case['expected_output'])

if __name__ == '__main__':
    unittest.main()
