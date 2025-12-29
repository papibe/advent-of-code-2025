from typing import List, Tuple

LAST: int = -1


def parse(filename: str) -> Tuple[List[str], List[Tuple[str, int, int]]]:
    with open(filename, "r") as fp:
        data: str = fp.read().strip("\n")

    all_rows: List[str] = data.split("\n")
    numbers: List[str] = all_rows[:LAST]
    operations_row = all_rows[LAST]

    operations: List[Tuple[str, int, int]] = []
    index: int = 0
    while index < len(operations_row):
        operation = operations_row[index]
        start_index: int = index

        index += 1
        while index < len(operations_row) and operations_row[index] == " ":
            index += 1
        if index >= len(operations_row):
            index = index + 1
        operations.append((operation, start_index, index - 1))

    return numbers, operations


def solve(numbers: List[str], operations: List[Tuple[str, int, int]]) -> int:
    grand_total: int = 0

    for operation, start, end in operations:
        result: int = 1 if operation == "*" else 0

        for col in range(start, end):
            digits: List[str] = []
            for row in range(len(numbers)):
                digits.append(numbers[row][col])

            number: int = int("".join(digits))

            if operation == "*":
                result *= number
            else:
                result += number

        grand_total += result

    return grand_total


def solution(filename: str) -> int:
    numbers, operations = parse(filename)
    return solve(numbers, operations)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 3263827
    print(solution("./input.txt"))  # 11479269003550
