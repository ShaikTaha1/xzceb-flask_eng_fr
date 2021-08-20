import unittest

from translator import englishToFrench, frenchToEnglish

class TestTranslator(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench("Hello"), 'Bonjour')
        self.assertEqual(englishToFrench(""), "")  


class TestDouble(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello") 
        self.assertEqual(frenchToEnglish(""), "")

unittest.main()