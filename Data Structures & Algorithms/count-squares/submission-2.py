class CountSquares:

    def __init__(self):
        self.data = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.data[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        px, py = point
        res = 0
        for (x, y), count in self.data.items():
            if (abs(x - px) != abs(y - py)) or x == px or y == py:
                continue
            res += count * self.data.get((x, py), 0) * self.data.get((px, y), 0)
        return res