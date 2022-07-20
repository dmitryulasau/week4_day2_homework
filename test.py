from unittest import TestCase, main
from palindrome import palindrome

class PalindromeTestCase(TestCase):
    def test_1_palindrome(self):
        self.assertTrue(palindrome('A man, a plan, a canal: Panama'), 'amanaplanacanalpanama')
    
    def test_2_not_palindrome(self):
        self.assertFalse(palindrome('race a car'), 'raceacar')

    def test_3_empty_palindrome(self):
        self.assertTrue(palindrome(''), '')

