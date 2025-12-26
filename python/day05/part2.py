from typing import List, Tuple

type IngredientRanges = List[Tuple[int, int]]
type AvailableIngredients = List[int]

LAST: int = -1


def parse(filename: str) -> IngredientRanges:
    with open(filename, "r") as fp:
        data: str = fp.read()

    blocks: List[str] = data.split("\n\n")
    ingredient_ranges: List[Tuple[int, int]] = []

    for line in blocks[0].splitlines():
        split_line: List[str] = line.split("-")
        start = int(split_line[0])
        end = int(split_line[1])

        ingredient_ranges.append((start, end))

    return ingredient_ranges


def solve(ranges: IngredientRanges) -> int:
    ranges.sort()
    new_ranges: IngredientRanges = [ranges[0]]

    for start, end in ranges[1:]:
        last_start: int = new_ranges[LAST][0]
        last_end: int = new_ranges[LAST][1]

        if start > last_end:
            new_ranges.append((start, end))
        else:
            new_ranges.pop()
            new_ranges.append((last_start, max(last_end, end)))

    total_fresh_ingredients: int = 0
    for start, end in new_ranges:
        total_fresh_ingredients += end - start + 1

    return total_fresh_ingredients


def solution(filename: str) -> int:
    ranges = parse(filename)
    return solve(ranges)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 14
    print(solution("./input.txt"))  # 345821388687084
