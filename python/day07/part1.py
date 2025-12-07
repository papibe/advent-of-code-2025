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


def solve(start_row, start_col, grid) -> int:
    total_sum: int = 0

    positions = set([(start_row, start_col)])
    while positions:
        new_positions = set()
        for row, col in positions:
            new_row = row + 1
            new_col = col
            print(new_row, new_col)
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                if grid[new_row][new_col] == "^":
                    print("split")
                    if 0 <= new_col - 1 < len(grid[0]):
                        new_positions.add((new_row, new_col - 1))
                    if 0 <= new_col + 1 < len(grid[0]):
                        new_positions.add((new_row, new_col + 1))

                    total_sum += 1
                else:
                    new_positions.add((new_row, new_col))

        positions = new_positions

    return total_sum


def solution(filename: str) -> int:
    start_row, start_col, grid = parse(filename)
    return solve(start_row, start_col, grid)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 0
    print(solution("./input.txt"))  # 0
