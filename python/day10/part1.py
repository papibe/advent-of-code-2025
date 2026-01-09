from itertools import combinations
from typing import List

ON: str = "#"


class Machine:
    def __init__(self, lights: str, buttons: List[str], joltage: str) -> None:
        goal_value: int = 0
        for i, char in enumerate(lights[1:-1]):
            if char == ON:
                goal_value |= 1 << i

        self.goal: int = goal_value
        self.lights: int = 0

        buttons_values: List[int] = []
        for button in buttons:
            button_value: int = 0
            for char in button[1:-1].split(","):
                value: int = int(char)
                button_value |= 1 << value
            buttons_values.append(button_value)

        self.buttons: List[int] = buttons_values

    def reset_lights(self) -> None:
        self.lights = 0

    def is_on(self) -> bool:
        return self.lights == self.goal

    def press(self, button_value: int) -> None:
        self.lights ^= button_value


def parse(filename: str) -> List[Machine]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    machines: List[Machine] = []
    for line in data:
        split_line: List[str] = line.split()
        lights: str = split_line[0]
        buttons: List[str] = split_line[1:-1]
        joltage: str = split_line[-1]

        machines.append(Machine(lights, buttons, joltage))

    return machines


def get_min_presses(machine: Machine) -> int:
    for size in range(1, len(machine.buttons) + 1):
        for combo in combinations(machine.buttons, size):
            machine.reset_lights()
            for button_value in combo:
                machine.press(button_value)

            if machine.is_on():
                return size

    return -1


def solve(machines: List[Machine]) -> int:
    sum_of_presses: int = 0

    for machine in machines:
        sum_of_presses += get_min_presses(machine)

    return sum_of_presses


def solution(filename: str) -> int:
    machines: List[Machine] = parse(filename)
    return solve(machines)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 7
    print(solution("./input.txt"))  # 491
