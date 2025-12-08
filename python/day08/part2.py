import re
from collections import deque, defaultdict, namedtuple
from dataclasses import dataclass
from typing import Deque, Dict, List, Match, Optional, Set, Tuple
from math import sqrt

class JunctionBoxes:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance(self, jb: "JunctionBoxes") -> float:
        return sqrt(
            (self.x - jb.x) ** 2 + (self.y - jb.y) ** 2 + (self.z - jb.z) ** 2
        )

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"

def parse(filename: str) -> List[str]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    junction_boxes = []
    for line in data:
        numbers = line.split(",")
        x = int(numbers[0])
        y = int(numbers[1])
        z = int(numbers[2])
        junction_boxes.append(JunctionBoxes(x, y, z))

    # for j in junction_boxes:
    #     print(j)

    return junction_boxes


def solve(junction_boxes: List[str]) -> int:
    total_sum: int = 0
    n: int = len(junction_boxes)

    distances = []


    for i, jb1 in enumerate(junction_boxes):
        for j in range(i+1, len(junction_boxes)):
            jb2 = junction_boxes[j]
            distance = jb1.distance(jb2)
            distances.append((distance, i, j))

    # for r in dm:
    #     print(r)
    distances.sort()

    parent = list(range(n))

    def find(i):
        # If i itself is root or representative
        if parent[i] == i:
            return i

        # Else recursively find the representative
        # of the parent
        return find(parent[i])


    def union(i, j):

        # Representative of set containing i
        irep = find(i)

        # Representative of set containing j
        jrep = find(j)

        # Make the representative of i's set
        # be the representative of j's set
        parent[irep] = jrep


    for index in range(len(distances)):
        min_distance, i_min, j_min = distances[index]

        union(i_min, j_min)

        dsets = {}
        for i in range(n):
            rep = find(i)
            dsets[rep] = dsets.get(rep, 0) + 1

        if len(dsets) == 1:
            one_circuit = True
            # print(min_distance, i_min, j_min, junction_boxes[i_min], junction_boxes[j_min])
            return junction_boxes[i_min].x * junction_boxes[j_min].x


def solution(filename: str) -> int:
    junction_boxes: List[str] = parse(filename)
    return solve(junction_boxes)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 25272
    print(solution("./input.txt"))  # 44543856
