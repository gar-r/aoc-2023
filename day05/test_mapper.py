from unittest import TestCase

from day05.mapper import Mapper, MapperList, MapperChain


class TestMapper(TestCase):
    def test_mapper_remap(self):
        m = Mapper(20, 10, 5)
        self.assertEqual(5, m.remap(20))
        self.assertEqual(6, m.remap(21))
        self.assertEqual(14, m.remap(29))

    def test_mapper_list_remap(self):
        ml = MapperList([
            Mapper(0, 10, 100),
            Mapper(20, 10, 50),
            Mapper(33, 4, 0)
        ])
        self.assertEqual(54, ml.remap(24))
        self.assertEqual(3, ml.remap(36))

    def test_mapper_chain_remap(self):
        mc = MapperChain([
            MapperList([
                Mapper(0, 10, 100),
                Mapper(50, 10, 20),
            ]),
            MapperList([
                Mapper(100, 5, 50)
            ])
        ])
        self.assertEqual(54, mc.remap(4))
        self.assertEqual(29, mc.remap(59))
