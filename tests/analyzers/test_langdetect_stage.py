import unittest
import sys
sys.path.insert(0,'../..')
from shamanapp.abstract_message import Message
from shamanapp.analyzers.analyzer_stages.langdetect_stage import LangDetectStage


class TestLangDetect(unittest.TestCase):

    stage = LangDetectStage({'order':1})

    def test_ru_langdetect(self):
        message = Message()
        message.clean_text = \
            "Одним из самых популярных направлений является отдых в Турции, " \
            "где роскошные отели всегда готовы к приему гостей."
        message = self.stage.do_stage(message)
        self.assertEqual('ru',message.results['mongo_extra']['extra']['lang']['lang'])

    def test_ar_langdetect(self):
        message = Message()
        message.clean_text = "موقع نتائج طلاب العراق | القبول المركزي 2016   اطرح سؤال/استفسار " \
                             "   اخر الاخبار    نتائج السادس الاعدادي  نتائج الثالث المتوسط   نتائج السادس" \
                             " الابتدائي  نتائج التعليم المهني  اتصل بنا   نتائج القبول المركزي للكليات" \
                             " والمعاهد العراقية 2016 نتائج قبولات الجامعات العراقية          موقع "
        message = self.stage.do_stage(message)
        self.assertEqual('ar', message.results['mongo_extra']['extra']['lang']['lang'])

    def test_kz_langdetect(self):
        message = Message()
        message.clean_text = \
            "Местоположение Павлодар Актау Актобе Алматы Астана Атырау Аягоз Жанаозен Караганда Каскелен Кокшетау " \
            "Костанай Кызылорда Петропавловск Семей Талдыкорган Тараз Темиртау Уральск Усть-Каменогорск Шымкент " \
            "Экибастуз   Тип "
        message = self.stage.do_stage(message)
        self.assertEqual('ru',message.results['mongo_extra']['extra']['lang']['lang'])

    def test_pl_langdetect(self):
        message = Message()
        message.clean_text = \
            "DinoAnimals.pl - Zwierzęta, Dinozaury, Rośliny  DinoAnimals.pl DobreSciagi.pl Zonka.pl DinoAnimals.com " \
            "Fakty.DinoAnimals.pl Blogi Galeria Forum 06 12 2016  Subscribe to rss Home Zwierzęta Ssaki Gryzonie " \
            "Hipopotamy Kotowate Koty domowe Lamparty Lwy Tygrysy "
        message = self.stage.do_stage(message)
        self.assertEqual('pl',message.results['mongo_extra']['extra']['lang']['lang'])

    def test_vi_langdetect(self):
        message = Message()
        message.clean_text = \
            "Xổ Số Minh Ngọc *NEW* - Hệ Thống Xổ Số Hiện Đại Nhất         Đăng Ký  Cài Đặt Thông Tin Vé Dò Đăng Xuất Menu  " \
            "   XSMN XSMT XSMB Mega 6/45 Max 4D Dò Vé   Xổ Số Trực Tiếp  Trực Tiếp Xổ Số Miền Nam Trực Tiếp Xổ Số Miền Trung " \
            "Trực Tiếp Xổ Số Miền Bắc Trực Tiếp Xổ Số Điện "
        message = self.stage.do_stage(message)
        self.assertEqual('vi',message.results['mongo_extra']['extra']['lang']['lang'])

    def test_pt_langdetect(self):
        message = Message()
        message.clean_text = \
            "  idealista — Moradias e apartamentos, arrendamento e venda, anúncios gratuitos       A maneira certa " \
            "de encontrar casa   Português      English     Français     Deutsch     Italiano     Español   idealista.com  " \
            "idealista.it     Inserir anúncio grátis   Acesso  utilizadores   Casa em Matosinhos e Leça da Palmeira"
        message = self.stage.do_stage(message)
        self.assertEqual('pt',message.results['mongo_extra']['extra']['lang']['lang'])

    def test_sk_langdetect(self):
        message = Message()
        message.clean_text = \
            "Magazín - Klocher.sk   Hľadaj Zaujímavosti Náhodne  Budúce hviezdy YouTube? #2: Boncamila  2. augusta 2016  " \
            "Z domova ,   Zaujímavosti Podobné  Krok za krokom: Herci z obľúbeného seriálu sa rokmi poriadne zmenili. " \
            "Ako dnes vyzerá fešák J.T. či kráska Karen?! "
        message = self.stage.do_stage(message)
        self.assertEqual('sk',message.results['mongo_extra']['extra']['lang']['lang'])

    def test_cs_langdetect(self):
        message = Message()
        message.clean_text = \
            "Pravidla českého pravopisu - Pravidla.cz       Psaní i a y Psaní ě Zkratky Tituly Více " \
            "Do hledacího políčka zadejte slovo, které chcete v pravidlech českého pravopisu vyhledat:"
        message = self.stage.do_stage(message)
        self.assertEqual('cs',message.results['mongo_extra']['extra']['lang']['lang'])


if __name__ == '__main__':
    unittest.main()