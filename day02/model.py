from dataclasses import dataclass


@dataclass
class Game:
    number: int
    sets: list

    def valid(self, r_max: int, g_max: int, b_max: int):
        for s in self.sets:
            if s.R > r_max or s.G > g_max or s.B > b_max:
                return False
        return True

    def min_valid(self):
        res = Set(0, 0, 0)
        for s in self.sets:
            if s.R > res.R:
                res.R = s.R
            if s.G > res.G:
                res.G = s.G
            if s.B > res.B:
                res.B = s.B
        return res


@dataclass
class Set:
    R: int
    G: int
    B: int

    def pow(self):
        return self.R * self.G * self.B