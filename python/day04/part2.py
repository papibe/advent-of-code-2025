from copy import deepcopy
from typing import List

PAPER_ROLL: str = "@"
SPACE: str = "."


def parse(filename: str) -> List[List[str]]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    grid: List[List[str]] = [list(line) for line in data]
    return grid


def solve(grid: List[List[str]]) -> int:
    total_rolls: int = 0

    while True:
        found = False
        next_data = deepcopy(grid)

        for row, line in enumerate(grid):
            for col, cell in enumerate(line):
                if cell != PAPER_ROLL:
                    continue

                adjacent_rolls: int = 0

                for n_row, n_col in [
                    (row - 1, col - 1),
                    (row - 1, col),
                    (row - 1, col + 1),
                    (row, col - 1),
                    (row, col + 1),
                    (row + 1, col - 1),
                    (row + 1, col),
                    (row + 1, col + 1),
                ]:
                    if (
                        0 <= n_row
                        and n_row < len(grid)
                        and 0 <= n_col
                        and n_col < len(grid[0])
                    ):
                        if grid[n_row][n_col] == PAPER_ROLL:
                            adjacent_rolls += 1

                if adjacent_rolls < 4:
                    total_rolls += 1
                    next_data[row][col] = SPACE
                    found = True

        if not found:
            break

        grid = next_data

    return total_rolls


def solution(filename: str) -> int:
    grid: List[List[str]] = parse(filename)
    return solve(grid)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 43
    print(solution("./input.txt"))  # 8899
