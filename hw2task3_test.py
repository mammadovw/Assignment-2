import Task_3
import unittest
from unittest.mock import patch
from io import StringIO

class TestMainFunction(unittest.TestCase):

    @patch('builtins.input', side_effect = ['425'])
    def test_main_input_calls(self, mock_input):
        Task_3.main()
        expected_calls = ["Enter the wavelength in nm: "]
        self.assertEqual(mock_input.call_args_list, [unittest.mock.call(arg) for arg in expected_calls])

    def test_invalid_input(self):
        test_cases = [
            {'input': 760, 'expected_output': 'Invalid input!'},
            {'input': 370, 'expected_output': 'Invalid input!'},
            # Add more test cases for invalid input...
        ]
        for test_case in test_cases:
            with patch('builtins.input', return_value=test_case['input']), \
                 patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                Task_3.main()
            self.assertEqual(mock_stdout.getvalue().strip(), test_case['expected_output'])

    def test_violet(self):
        test_cases = [
            {'input': 380, 'expected_output': 'The relevant color is Violet'},
            {'input': 449, 'expected_output': 'The relevant color is Violet'}
        ]

        for test_case in test_cases:
            with patch('builtins.input', return_value=test_case['input']), \
                patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                Task_3.main()
            self.assertEqual(mock_stdout.getvalue().strip(), test_case['expected_output'])

    def test_blue(self):
        test_cases = [
            {'input': 450, 'expected_output': 'The relevant color is Blue'},
            {'input': 494, 'expected_output': 'The relevant color is Blue'}
        ]

        for test_case in test_cases:
            with patch('builtins.input', return_value=test_case['input']), \
                patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                Task_3.main()
            self.assertEqual(mock_stdout.getvalue().strip(), test_case['expected_output'])

    def test_green(self):
        test_cases = [
            {'input': 495, 'expected_output': 'The relevant color is Green'},
            {'input': 569, 'expected_output': 'The relevant color is Green'}
        ]

        for test_case in test_cases:
            with patch('builtins.input', return_value=test_case['input']), \
                patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                Task_3.main()
            self.assertEqual(mock_stdout.getvalue().strip(), test_case['expected_output'])

    def test_yellow(self):
        test_cases = [
            {'input': 589, 'expected_output': 'The relevant color is Yellow'},
            {'input': 570, 'expected_output': 'The relevant color is Yellow'}
        ]

        for test_case in test_cases:
            with patch('builtins.input', return_value=test_case['input']), \
                patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                Task_3.main()
            self.assertEqual(mock_stdout.getvalue().strip(), test_case['expected_output'])
    
    def test_orange(self):
        test_cases = [
            {'input': 590, 'expected_output': 'The relevant color is Orange'},
            {'input': 619, 'expected_output': 'The relevant color is Orange'}
        ]

        for test_case in test_cases:
            with patch('builtins.input', return_value=test_case['input']), \
                patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                Task_3.main()
            self.assertEqual(mock_stdout.getvalue().strip(), test_case['expected_output'])
    
    def test_red(self):
        test_cases = [
            {'input': 620, 'expected_output': 'The relevant color is Red'},
            {'input': 749, 'expected_output': 'The relevant color is Red'}
        ]

        for test_case in test_cases:
            with patch('builtins.input', return_value=test_case['input']), \
                patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                Task_3.main()
            self.assertEqual(mock_stdout.getvalue().strip(), test_case['expected_output'])
