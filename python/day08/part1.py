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


def solve(junction_boxes: List[str], connections: int) -> int:
    total_sum: int = 0
    n: int = len(junction_boxes)

    # dm = [[float("inf")] * n for _ in range(n)]

    distances = []

    for i, jb1 in enumerate(junction_boxes):
        for j in range(i+1, len(junction_boxes)):
            jb2 = junction_boxes[j]
            distance = jb1.distance(jb2)
            # distance2 = jb2.distance(jb1)
            # assert distance == distance2, print(jb1, jb2, distance, distance2)
            # dm[i][j] = distance
            # dm[j][i] = distance
            distances.append((distance, i, j))


    distances.sort()

    # for r in dm:
    #     print(r)
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


    for index in range(connections):
        min_distance, i_min, j_min = distances[index]

        # print(min_distance, i_min, j_min, junction_boxes[i_min], junction_boxes[j_min])
        # dm[i_min][j_min] = float("inf")
        # dm[j_min][i_min] = float("inf")

        union(i_min, j_min)


        # dsets = {}
        # for i in range(n):
        #     rep = find(i)
        #     dsets[rep] = dsets.get(rep, 0) + 1

        # print(parent)
        # print(dsets)
        # print(sorted(dsets.values(), reverse=True))
        # print()

    dsets = {}
    for i in range(n):
        rep = find(i)
        dsets[rep] = dsets.get(rep, 0) + 1

    # print(parent)
    # print(dsets)
    # print(sorted(dsets.values(), reverse=True))
    # print()

    values = sorted(dsets.values(), reverse=True)
    big_3 = set()
    index = 0
    while len(big_3) < 3:
        big_3.add(values[index])
        index += 1

    # print(big_3)

    product = 1
    for _ in range(3):
        product *= big_3.pop()

    return product


def solution(filename: str, connections: int) -> int:
    junction_boxes: List[str] = parse(filename)
    return solve(junction_boxes, connections)


if __name__ == "__main__":
    print(solution("./example.txt", 10))  # 40
    print(solution("./input.txt", 1_000))  # 68112
