from typing import List

PAPER_ROLL: str = "@"


def parse(filename: str) -> List[str]:
    with open(filename, "r") as fp:
        grid: List[str] = fp.read().splitlines()

    return grid


def solve(grid: List[str]) -> int:
    total_rolls: int = 0

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

    return total_rolls


def solution(filename: str) -> int:
    grid: List[str] = parse(filename)
    return solve(grid)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 13
    print(solution("./input.txt"))  # 1480
