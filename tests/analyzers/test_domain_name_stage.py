import unittest
import sys


sys.path.insert(0,'../..')
from shamanapp.abstract_message import Message
from shamanapp.analyzers.general_stages.domain_name_stage import DomainNameStage

class TestDomainLevelStage(unittest.TestCase):

    stage = DomainNameStage({'order':1})

    def test_ex1_domain_name(self):
        message = Message()
        message.url = "http://yandex.ru/"
        message = self.stage.do_stage(message)
        self.assertEqual("yandex.ru",message.results['mongo_extra']['domain'])

    def test_ex2_domain_name(self):
        message = Message()
        message.url = "http://yandex.ru/qwe/qwe/qwe"
        message = self.stage.do_stage(message)
        self.assertEqual("yandex.ru",message.results['mongo_extra']['domain'])

    def test_ex3_domain_name(self):
        message = Message()
        message.url = "yandex.ru/qwe/qwe/"
        message = self.stage.do_stage(message)
        self.assertEqual("yandex.ru",message.results['mongo_extra']['domain'])

if __name__ == '__main__':
    unittest.main()