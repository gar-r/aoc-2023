from dataclasses import dataclass


@dataclass
class Race:
    time: int  # race time
    dtb: int  # distance to beat

    def calc_distance(self, charge_time):
        return (self.time - charge_time) * charge_time


