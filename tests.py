import unittest
from main import is_https

class Test(unittest.TestCase):
    def test_1(self):
        """Checking right domain"""
        self.assertTrue(is_https("https://mejorconsalud.as.com"))
    
    def test_2(self):
        """Checking http protocol"""
        self.assertTrue(is_https("http://lamenteesmaravillosa.com"))


if __name__ == "__main__":
    unittest.main()