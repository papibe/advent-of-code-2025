package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func parse(filename string) map[string][]string {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}
	lines := strings.Split(strings.Trim(string(data), "\n"), "\n")
	graph := make(map[string][]string)

	for _, line := range lines {
		line_split := strings.Split(line, ":")
		node := line_split[0]
		nodes := strings.Split(strings.Trim(line_split[1], " "), " ")
		graph[node] = nodes
	}

	return graph
}

func solve(graph map[string][]string) int {
	total_paths := 0
	memo := make(map[string]int)

	var dfs func(node string, has_pass_by_dac, has_pass_by_fft bool) int

	dfs = func(node string, has_pass_by_dac, has_pass_by_fft bool) int {
		if node == "out" {
			if has_pass_by_dac && has_pass_by_fft {
				total_paths++
				return 1
			} else {
				return 0
			}
		}
		key := node + strconv.FormatBool(has_pass_by_dac) + strconv.FormatBool(has_pass_by_fft)
		cached_value, in_memo := memo[key]
		if in_memo {
			return cached_value
		}

		result := 0
		for _, device := range graph[node] {
			new_has_pass_by_dac := has_pass_by_dac || device == "dac"
			new_has_pass_by_fft := has_pass_by_fft || device == "fft"

			result += dfs(device, new_has_pass_by_dac, new_has_pass_by_fft)
		}
		memo[key] = result
		return result
	}

	return dfs("svr", false, false)
}

func solution(filename string) int {
	graph := parse(filename)
	return solve(graph)
}

func main() {
	fmt.Println(solution("./example2.txt")) // 2
	fmt.Println(solution("./input.txt"))    // 294310962265680
}
