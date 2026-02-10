package main

import (
	"fmt"
	"os"
	"strings"
)

const START = 'S'
const DIVIDER = '^'

type Coords struct {
	row int
	col int
}

func parse(filename string) (int, int, []string) {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}

	grid := strings.Split(strings.Trim(string(data), "\n"), "\n")

	for row, line := range grid {
		for col, cell := range line {
			if cell == START {
				return row, col, grid
			}
		}
	}
	return 0, 0, []string{}
}

func solve(start_row, start_col int, grid []string) int {
	rows := len(grid)
	cols := len(grid[0])

	// BFS init
	start := Coords{start_row, start_col}

	queue := NewQueue[Coords]()
	queue.append(start)

	seen := NewSet[Coords]()
	seen.add(start)

	total_splits := 0

	// BFS
	for !queue.is_empty() {
		coord := queue.popleft()

		new_row := coord.row + 1
		new_col := coord.col

		if !(0 <= new_row && new_row < rows && 0 <= new_col && new_col < cols) {
			continue
		}
		if grid[new_row][new_col] == DIVIDER {
			total_splits++
			for _, next_col := range []int{new_col - 1, new_col + 1} {
				new_coord := Coords{new_row, next_col}
				if !seen.contains(new_coord) {
					queue.append(new_coord)
					seen.add(new_coord)
				}
			}
		} else {
			new_coord := Coords{new_row, new_col}
			if !seen.contains(new_coord) {
				queue.append(new_coord)
				seen.add(new_coord)
			}
		}
	}

	return total_splits
}

func solution(filename string) int {
	start_row, start_col, grid := parse(filename)
	return solve(start_row, start_col, grid)
}

func main() {
	fmt.Println(solution("./example.txt")) // 21
	fmt.Println(solution("./input.txt"))   // 1560
}
