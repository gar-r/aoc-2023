from dataclasses import dataclass

from day05.range import Range


@dataclass
class Mapper(Range):
    dst: int

    def remap(self, i):
        return self.dst + (i - self.start)


class MapperList(list[Mapper]):

    def remap(self, i):
        for m in self:
            if m.contains(i):
                return m.remap(i)
        return i


class MapperChain(list[MapperList]):

    def remap(self, i):
        res = i
        for ml in self:
            res = ml.remap(res)
        return res

