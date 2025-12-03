from collections import namedtuple
from typing import List

Range = namedtuple("Range", ["start_id", "end_id"])


def parse(filename: str) -> List[Range]:
    with open(filename, "r") as fp:
        data: str = fp.read()

    ranges: List[Range] = []
    for id_range in data.split(","):
        ids = id_range.split("-")
        start_id: int = int(ids[0])
        end_id: int = int(ids[1])

        ranges.append(Range(start_id, end_id))

    return ranges


def solve(ranges: List[Range]) -> int:
    total_sum: int = 0

    for id_range in ranges:
        for product_id in range(id_range.start_id, id_range.end_id + 1):
            str_id: str = str(product_id)

            if len(str_id) % 2 == 0:
                half: str = str_id[: len(str_id) // 2]
                if str_id == half + half:
                    total_sum += product_id

    return total_sum


def solution(filename: str) -> int:
    ranges: List[Range] = parse(filename)
    return solve(ranges)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 1227775554
    print(solution("./input.txt"))  # 29940924880
