package main

import (
	"fmt"
	"os"
	"strings"
)

const PAPER_ROLL = '@'
const SPACE = '.'

func parse(filename string) [][]rune {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}

	grid := [][]rune{}
	lines := strings.Split(strings.Trim(string(data), "\n"), "\n")
	for _, line := range lines {
		row := []rune{}
		for _, char := range line {
			row = append(row, char)
		}
		grid = append(grid, row)
	}
	return grid
}

func solve(grid [][]rune) int {
	total_rolls := 0

	for {
		// copy grid
		next_grid := [][]rune{}
		for _, line_row := range grid {
			next_row := []rune{}
			for _, char := range line_row {
				next_row = append(next_row, char)
			}
			next_grid = append(next_grid, next_row)
		}
		changed_cycle := false

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
					next_grid[row][col] = SPACE
					changed_cycle = true
				}
			}
		}
		if !changed_cycle {
			return total_rolls
		}
		grid = next_grid
	}
}

func solution(filename string) int {
	grid := parse(filename)
	return solve(grid)
}

func main() {
	fmt.Println(solution("./example.txt")) // 43
	fmt.Println(solution("./input.txt"))   // 8899
}
