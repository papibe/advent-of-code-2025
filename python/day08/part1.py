from math import sqrt
from typing import Dict, List, Tuple


class JunctionBoxes:
    def __init__(self, x: int, y: int, z: int) -> None:
        self.x: int = x
        self.y: int = y
        self.z: int = z

    def distance(self, jb: "JunctionBoxes") -> float:
        return sqrt((self.x - jb.x) ** 2 + (self.y - jb.y) ** 2 + (self.z - jb.z) ** 2)


class UnionFind:
    def __init__(self, size: int) -> None:
        self.parent: List[int] = list(range(size))

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])

    def union(self, i: int, j: int) -> None:
        i_root: int = self.find(i)
        j_root: int = self.find(j)
        self.parent[i_root] = j_root


def parse(filename: str) -> List[JunctionBoxes]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    junction_boxes: List[JunctionBoxes] = []
    for line in data:
        str_numbers: List[str] = line.split(",")
        x: int = int(str_numbers[0])
        y: int = int(str_numbers[1])
        z: int = int(str_numbers[2])
        junction_boxes.append(JunctionBoxes(x, y, z))

    return junction_boxes


def solve(junction_boxes: List[JunctionBoxes], connections: int) -> int:
    n: int = len(junction_boxes)

    distances: List[Tuple[float, int, int]] = []

    for i, jb1 in enumerate(junction_boxes):
        for j in range(i + 1, len(junction_boxes)):
            jb2: JunctionBoxes = junction_boxes[j]
            distance: float = jb1.distance(jb2)
            distances.append((distance, i, j))

    sorted_distances: List[Tuple[float, int, int]] = sorted(distances)

    union_find: UnionFind = UnionFind(n)
    for index in range(connections):
        _, i, j = sorted_distances[index]
        union_find.union(i, j)

    circuit_sizes: Dict[int, int] = {}
    for i in range(n):
        i_root: int = union_find.find(i)
        circuit_sizes[i_root] = circuit_sizes.get(i_root, 0) + 1

    values: List[int] = sorted(list(set(circuit_sizes.values())), reverse=True)
    return values[0] * values[1] * values[2]


def solution(filename: str, connections: int) -> int:
    junction_boxes: List[JunctionBoxes] = parse(filename)
    return solve(junction_boxes, connections)


if __name__ == "__main__":
    # print(solution("./example.txt", 10))  # 40
    # print(solution("./input.txt", 1_000))  # 68112

    assert solution("./example.txt", 10) == 40
    assert solution("./input.txt", 1_000) == 68112
