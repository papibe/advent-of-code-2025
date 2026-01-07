from math import sqrt
from typing import List, Set, Tuple


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
        root: int = self.parent[i]

        if self.parent[root] != root:
            self.parent[i] = self.find(root)
            return self.parent[i]

        return root

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


def solve(junction_boxes: List[JunctionBoxes]) -> int:
    n: int = len(junction_boxes)

    distances: List[Tuple[float, int, int]] = []

    for i, jb1 in enumerate(junction_boxes):
        for j in range(i + 1, len(junction_boxes)):
            jb2: JunctionBoxes = junction_boxes[j]
            distance: float = jb1.distance(jb2)
            distances.append((distance, i, j))

    sorted_distances: List[Tuple[float, int, int]] = sorted(distances)

    union_find: UnionFind = UnionFind(n)
    for _, i, j in sorted_distances:
        union_find.union(i, j)

        circuit_sizes: Set[int] = set()
        for k in range(n):
            circuit_sizes.add(union_find.find(k))
            if len(circuit_sizes) > 1:
                break

        if len(circuit_sizes) == 1:
            return junction_boxes[i].x * junction_boxes[j].x

    return -1


def solution(filename: str) -> int:
    junction_boxes: List[JunctionBoxes] = parse(filename)
    return solve(junction_boxes)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 25272
    print(solution("./input.txt"))  # 44543856
