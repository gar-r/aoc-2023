from dataclasses import dataclass


@dataclass
class Range:
    start: int
    length: int

    def contains(self, i):
        return self.start <= i < self.start + self.length


class RangeList(list[Range]):

    def where(self, i):
        for r in self:
            if r.contains(i):
                return r
        return None
