import re
from collections import namedtuple
from typing import List, Match, Optional, Tuple

Area = namedtuple("Area", ["rows", "cols", "quantities"])
Shape = namedtuple("Shape", ["rows", "cols", "grid", "used"])


def parse(filename: str) -> Tuple[List[Shape], List[Area]]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    re_shape: str = r"^\d:$"
    re_area: str = r"(\d+)x(\d+): (\d+) (\d+) (\d+) (\d+) (\d+) (\d+)"

    shapes: List[Shape] = []
    areas: List[Area] = []

    index: int = 0
    while index < len(data):
        # parse shape
        matches: Optional[Match[str]] = re.match(re_shape, data[index])
        if matches:
            shape = []
            index += 1
            for _ in range(3):
                shape.append([c for c in data[index]])
                index += 1

            used: int = 0
            for line in shape:
                for cell in line:
                    if cell == "#":
                        used += 1

            shapes.append(Shape(rows=3, cols=3, grid=shape, used=used))

        # parse area
        matches = re.match(re_area, data[index])
        if matches:
            area: Area = Area(
                rows=int(matches[1]),
                cols=int(matches[2]),
                quantities=[
                    int(matches[3]),
                    int(matches[4]),
                    int(matches[5]),
                    int(matches[6]),
                    int(matches[7]),
                    int(matches[8]),
                ],
            )

            areas.append(area)

        index += 1

    return shapes, areas


def fit_shapes(area: Area, shapes: List[Shape]) -> bool:
    area_size: int = area.rows * area.cols
    shape: Shape

    min_area_requires: int = 0
    for shape_number, required_amount in enumerate(area.quantities):
        shape = shapes[shape_number]
        min_area_requires += shape.rows * shape.cols * required_amount

    if min_area_requires <= area_size:
        return True

    min_used_required: int = 0
    for shape_number, required_amount in enumerate(area.quantities):
        shape = shapes[shape_number]
        min_used_required += shape.used * required_amount

    if min_used_required > area_size:
        return False

    raise RuntimeError("precise size fitting not implemented")


def solve(shapes: List[Shape], areas: List[Area]) -> int:
    total_sum: int = 0

    for area in areas:
        if fit_shapes(area, shapes):
            total_sum += 1

    return total_sum


def solution(filename: str) -> int:
    shapes, areas = parse(filename)
    return solve(shapes, areas)


if __name__ == "__main__":
    print(solution("./input.txt"))  # 575
