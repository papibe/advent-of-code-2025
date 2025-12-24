from typing import List, Tuple

type IngredientRanges = List[Tuple[int, int]]
type AvailableIngredients = List[int]


def parse(filename: str) -> Tuple[IngredientRanges, AvailableIngredients]:
    with open(filename, "r") as fp:
        data: str = fp.read()

    blocks: List[str] = data.split("\n\n")
    available_ingredients = [int(i) for i in blocks[1].splitlines()]

    ingredient_ranges: List[Tuple[int, int]] = []

    for line in blocks[0].splitlines():
        split_line: List[str] = line.split("-")
        start = int(split_line[0])
        end = int(split_line[1])

        ingredient_ranges.append((start, end))

    return ingredient_ranges, available_ingredients


def solve(ranges: IngredientRanges, ingredients: AvailableIngredients) -> int:
    available_fresh_ingredients: int = 0

    for ingredient in ingredients:
        for start, end in ranges:
            if start <= int(ingredient) <= end:
                break
        else:
            continue

        available_fresh_ingredients += 1

    return available_fresh_ingredients


def solution(filename: str) -> int:
    ranges, ingredients = parse(filename)
    return solve(ranges, ingredients)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 3
    print(solution("./input.txt"))  # 733
