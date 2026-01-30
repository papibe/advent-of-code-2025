package main

import (
	"fmt"
	"os"
	"strings"
)

const PAPER_ROLL = '@'

func parse(filename string) []string {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}

	return strings.Split(strings.Trim(string(data), "\n"), "\n")
}

func solve(grid []string) int {
	total_rolls := 0

	for row, line := range grid {
		for col, cell := range line {
			if cell != PAPER_ROLL {
				continue
			}
			adjacent_rolls := 0

			for _, n_coords := range [][2]int{
				{row - 1, col - 1},
				{row - 1, col},
				{row - 1, col + 1},
				{row, col - 1},
				{row, col + 1},
				{row + 1, col - 1},
				{row + 1, col},
				{row + 1, col + 1},
			} {
				n_row, n_col := n_coords[0], n_coords[1]

				if 0 <= n_row && n_row < len(grid) && 0 <= n_col && n_col < len(grid[0]) {
					if grid[n_row][n_col] == PAPER_ROLL {
						adjacent_rolls += 1
					}
				}
			}
			if adjacent_rolls < 4 {
				total_rolls++
			}
		}
	}
	return total_rolls
}

func solution(filename string) int {
	grid := parse(filename)
	return solve(grid)
}

func main() {
	fmt.Println(solution("./example.txt")) // 13
	fmt.Println(solution("./input.txt"))   // 1480
}
