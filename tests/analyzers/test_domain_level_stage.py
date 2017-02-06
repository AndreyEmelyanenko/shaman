import unittest
import sys
sys.path.insert(0,'../..')
from shamanapp.abstract_message import Message
from shamanapp.analyzers.general_stages.domain_level_stage import DomainLevelStage

class TestDomainLevelStage(unittest.TestCase):

    stage = DomainLevelStage({'order':1})

    def test_1l_with_right_slash_domain_level(self):
        message = Message()
        message.url = "http://yandex.ru/"
        message = self.stage.do_stage(message)
        self.assertEqual(1,message.results['mongo_extra']['domain_level'])

    def test_1l_no_right_slash_domain_level(self):
        message = Message()
        message.url = "http://yandex.ru"
        message = self.stage.do_stage(message)
        self.assertEqual(1,message.results['mongo_extra']['domain_level'])

    def test_2l_domain_level(self):
        message = Message()
        message.url = "http://yandex.ru/qweqwe/"
        message = self.stage.do_stage(message)
        self.assertEqual(2, message.results['mongo_extra']['domain_level'])

    def test_no_scheme_domain_level(self):
        message = Message()
        message.url = "yandex.ru/qweqwe/"
        message = self.stage.do_stage(message)
        self.assertEqual(2, message.results['mongo_extra']['domain_level'])

if __name__ == '__main__':
    unittest.main()