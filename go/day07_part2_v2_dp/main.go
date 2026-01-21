package main

import (
	"fmt"
	"os"
	"strings"
)

const START = 'S'
const DIVIDER = '^'
const SPACE = '.'

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

	// DP table
	dp := make([][]int, rows)
	for row := range rows {
		dp[row] = make([]int, cols)
	}
	dp[start_row][start_col] = 1

	for row := 1; row < rows; row++ {
		for col := range cols {
			if grid[row][col] == SPACE {
				dp[row][col] += dp[row-1][col]
			} else {
				dp[row][col-1] += dp[row-1][col]
				dp[row][col+1] += dp[row-1][col]

			}
		}
	}
	total := 0
	for col := range cols {
		total += dp[rows-1][col]
	}
	return total

}

func solution(filename string) int {
	start_row, start_col, grid := parse(filename)
	return solve(start_row, start_col, grid)
}

func main() {
	fmt.Println(solution("./example.txt")) // 40
	fmt.Println(solution("./input.txt"))   // 25592971184998
}
