import unittest
import temp_converter

class Tests(unittest.TestCase):

    #check c_to_f returns correct values
    def test_c_to_f(self):
        self.assertEqual(212, temp_converter.c_to_f(100))

    #check f_to_c returns correct value
    def test_f_to_c(self):
        self.assertEqual(0, temp_converter.f_to_c(32))

if __name__ == '__main__':
    unittest.main()