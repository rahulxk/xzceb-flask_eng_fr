'''Unit test for tranlator functions'''
import unittest

from translator import english_to_french, french_to_english

class TestFrenchToEnglish(unittest.TestCase):
    '''class for French to English tranlator function'''
    def test1(self):
        '''Unit test for French to English function'''
        self.assertIsNone(english_to_french(None))
        self.assertEqual(french_to_english('Bonjour'),'Hello')

class TestEnglishToFrench(unittest.TestCase):
    '''class for English to French tranlator function'''
    def test1(self):
        '''Unit test function for English to French function'''
        self.assertIsNone(french_to_english(None))
        self.assertEqual(english_to_french('Hello'),'Bonjour')

unittest.main()
