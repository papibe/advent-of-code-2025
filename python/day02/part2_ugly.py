import re
from collections import deque, defaultdict, namedtuple
from dataclasses import dataclass
from typing import Deque, Dict, List, Match, Optional, Set, Tuple


def parse(filename: str) -> List[str]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read()

    ranges = []
    for id_range in data.split(","):
        ids = id_range.split("-")
        first_id: int = int(ids[0])
        second_id: int = int(ids[1])

        ranges.append((first_id, second_id))

    return ranges


def solve(ranges: List[str]) -> int:
    total_sum: int = 0

    # bad_ones = set()

    for id_range in ranges:
        for product_id in range(id_range[0], id_range[1] + 1):
            str_id: str = str(product_id)

            if len(set(str_id)) == 1 and len(str_id) > 1:
                # print(product_id)
                total_sum += product_id
                # if product_id in bad_ones:
                #     print("============ repeated")
                # bad_ones.add(product_id)
                continue

            # if product_id == 1010:
            #     print(f"{len(str_id) // 2 = }")

            for l in range(2, len(str_id) // 2 + 1):
                # if product_id == 1010:
                #     print(f"{len(str_id) % l = }")
                if len(str_id) % l != 0:
                    continue

                for i in range(l):
                    good = True
                    for j in range(1, len(str_id) // l):
                        # if product_id == 1010:
                        #     print(f"{l = } {i = } {j = } {len(str_id) // l = }")
                        #     print(i, i + j*l, str_id[i], str_id[i + j*l])
                        if str_id[i] != str_id[i + j*l]:
                            good = False
                            # if product_id == 1010:
                            #     print("bad")
                            break

                    if not good:
                        break

                if good == True:
                    # print(product_id, l)
                    total_sum += product_id
                    # if product_id in bad_ones:
                    #     print("============ repeated")
                    # bad_ones.add(product_id)
                    break


    return total_sum


def solution(filename: str) -> int:
    ranges: List[str] = parse(filename)
    return solve(ranges)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 4174379265
    print(solution("./input.txt"))  # 48631958998
