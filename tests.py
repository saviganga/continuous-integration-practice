import unittest
import temp_converter
import distance_converter

class Tests(unittest.TestCase):

    # check celcius_to_fahrenheit returns correct values
    def test_c_to_f(self):
        self.assertEqual(68.9, temp_converter.c_to_f(20.5))

    # check f_to_c returns correct value
    def test_f_to_c(self):

        self.assertEqual(0, temp_converter.f_to_c(32))

    def test_km_to_m(self):
        self.assertEqual(3, distance_converter.km_to_m(3000))

    def test_m_to_km(self):
        self.assertEqual(15000, distance_converter.m_to_km(15))

if __name__ == '__main__':
    unittest.main()
