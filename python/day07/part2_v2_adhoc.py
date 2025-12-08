from collections import deque
from typing import Deque, Dict, List, Tuple

START: str = "S"
SPACE: str = "."
LAST: int = -1


def parse(filename: str) -> Tuple[int, int, List[str]]:
    with open(filename, "r") as fp:
        grid: List[str] = fp.read().splitlines()

    for row, line in enumerate(grid):
        for col, cell in enumerate(line):
            if cell == START:
                start_row: int = row
                start_col: int = col
                break

    return start_row, start_col, grid


def solve(start_row: int, start_col: int, grid: List[str]) -> int:
    # BFS init
    queue: Deque[Tuple[int, int]] = deque([(start_row, start_col)])
    total_paths: int = 0
    paths: Dict[Tuple[int, int], int] = {}
    paths[(start_row, start_col)] = 1

    while queue:
        row: int
        col: int
        row, col = queue.popleft()
        number_of_paths: int = paths[(row, col)]

        if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
            total_paths += paths[(row, col)]
            continue

        new_row: int = row + 1
        new_col: int = col

        if not (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0])):
            total_paths += paths[(row, col)]
            continue

        if grid[new_row][new_col] == SPACE:
            if (new_row, new_col) in paths:
                paths[(new_row, new_col)] += number_of_paths
            else:
                paths[(new_row, new_col)] = number_of_paths
                queue.append((new_row, new_col))
            continue

        for next_col in [new_col + 1, new_col - 1]:
            if (new_row, next_col) in paths:
                paths[(new_row, next_col)] += number_of_paths
            else:
                paths[(new_row, next_col)] = number_of_paths

                queue.append((new_row, next_col))

    return total_paths


def solution(filename: str) -> int:
    start_row, start_col, grid = parse(filename)
    return solve(start_row, start_col, grid)


if __name__ == "__main__":
    assert solution("./example.txt") == 40
    assert solution("./input.txt") == 25592971184998
