offsets = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1)
]


def neighbors(data: list[list], coord: tuple[int, int]) -> list:
    n = []
    for offset in offsets:
        nx = coord[0] + offset[0]
        ny = coord[1] + offset[1]
        if valid(data, (nx, ny)):
            n.append(data[nx][ny])
    return n


def valid(data: list[list], coord: tuple[int, int]) -> bool:
    size = (len(data), len(data[0]))
    if coord[0] < 0 or coord[0] >= size[0]:
        return False
    if coord[1] < 0 or coord[1] >= size[1]:
        return False
    return True
