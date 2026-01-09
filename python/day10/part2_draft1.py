from itertools import combinations
from typing import List, Tuple
from copy import deepcopy


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

        self.joltage: List[int] = eval("[" + joltage[1:-1] + "]")

    def set_lights_goal(self) -> None:
        goal: int = 0
        for i, jol in enumerate(self.joltage):
            if jol % 2 == 1:
                goal |= 1 << i
        self.goal = goal

    def update_joltage(self, vector: List[int]) -> None:
        for i in range(len(self.joltage)):
            self.joltage[i] -= vector[i]

    def half_joltage(self) -> None:
        for i in range(len(self.joltage)):
            self.joltage[i] //= 2

    def is_overloaded(self) -> bool:
        for joltage in self.joltage:
            if joltage < 0:
                # print(f"{joltage = }")
                return True
        return False

    def is_jolted_balanced(self) -> bool:
        for joltage in self.joltage:
            if joltage != 0:
                return False
        return True

    def reset_lights(self) -> None:
        self.lights = 0

    def is_on(self) -> bool:
        return self.lights == self.goal

    def press(self, button_value: int) -> None:
        self.lights ^= button_value

    def __hash__(self):
        return hash(tuple(self.joltage))

    def __repr__(self):
        return str(self.joltage)


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

def get_diff_vector(combo: List[Tuple[int, ...]], size: int) -> List[int]:
    vector = [0] * size
    for n in combo:
        for i in range(size):
            if n & (1 << i) != 0:
                vector[i] += 1

    return vector

def get_min_parity(machine: Machine, combos) -> int:

    presses = []
    for combo in combos:
        machine.reset_lights()
        for button_value in combo:
            machine.press(button_value)

        if machine.is_on():
            presses.append((len(combo), get_diff_vector(combo, len(machine.joltage))))
    return presses

def get_all_button_combos(buttons):
    combos = []
    for size in range(len(buttons) + 1):
        for combo in combinations(buttons, size):
            combos.append(combo)
    return combos

def get_min_presses(machine: Machine) -> int:
    buttons_combos = get_all_button_combos(machine.buttons)

    memo = {}
    def _get_min_presses(machine: Machine) -> int:

        if machine.is_jolted_balanced():
            return 0

        if machine.is_overloaded():
            return float("inf")

        key = tuple(machine.joltage)
        if key in memo:
            return memo[key]

        machine.set_lights_goal()
        presses = get_min_parity(machine, buttons_combos)


        results = [float("inf")]
        for press, vector in presses:
            new_machine = deepcopy(machine)

            new_machine.update_joltage(vector)
            if new_machine.is_overloaded():
                continue

            new_machine.half_joltage()
            results.append(2 * _get_min_presses(new_machine) + press)

        memo[key] = min(results)

        return memo[key]

    return _get_min_presses(machine)


def solve(machines: List[Machine]) -> int:
    sum_of_presses: int = 0

    for index, machine in enumerate(machines):
        r = get_min_presses(machine)
        sum_of_presses += r

    return sum_of_presses


def solution(filename: str) -> int:
    machines: List[Machine] = parse(filename)
    return solve(machines)


if __name__ == "__main__":
    # it takes 11secs
    print(solution("./example.txt"))  # 33
    print(solution("./input.txt"))  # 20617
