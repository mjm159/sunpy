"""BaseMap tests"""
import unittest
import sunpy
import pyfits
import os

class TestBaseMap(unittest.TestCase):
    def setUp(self):
        self.file = 'sunpy/dev/sample-data/AIA20110319_105400_0171.fits'
        self.map = sunpy.Map(self.file) 

    def tearDown(self):
        self.map = None

    def test_fits_data_comparison(self):
        fits = pyfits.open(self.file)
        self.assertEqual(self.map.tolist(), fits[0].data.tolist(),
                         'data not preserved')
    def test_fits_header_comparison(self):
        fits = pyfits.open(self.file)
        self.assertEqual(self.map.header.keys(), fits[0].header.keys(),
                         'header not preserved')

print(os.path.realpath('sunpy/dev/sample-data/AIA20110319_105400_0171.fits'))
suite = unittest.TestLoader().loadTestsFromTestCase(TestBaseMap)
unittest.TextTestRunner(verbosity=2).run(suite)
