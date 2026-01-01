from typing import Dict, List, Tuple

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


memo: Dict[Tuple[int, int], int] = {}


def solve(row: int, col: int, grid: List[str]) -> int:
    if row == len(grid) - 1:
        return 1

    if (row, col) in memo:
        return memo[(row, col)]

    result: int
    if grid[row][col] == SPACE:
        result = solve(row + 1, col, grid)
    else:
        result = solve(row + 1, col - 1, grid) + solve(row + 1, col + 1, grid)

    memo[(row, col)] = result
    return result


def solution(filename: str) -> int:
    start_row, start_col, grid = parse(filename)
    return solve(start_row, start_col, grid)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 40
    print(solution("./input.txt"))  # 25592971184998
