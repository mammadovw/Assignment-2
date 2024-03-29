import Task_1
import unittest
from unittest.mock import patch
from io import StringIO

class TestMainFunction(unittest.TestCase):

    @patch('builtins.input', side_effect=["abracadabra"])
    def test_main_input_calls(self, mock_input):
        Task_1.main() 
        expected_calls = ["Enter a letter of the alphabet: "]
        # Check if input was called with the expected arguments
        self.assertEqual(mock_input.call_args_list, [unittest.mock.call(arg) for arg in expected_calls])

    def test_input_vowel(self):
        input_value = [97, 101, 105, 111, 117]
        expected_output = 'Entered alphabet is a vowel!'
        for test in input_value:
            with patch('builtins.input', return_value=chr(test)), \
                patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                Task_1.main()
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_input_consonant(self):
        input_value = [98, 99, 100, 102, 103, 104, 106, 107, 108, 109, 110, 112, 113, 114, 115, 116, 118, 119, 120, 122]
        expected_output = 'Entered alphabet is a consonant!'
        for test in input_value:
            with patch('builtins.input', return_value=chr(test)), \
                patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                Task_1.main()
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_input_y(self):
        input_value = 121
        expected_output = 'Sometimes it is a vowel, and sometimes it is a consonant!'
        with patch('builtins.input', return_value=chr(input_value)), \
             patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            Task_1.main()
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
    

if __name__ == '__main__':
    unittest.main()
