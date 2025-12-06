import re
from collections import deque, defaultdict, namedtuple
from dataclasses import dataclass
from typing import Deque, Dict, List, Match, Optional, Set, Tuple


def parse(filename: str) -> List[str]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    numbers = []
    for line in data[:-1]:
        line_numbers = line.split()
        numbers.append([int(n) for n in line_numbers])

    operations = data[-1].split()

    return numbers, operations


def solve(numbers, operations) -> int:
    grand_total: int = 0

    for index, op in enumerate(operations):
        if op == "*":
            result = 1
        else:
            result = 0

        for row in numbers:
            if op == "*":
                result *= row[index]
            else:
                result += row[index]

        grand_total += result


    return grand_total


def solution(filename: str) -> int:
    numbers, operations = parse(filename)
    return solve(numbers, operations)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 0
    print(solution("./input.txt"))  # 0
