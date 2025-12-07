import re
from collections import deque, defaultdict, namedtuple
from dataclasses import dataclass
from typing import Deque, Dict, List, Match, Optional, Set, Tuple


def parse(filename: str) -> List[str]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    start_row = start_col = 0
    grid = []
    for row, line in enumerate(data):
        for col, cell in enumerate(line):
            if cell == "S":
                start_row = row
                start_col = col

        grid.append([c for c in line])

    return start_row, start_col, grid


def solve(row, col, grid) -> int:
    # BFS init
    queue = deque([(row, col)])
    counter = 0
    memo = {}
    memo[(row, col)] = 1


    while queue:
        row, col = queue.popleft()
        paths = memo[(row, col)]

        if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
            counter += memo[(row, col)]
            continue

        new_row = row + 1
        new_col = col

        if not (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0])):
            counter += memo[(row, col)]
            continue

        if grid[new_row][new_col] == ".":
            if (new_row, new_col) in memo:
                memo[(new_row, new_col)] += paths
            else:
                memo[(new_row, new_col)] = paths
                queue.append((new_row, new_col))
            continue

        for next_col in [new_col + 1, new_col - 1]:
            if (new_row, next_col) in memo:
                memo[(new_row, next_col)] += paths
            else:
                memo[(new_row, next_col)] = paths

                queue.append((new_row, next_col))

    return counter



def solution(filename: str) -> int:
    start_row, start_col, grid = parse(filename)
    return solve(start_row, start_col, grid)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 0
    print(solution("./input.txt"))  # 0
    # 25592971185038 to high
