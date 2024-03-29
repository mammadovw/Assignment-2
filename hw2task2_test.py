import Task_2
import unittest
from unittest.mock import patch
from io import StringIO

class TestMainFunction(unittest.TestCase):

    @patch('builtins.input', side_effect=["January", "24"])
    def test_main_input_calls(self, mock_input):
        Task_2.main() 
        expected_calls = ["Enter name of the month [ex. June]: ", "Enter the day [ex. 5]: "]
        # Check if input was called with the expected arguments
        self.assertEqual(mock_input.call_args_list, [unittest.mock.call(arg) for arg in expected_calls])
    
    def test_winter(self):
        test_cases = [
            {'input': ('December', 21), 'expected_output': 'December 21 is in Winter'},
            {'input': ('December', 31), 'expected_output': 'December 31 is in Winter'},
            {'input': ('January', 1), 'expected_output': 'January 1 is in Winter'},
            {'input': ('January', 31), 'expected_output': 'January 31 is in Winter'},
            {'input': ('February', 1), 'expected_output': 'February 1 is in Winter'},
            {'input': ('February', 28), 'expected_output': 'February 28 is in Winter'},
            {'input': ('March', 1), 'expected_output': 'March 1 is in Winter'},
            {'input': ('March', 19), 'expected_output': 'March 19 is in Winter'}
        ]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=test_case['input']), \
                patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                Task_2.main()
            self.assertEqual(mock_stdout.getvalue().strip(), test_case['expected_output'])
    
    def test_spring(self):
        test_cases = [
            {'input': ('March', 20), 'expected_output': 'March 20 is in Spring'},
            {'input': ('March', 31), 'expected_output': 'March 31 is in Spring'},
            {'input': ('April', 1), 'expected_output': 'April 1 is in Spring'},
            {'input': ('April', 30), 'expected_output': 'April 30 is in Spring'},
            {'input': ('May', 1), 'expected_output': 'May 1 is in Spring'},
            {'input': ('May', 31), 'expected_output': 'May 31 is in Spring'},
            {'input': ('June', 1), 'expected_output': 'June 1 is in Spring'},
            {'input': ('June', 20), 'expected_output': 'June 20 is in Spring'}
        ]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=test_case['input']), \
                patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                Task_2.main()
            self.assertEqual(mock_stdout.getvalue().strip(), test_case['expected_output'])
    
    def test_summer(self):
        test_cases = [
            {'input': ('June', 21), 'expected_output': 'June 21 is in Summer'},
            {'input': ('June', 30), 'expected_output': 'June 30 is in Summer'},
            {'input': ('July', 1), 'expected_output': 'July 1 is in Summer'},
            {'input': ('July', 31), 'expected_output': 'July 31 is in Summer'},
            {'input': ('August', 1), 'expected_output': 'August 1 is in Summer'},
            {'input': ('August', 30), 'expected_output': 'August 30 is in Summer'},
            {'input': ('September', 1), 'expected_output': 'September 1 is in Summer'},
            {'input': ('September', 21), 'expected_output': 'September 21 is in Summer'},
        ]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=test_case['input']), \
                patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                Task_2.main()
            self.assertEqual(mock_stdout.getvalue().strip(), test_case['expected_output'])
    
    def test_fall(self):
        test_cases = [
            {'input': ('September', 22), 'expected_output': 'September 22 is in Fall'},
            {'input': ('October', 1), 'expected_output': 'October 1 is in Fall'},
            {'input': ('October', 31), 'expected_output': 'October 31 is in Fall'},
            {'input': ('November', 1), 'expected_output': 'November 1 is in Fall'},
            {'input': ('November', 30), 'expected_output': 'November 30 is in Fall'},
            {'input': ('December', 1), 'expected_output': 'December 1 is in Fall'},
            {'input': ('December', 20), 'expected_output': 'December 20 is in Fall'},
        ]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=test_case['input']), \
                patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                Task_2.main()
            self.assertEqual(mock_stdout.getvalue().strip(), test_case['expected_output'])
