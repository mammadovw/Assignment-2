import unittest
from io import StringIO
from unittest.mock import patch
import Task_5

class TestMainFunction(unittest.TestCase):

    @patch('builtins.input', side_effect=["March", "12"])
    def test_main_input_calls(self, mock_input):
        Task_5.main() 
        expected_calls = ["Enter a month [ex. March]: ", "Enter the day [ex. 12]: "]
        # Check if input was called with the expected arguments
        self.assertEqual(mock_input.call_args_list, [unittest.mock.call(arg) for arg in expected_calls])

    def test_zodiac1(self):
        test_cases = [
            {'input': ["December", 22], 'expected_output': 'Your zodiac sign is Capricorn'},
            {'input': ["December", 31], 'expected_output': 'Your zodiac sign is Capricorn'},
            {'input': ["January", 1], 'expected_output': 'Your zodiac sign is Capricorn'},
            {'input': ["January", 19], 'expected_output': 'Your zodiac sign is Capricorn'},
            {'input': ["January", 20], 'expected_output': 'Your zodiac sign is Aquarius'},
            {'input': ["January", 31], 'expected_output': 'Your zodiac sign is Aquarius'},
            {'input': ["February", 1], 'expected_output': 'Your zodiac sign is Aquarius'},
            {'input': ["February", 18], 'expected_output': 'Your zodiac sign is Aquarius'},
            {'input': ["February", 19], 'expected_output': 'Your zodiac sign is Pisces'},
            {'input': ["February", 29], 'expected_output': 'Your zodiac sign is Pisces'},
            {'input': ["March", 1], 'expected_output': 'Your zodiac sign is Pisces'},
            {'input': ["March", 20], 'expected_output': 'Your zodiac sign is Pisces'}
        ]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=test_case['input']), \
                 patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                Task_5.main()
            self.assertEqual(mock_stdout.getvalue().strip(), test_case['expected_output'])

    def test_zodiac2(self):
        test_cases = [
            {'input': ["June", 20], 'expected_output': 'Your zodiac sign is Gemini'},
            {'input': ["June", 1], 'expected_output': 'Your zodiac sign is Gemini'},
            {'input': ["May", 31], 'expected_output': 'Your zodiac sign is Gemini'},
            {'input': ["May", 21], 'expected_output': 'Your zodiac sign is Gemini'},
            {'input': ["May", 20], 'expected_output': 'Your zodiac sign is Taurus'},
            {'input': ["May", 1], 'expected_output': 'Your zodiac sign is Taurus'},
            {'input': ["April", 30], 'expected_output': 'Your zodiac sign is Taurus'},
            {'input': ["April", 20], 'expected_output': 'Your zodiac sign is Taurus'},
            {'input': ["April", 19], 'expected_output': 'Your zodiac sign is Aries'},
            {'input': ["April", 1], 'expected_output': 'Your zodiac sign is Aries'},
            {'input': ["March", 31], 'expected_output': 'Your zodiac sign is Aries'},
            {'input': ["March", 21], 'expected_output': 'Your zodiac sign is Aries'}
        ]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=test_case['input']), \
                 patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                Task_5.main()
            self.assertEqual(mock_stdout.getvalue().strip(), test_case['expected_output'])

    def test_zodiac3(self):
        test_cases = [
            {'input': ["June", 21], 'expected_output': 'Your zodiac sign is Cancer'},
            {'input': ["June", 30], 'expected_output': 'Your zodiac sign is Cancer'},
            {'input': ["July", 1], 'expected_output': 'Your zodiac sign is Cancer'},
            {'input': ["July", 22], 'expected_output': 'Your zodiac sign is Cancer'},
            {'input': ["July", 23], 'expected_output': 'Your zodiac sign is Leo'},
            {'input': ["July", 31], 'expected_output': 'Your zodiac sign is Leo'},
            {'input': ["August", 1], 'expected_output': 'Your zodiac sign is Leo'},
            {'input': ["August", 22], 'expected_output': 'Your zodiac sign is Leo'},
            {'input': ["August", 23], 'expected_output': 'Your zodiac sign is Virgo'},
            {'input': ["August", 31], 'expected_output': 'Your zodiac sign is Virgo'},
            {'input': ["September", 1], 'expected_output': 'Your zodiac sign is Virgo'},
            {'input': ["September", 22], 'expected_output': 'Your zodiac sign is Virgo'}
        ]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=test_case['input']), \
                 patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                Task_5.main()
            self.assertEqual(mock_stdout.getvalue().strip(), test_case['expected_output'])

    def test_zodiac4(self):
        test_cases = [
            {'input': ["December", 21], 'expected_output': 'Your zodiac sign is Sagittarius'},
            {'input': ["December", 1], 'expected_output': 'Your zodiac sign is Sagittarius'},
            {'input': ["November", 30], 'expected_output': 'Your zodiac sign is Sagittarius'},
            {'input': ["November", 22], 'expected_output': 'Your zodiac sign is Sagittarius'},
            {'input': ["November", 21], 'expected_output': 'Your zodiac sign is Scorpion'},
            {'input': ["November", 1], 'expected_output': 'Your zodiac sign is Scorpion'},
            {'input': ["October", 31], 'expected_output': 'Your zodiac sign is Scorpion'},
            {'input': ["October", 23], 'expected_output': 'Your zodiac sign is Scorpion'},
            {'input': ["October", 22], 'expected_output': 'Your zodiac sign is Libra'},
            {'input': ["October", 1], 'expected_output': 'Your zodiac sign is Libra'},
            {'input': ["September", 30], 'expected_output': 'Your zodiac sign is Libra'},
            {'input': ["September", 23], 'expected_output': 'Your zodiac sign is Libra'}
        ]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=test_case['input']), \
                 patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                Task_5.main()
            self.assertEqual(mock_stdout.getvalue().strip(), test_case['expected_output'])

    def test_invalid_date(self):
        test_cases = [
            {'input': ["February", 30], 'expected_output': 'Either a month or a day is invalid!'},
            {'input': ["June", 31], 'expected_output': 'Either a month or a day is invalid!'},
            {'input': ["November", 31], 'expected_output': 'Either a month or a day is invalid!'},
            {'input': ["May", -5], 'expected_output': 'Either a month or a day is invalid!'},
            {'input': ["july", 31], 'expected_output': 'Either a month or a day is invalid!'},
        ]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=test_case['input']), \
                 patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                Task_5.main()
            self.assertEqual(mock_stdout.getvalue().strip(), test_case['expected_output'])

if __name__ == '__main__':
    unittest.main()
