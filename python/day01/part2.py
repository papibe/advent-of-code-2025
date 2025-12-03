import re
from collections import deque, defaultdict, namedtuple
from dataclasses import dataclass
from typing import Deque, Dict, List, Match, Optional, Set, Tuple


def parse(filename: str) -> List[str]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    rotations = []
    for line in data:
        direction: str = line[0]
        amount: int = int(line[1:])
        rotations.append((direction, amount))

    return rotations


def solve(rotations: List[str]) -> int:
    dial_pointer: int = 50

    zeros: int = 0
    for direction, amount in rotations:
        if direction == "R":
            step = 1
        else:
            step = -1

        for _ in range(amount):
            dial_pointer = (dial_pointer + step) % 100
            if dial_pointer == 0:
                zeros += 1

    return zeros


def solution(filename: str) -> int:
    data: List[str] = parse(filename)
    return solve(data)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 6
    print(solution("./input.txt"))  # 6907
