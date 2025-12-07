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


memo = {}
timelines = [0]
max_times = [-1]
finals = {}

def solve(row, col, grid) -> int:
    if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
        finals[(row, col)] = memo[(row, col)]
        return

    memo[(row, col)] = memo.get((row, col), 0) + 1

    while 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] != "^":
        row += 1
        memo[(row, col)] = memo.get((row, col), 0) + 1


    for new_col in [col + 1, col - 1]:
        if not (0 <= row < len(grid) and 0 <= new_col < len(grid[0])):
            finals[(row, col)] = memo[(row, col)]
        else:
            solve(row, new_col, grid)


    return 0



def solution(filename: str) -> int:
    start_row, start_col, grid = parse(filename)
    r =  solve(start_row, start_col, grid)
    print(r, max_times, timelines)
    # for k, v in memo.items():
    #     print(k, v)
    print(finals)
    print(sum(finals.values()))

    return 0


if __name__ == "__main__":
    print(solution("./example.txt"))  # 0
    print(solution("./input.txt"))  # 0
