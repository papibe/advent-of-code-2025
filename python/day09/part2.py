from collections import namedtuple
from typing import List, Tuple

Corner = namedtuple("Corner", ["row", "col"])


def parse(filename: str) -> List[Corner]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    corners: List[Corner] = []
    for line in data:
        str_numbers: List[str] = line.split(",")
        corners.append(Corner(int(str_numbers[1]), int(str_numbers[0])))

    return corners


def calculate_area(x1: int, y1: int, x2: int, y2: int) -> float:
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)


def _intersect(edge: Tuple[Corner, Corner], gl_edge: Tuple[Corner, Corner]) -> bool:
    row1: int = min(edge[0].row, edge[1].row)
    col1: int = min(edge[0].col, edge[1].col)
    row2: int = max(edge[0].row, edge[1].row)
    col2: int = max(edge[0].col, edge[1].col)

    edge_row1: int = min(gl_edge[0].row, gl_edge[1].row)
    edge_col1: int = min(gl_edge[0].col, gl_edge[1].col)
    edge_row2: int = max(gl_edge[0].row, gl_edge[1].row)
    edge_col2: int = max(gl_edge[0].col, gl_edge[1].col)

    left_of_rect: bool = col2 <= edge_col1
    right_of_rect: bool = col1 >= edge_col2
    above: bool = row2 <= edge_row1
    below: bool = row1 >= edge_row2

    return not (left_of_rect or right_of_rect or above or below)


def intersect(c1: Corner, c2: Corner, green_lines: List[Tuple[Corner, Corner]]) -> bool:

    p1: Corner = Corner(min(c1.row, c2.row), min(c1.col, c2.col))
    p3: Corner = Corner(max(c1.row, c2.row), max(c1.col, c2.col))

    for gl_edge in green_lines:
        if _intersect((p1, p3), gl_edge):
            return True

    return False


def solve(corners: List[Corner]) -> int:
    green_lines: List[Tuple[Corner, Corner]] = []

    corner1: Corner
    corner2: Corner

    for i in range(len(corners)):
        corner1 = corners[i]
        corner2 = corners[(i + 1) % len(corners)]
        green_lines.append((corner1, corner2))

    areas: List[Tuple[float, Corner, Corner]] = []
    for i, corner1 in enumerate(corners):
        for j in range(i + 1, len(corners)):
            corner2 = corners[j]
            area: float = calculate_area(
                corner1.row, corner1.col, corner2.row, corner2.col
            )
            areas.append((area, corner1, corner2))

    areas.sort(reverse=True)
    for area, corner1, corner2 in areas:
        if not intersect(corner1, corner2, green_lines):
            return int(area)

    return -1


def solution(filename: str) -> int:
    corners: List[Corner] = parse(filename)
    return solve(corners)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 24
    print(solution("./input.txt"))  # 1654141440
