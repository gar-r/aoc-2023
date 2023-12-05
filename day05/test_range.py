from unittest import TestCase

from day05.range import Range, RangeList


class TestRange(TestCase):
    def test_range_contains(self):
        r = Range(10, 3)
        self.assertTrue(r.contains(10))
        self.assertTrue(r.contains(11))
        self.assertTrue(r.contains(12))
        self.assertFalse(r.contains(13))
        self.assertFalse(r.contains(9))

    def test_rangelist_where(self):
        rs = RangeList([
            Range(0, 10),
            Range(20, 10),
            Range(33, 4)
        ])
        self.assertEqual(rs[0], rs.where(5))
        self.assertEqual(rs[1], rs.where(20))
        self.assertEqual(rs[2], rs.where(36))
        self.assertIsNone(rs.where(100))
