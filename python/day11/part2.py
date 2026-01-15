from typing import Dict, List


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
    memo: Dict[str, int] = {}

    def dfs(node: str, has_pass_by_dac: bool, has_pass_by_fft: bool) -> int:
        nonlocal total_paths

        if node == "out":
            if has_pass_by_dac and has_pass_by_fft:
                total_paths += 1
                return 1
            else:
                return 0

        key: str = node + str(has_pass_by_dac) + str(has_pass_by_fft)
        if key in memo:
            return memo[key]

        result: int = 0
        for device in graph[node]:

            new_has_pass_by_dac: bool = has_pass_by_dac or device == "dac"
            new_has_pass_by_fft: bool = has_pass_by_fft or device == "fft"

            result += dfs(device, new_has_pass_by_dac, new_has_pass_by_fft)

        memo[key] = result
        return result

    return dfs("svr", False, False)


def solution(filename: str) -> int:
    graph: Dict[str, List[str]] = parse(filename)
    return solve(graph)


if __name__ == "__main__":
    print(solution("./example2.txt"))  # 2
    print(solution("./input.txt"))  # 294310962265680
