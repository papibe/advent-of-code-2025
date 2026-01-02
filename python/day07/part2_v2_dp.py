from typing import List, Tuple

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
    rows: int = len(grid)
    cols: int = len(grid[0])

    dp: List[List[int]] = [[0] * cols for _ in range(rows)]
    dp[start_row][start_col] = 1

    for row in range(1, rows):
        for col in range(cols):
            if grid[row][col] == SPACE:
                dp[row][col] += dp[row - 1][col]
            else:
                dp[row][col - 1] += dp[row - 1][col]
                dp[row][col + 1] += dp[row - 1][col]

    return sum(dp[LAST])


def solution(filename: str) -> int:
    start_row, start_col, grid = parse(filename)
    return solve(start_row, start_col, grid)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 40
    print(solution("./input.txt"))  # 25592971184998
