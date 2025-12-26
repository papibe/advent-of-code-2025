from typing import List, Tuple


def parse(filename: str) -> Tuple[List[List[int]], List[str]]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    numbers: List[List[int]] = []
    for line in data[:-1]:
        line_numbers: List[str] = line.split()
        numbers.append([int(n) for n in line_numbers])

    operations: List[str] = data[-1].split()

    return numbers, operations


def solve(numbers: List[List[int]], operations: List[str]) -> int:
    grand_total: int = 0

    for index, operation in enumerate(operations):
        result: int = 1 if operation == "*" else 0

        for row in numbers:
            if operation == "*":
                result *= row[index]
            else:
                result += row[index]

        grand_total += result

    return grand_total


def solution(filename: str) -> int:
    numbers, operations = parse(filename)
    return solve(numbers, operations)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 4277556
    print(solution("./input.txt"))  # 7229350537438
