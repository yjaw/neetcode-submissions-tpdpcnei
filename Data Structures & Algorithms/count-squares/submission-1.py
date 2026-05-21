class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)
        self.points_on_x = defaultdict(set)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x, y)] += 1
        self.points_on_x[x].add(y)

    def count(self, point: List[int]) -> int:
        res = 0
        x, y = point

        for next_y in self.points_on_x[x]:
            if y == next_y:
                continue
            length = abs(y - next_y)
            res += 1 * self.points[(x, next_y)] * self.points[(x - length, y)] * self.points[(x - length, next_y)]
            res += 1 * self.points[(x, next_y)] * self.points[(x + length, y)] * self.points[(x + length, next_y)]

        return res