import unittest
import blur


class FooCheck(unittest.TestCase):

    def setUp(self):
        self.arr = [0,1,2,3,4]
    
    def testDiffIndex0(self):
        self.assertEqual(blur.diff_of_diff(self.arr, 0), 2)
    
    def testDiffIndex1(self):
        self.assertEqual(blur.diff_of_diff(self.arr, 1), 1)
    
    def testDiff(self):
        self.assertEqual(blur.diff_of_diff(self.arr, 2), 0)

    def testDiffPenultimateIndex(self):
        self.assertEqual(blur.diff_of_diff(self.arr, 3), 1)

    def testUltimateIndex(self):
        self.assertEqual(blur.diff_of_diff(self.arr, 4), 2)

    def testIndexErrorUnderflow(self):
        self.assertRaises(IndexError, blur.diff_of_diff, [0], -1)

    def testIndexErrorOverflow(self):
        self.assertRaises(IndexError, blur.diff_of_diff, [0], 1)


if __name__ == '__main__':
    unittest.main()
