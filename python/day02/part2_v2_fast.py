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
    sum_of_invalid_ids: int = 0

    for id_range in ranges:
        for product_id in range(id_range.start_id, id_range.end_id + 1):
            str_id: str = str(product_id)
            n: int = len(str_id)

            for pattern_len in range(1, n // 2 + 1):
                if n % pattern_len != 0:
                    continue

                for i in range(pattern_len):
                    for j in range(1, n // pattern_len):
                        if str_id[i] != str_id[i + j * pattern_len]:
                            break
                    else:
                        continue
                    break

                else:
                    sum_of_invalid_ids += product_id
                    break

    return sum_of_invalid_ids


def solution(filename: str) -> int:
    ranges: List[Range] = parse(filename)
    return solve(ranges)


if __name__ == "__main__":
    r = solution("./example.txt")
    assert r == 4174379265
    r = solution("./input.txt")
    assert r == 48631958998
