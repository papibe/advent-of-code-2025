from collections import deque
from typing import Deque, List, Set, Tuple

START: str = "S"
DIVIDER: str = "^"
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
    seen: Set[Tuple[int, int]] = set([(start_row, start_col)])
    total_splits: int = 0

    # BFS
    while queue:
        row: int
        col: int
        row, col = queue.popleft()

        new_row: int = row + 1
        new_col: int = col

        if not (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0])):
            continue

        if grid[new_row][new_col] == DIVIDER:
            total_splits += 1
            for next_col in [new_col - 1, new_col + 1]:
                if (new_row, next_col) not in seen:
                    queue.append((new_row, next_col))
                    seen.add((new_row, next_col))
        else:
            if (new_row, new_col) not in seen:
                queue.append((new_row, new_col))
                seen.add((new_row, new_col))

    return total_splits


def solution(filename: str) -> int:
    start_row, start_col, grid = parse(filename)
    return solve(start_row, start_col, grid)


if __name__ == "__main__":
    r = solution("./example.txt")
    print(r)
    assert r == 21
    r = solution("./input.txt")
    print(r)

    assert r == 1560
