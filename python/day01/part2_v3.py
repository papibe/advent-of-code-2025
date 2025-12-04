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
    zeros2: int = 0
    for direction, amount in rotations:
        original_pointer  = dial_pointer
        if direction == "R":
            step = 1
        else:
            step = -1

        clicks = 0
        for _ in range(amount):
            dial_pointer = (dial_pointer + step) % 100
            if dial_pointer == 0:
                clicks += 1
        zeros += clicks

        increase = 0
        raw_dial_pointer = original_pointer + step * amount
        dial_pointer2 = (original_pointer + step * amount) % 100
        if  (raw_dial_pointer < 0 or raw_dial_pointer > 99):
            rotation = amount // 100
            if rotation == 0:
                rotation = 1
            increase = rotation


        elif dial_pointer2 == 0:
            increase += 1

        zeros2 += increase

        if clicks != increase:
            print(f"{original_pointer = } dir = {step * amount} {clicks = } {increase = }")
            print(f"{original_pointer + step * amount = }")
            print(f"{dial_pointer2 = }")
            print()


    print(f"{zeros2 = }")
    return zeros


def solution(filename: str) -> int:
    data: List[str] = parse(filename)
    return solve(data)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 6
    print(solution("./input.txt"))  # 6907
