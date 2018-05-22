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

    def test_ranges_1(self):
        data = [['AC008128', 73],['AC019221', 38],['AB040731', 52]]
        ranges = classify.thoseInRange(data, 0, 20)
        self.assertEqual(ranges,["none"])

    def test_ranges_2(self):
        data = [['AC008128', 73],['AC019221', 38],['AB040731', 52]]
        ranges = classify.thoseInRange(data, 0, 49)
        self.assertEqual(ranges,['AC019221'])

    def test_ranges_3(self):
        data = [['AC008128', 73],['AC019221', 38],['AB040731', 52]]
        ranges = classify.thoseInRange(data, 0, 60)
        self.assertEqual(ranges,['AC019221','AB040731'])

if __name__ == '__main__':
    unittest.main()
