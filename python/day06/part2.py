import re
from collections import deque, defaultdict, namedtuple
from dataclasses import dataclass
from typing import Deque, Dict, List, Match, Optional, Set, Tuple

LAST: int = -1

def parse(filename: str) -> List[str]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().strip("\n")

    all_rows = data.split("\n")
    number_rows = all_rows[:LAST]
    operations_row = all_rows[LAST]

    numbers = []
    for n in number_rows:
        numbers.append(n.replace("\n", " "))

    operations = []
    index = 0
    while index < len(operations_row):
        operation = operations_row[index]
        start_index = index

        index += 1
        while index < len(operations_row) and operations_row[index] == " ":
            index += 1
        if index >= len(operations_row):
            index = index + 1
        operations.append((operation, start_index, index - 1))

    # print(numbers)
    # for op in operations:
    #     print(op)

    return numbers, operations


def solve(numbers, operations) -> int:
    grand_total: int = 0

    for op, start, end in operations:
        result: int = 1 if op == "*" else 0

        for col in range(start, end):
            number = []
            for row in range(len(numbers)):
                number.append(numbers[row][col])

            if op == "*":
                result *= int("".join(number))
            else:
                result += int("".join(number))

        grand_total += result


    return grand_total


def solution(filename: str) -> int:
    numbers, operations = parse(filename)
    return solve(numbers, operations)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 3263827
    print(solution("./input.txt"))  # 11479269003550
