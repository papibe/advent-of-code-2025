from typing import List, Tuple


def parse(filename: str) -> List[Tuple[str, int]]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    rotations: List[Tuple[str, int]] = []
    for line in data:
        direction: str = line[0]
        amount: int = int(line[1:])
        rotations.append((direction, amount))

    return rotations


def solve(rotations: List[Tuple[str, int]]) -> int:
    dial_pointer: int = 50

    zeros: int = 0
    for direction, amount in rotations:
        if direction == "R":
            dial_pointer = (dial_pointer + amount) % 100
        else:
            dial_pointer = (dial_pointer - amount) % 100

        if dial_pointer == 0:
            zeros += 1

    return zeros


def solution(filename: str) -> int:
    rotations: List[Tuple[str, int]] = parse(filename)
    return solve(rotations)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 3
    print(solution("./input.txt"))  # 1182
