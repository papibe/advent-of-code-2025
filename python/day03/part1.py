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

    for bank in banks:

        first_battery: int = max(bank[:-1])
        for position, battery in enumerate(bank):
            if battery == first_battery:
                break
        second_battery: int = max(bank[position + 1 :])

        total_sum += first_battery * 10 + second_battery

    return total_sum


def solution(filename: str) -> int:
    banks: List[List[int]] = parse(filename)
    return solve(banks)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 357
    print(solution("./input.txt"))  # 17376
