package main

import (
	"fmt"
	"os"
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
	queue := NewQueue[string]()
	queue.append("you")

	for !queue.is_empty() {
		node := queue.popleft()

		if node == "out" {
			total_paths++
			continue
		}

		for _, device := range graph[node] {
			queue.append(device)
		}
	}

	return total_paths
}

func solution(filename string) int {
	graph := parse(filename)
	return solve(graph)
}

func main() {
	fmt.Println(solution("./example1.txt")) // 5
	fmt.Println(solution("./input.txt"))    // 668
}
