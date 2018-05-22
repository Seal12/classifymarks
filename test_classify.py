import unittest
import classify


class TestExclude(unittest.TestCase):

    def getData(self):
        fname = open("marks.dat")
        boundaries = list(map(int, ['0', '49', '59', '60', '69', '74', '100']))
        return fname, boundaries

    def test_getdata(self):
        fname, boundaries = self.getData()
        data = classify.getData(fname)
        fname.close()
        self.assertEqual(len(data),10)


if __name__ == '__main__':
    unittest.main()
