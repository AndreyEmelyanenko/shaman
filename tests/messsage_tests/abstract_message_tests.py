import unittest
import sys
sys.path.insert(0,'../..')
from shamanapp.abstract_message import Message

class TestMessage(unittest.TestCase):
    def test_clean_message_results1(self):
        message = Message()
        message.add_result_to_message('ex',1,'blarbla')

        self.assertTrue('blarbla' in message.results)

        # calling cleaning
        message.clean_fields()

        self.assertFalse('blarbla' in message.results)


    def test_clean_message_results2(self):
        message = Message()
        message.add_result_to_message('ex', 1, 'blarbla')

        self.assertTrue('blarbla' in message.results)

        # calling cleaning
        message.clean_fields()

        self.assertFalse('blarbla' in message.results)

        message.add_result_to_message('ex', 1, 'blarbla')

        self.assertTrue('blarbla' in message.results)

        # calling cleaning
        message.clean_fields()

        self.assertFalse('blarbla' in message.results)

    def test_clean_message_fields1(self):
        message = Message()
        message.cook = 'good'

        self.assertTrue('cook' in message.__dict__)

        # calling cleaning
        message.clean_fields()

        self.assertFalse('cook' in message.__dict__)


if __name__ == '__main__':
    unittest.main()

