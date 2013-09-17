import unittest
import blur
import numpy as np

class DiffOfDiffCheck(unittest.TestCase):

    def setUp(self):
        self.arr = np.array([0,1,2,3,4])
    
    def testDiffIndex0(self):
        self.assertEqual(blur.diffofdiff(self.arr, 0), 2)
    
    def testDiffIndex1(self):
        self.assertEqual(blur.diffofdiff(self.arr, 1), 1)
    
    def testDiff(self):
        self.assertEqual(blur.diffofdiff(self.arr, 2), 0)

    def testDiffPenultimateIndex(self):
        self.assertEqual(blur.diffofdiff(self.arr, 3), 1)

    def testUltimateIndex(self):
        self.assertEqual(blur.diffofdiff(self.arr, 4), 2)

    def testIndexErrorUnderflow(self):
        self.assertRaises(IndexError, blur.diffofdiff, [0], -1)

    def testIndexErrorOverflow(self):
        self.assertRaises(IndexError, blur.diffofdiff, [0], 1)

class ContrastCheck(unittest.TestCase):

    def setUp(self):
        self.arr = [0,1,2,3,4]
        
    def testContraseIndex0(self):
        self.assertEqual(blur.contrast(self.arr, 0), 2)        
        

if __name__ == '__main__':
    unittest.main()
