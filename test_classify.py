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
        self.assertEqual(len(data), 10)

    def test_ranges(self):
        data = [['AC008128', 73],['AC019221', 38],['AB040731', 52]]
        ranges = classify.thoseInRange(data, 0, 49)
        self.assertEqual(ranges[0],'AC019221')

if __name__ == '__main__':
    unittest.main()
