from collections import namedtuple
from typing import List

Corner = namedtuple("Corner", ["x", "y"])


def parse(filename: str) -> List[Corner]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    corners: List[Corner] = []
    for line in data:
        str_numbers: List[str] = line.split(",")
        corners.append(Corner(int(str_numbers[0]), int(str_numbers[1])))

    return corners


def area(x1: int, y1: int, x2: int, y2: int) -> float:
    return abs(x1 - x2 + 1) * abs(y1 - y2 + 1)


def solve(corners: List[Corner]) -> int:
    max_area = float("-inf")

    for i, corner1 in enumerate(corners):
        for j in range(i + 1, len(corners)):
            corner2: Corner = corners[j]
            max_area = max(max_area, area(corner1.x, corner1.y, corner2.x, corner2.y))

    return int(max_area)


def solution(filename: str) -> int:
    corners: List[Corner] = parse(filename)
    return solve(corners)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 50
    print(solution("./input.txt"))  # 4739623064
