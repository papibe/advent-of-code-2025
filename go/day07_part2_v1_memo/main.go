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

var memo = map[Coords]int{}

func solve(row, col int, grid []string) int {
	if row == len(grid)-1 {
		return 1
	}

	key := Coords{row, col}
	value, seen_before := memo[key]
	if seen_before {
		return value
	}
	result := 0
	if grid[row][col] == SPACE {
		result = solve(row+1, col, grid)
	} else {
		result = solve(row+1, col-1, grid) + solve(row+1, col+1, grid)
	}
	memo[key] = result
	return result
}

func solution(filename string) int {
	start_row, start_col, grid := parse(filename)
	return solve(start_row, start_col, grid)
}

func main() {
	fmt.Println(solution("./example.txt")) // 40
	fmt.Println(solution("./input.txt"))   // 25592971184998
}
