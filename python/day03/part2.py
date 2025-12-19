from typing import List


def parse(filename: str) -> List[List[int]]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    banks: List[List[int]] = []
    for line in data:
        battery = []
        for char in line:
            battery.append(int(char))
        banks.append(battery)

    return banks


def solve(banks: List[List[int]]) -> int:
    total_sum: int = 0
    bank: List[int]

    for bank in banks:
        selection: List[int] = []

        number: int
        for digit in range(11, -1, -1):
            if digit > 0:
                number = max(bank[:-digit])
            else:
                number = max(bank)

            for position, battery in enumerate(bank):
                if battery == number:
                    break

            bank = bank[position + 1 :]
            selection.append(number)

        total_sum += int("".join([str(d) for d in selection]))

    return total_sum


def solution(filename: str) -> int:
    banks: List[List[int]] = parse(filename)
    return solve(banks)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 3121910778619
    print(solution("./input.txt"))  # 172119830406258
