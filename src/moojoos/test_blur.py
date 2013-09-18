import unittest
import blur
import numpy as np

class DiffOfDiffCheck(unittest.TestCase):

    def setUp(self):
        self.arr = np.array([0,1,2,3,4])
    
    def testDiffIndex0(self):
        self.assertEqual(blur._diffofdiff(self.arr, 0), 2)
    
    def testDiffIndex1(self):
        self.assertEqual(blur._diffofdiff(self.arr, 1), 1)
    
    def testDiff(self):
        self.assertEqual(blur._diffofdiff(self.arr, 2), 0)

    def testDiffPenultimateIndex(self):
        self.assertEqual(blur._diffofdiff(self.arr, 3), 1)

    def testUltimateIndex(self):
        self.assertEqual(blur._diffofdiff(self.arr, 4), 2)

    def testIndexErrorUnderflow(self):
        self.assertRaises(IndexError, blur._diffofdiff, [0], -1)

    def testIndexErrorOverflow(self):
        self.assertRaises(IndexError, blur._diffofdiff, [0], 1)

class ContrastCheck(unittest.TestCase):

    def setUp(self):
        self.arr = [50,20,30,40,10]
        
    def testContrastIndex0(self):
        self.assertEqual(blur._contrast(self.arr, 0), 0)     
        
    def testContrastIndex1(self):
        self.assertEqual(blur._contrast(self.arr, 1), 30)            

    def testContrastIndex2(self):
        self.assertEqual(blur._contrast(self.arr, 2), 10)   
        
    def testContrastIndex3(self):
        self.assertEqual(blur._contrast(self.arr, 3), 10)  

    def testContrastIndex4(self):
        self.assertEqual(blur._contrast(self.arr, 4), 30)    
        
    def testIndexErrorUnderflow(self):
        self.assertRaises(IndexError, blur._contrast, [0], -1)

    def testIndexErrorOverflow(self):
        self.assertRaises(IndexError, blur._contrast, [0], 1)        

if __name__ == '__main__':
    unittest.main()