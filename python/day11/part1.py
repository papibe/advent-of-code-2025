from collections import deque
from typing import Deque, Dict, List


def parse(filename: str) -> Dict[str, List[str]]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    graph: Dict[str, List[str]] = {}
    for line in data:
        line_split: List[str] = line.split(":")
        node: str = line_split[0]
        nodes: List[str] = line_split[1].strip().split()
        graph[node] = nodes

    return graph


def solve(graph: Dict[str, List[str]]) -> int:
    total_paths: int = 0

    queue: Deque[str] = deque(["you"])

    while queue:
        node: str = queue.popleft()

        if node == "out":
            total_paths += 1
            continue

        for device in graph[node]:
            queue.append(device)

    return total_paths


def solution(filename: str) -> int:
    graph: Dict[str, List[str]] = parse(filename)
    return solve(graph)


if __name__ == "__main__":
    print(solution("./example1.txt"))  # 5
    print(solution("./input.txt"))  # 668
