package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func parse(filename string) ([][]int, []string) {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}

	numbers := [][]int{}
	lines := strings.Split(strings.Trim(string(data), "\n"), "\n")
	re_space := regexp.MustCompile(`\s+`)
	for _, line := range lines[:len(lines)-1] {
		row := []int{}
		clean_line := re_space.Split(strings.Trim(line, " "), -1)
		for _, str_number := range clean_line {
			number, _ := strconv.Atoi(str_number)
			row = append(row, number)
		}
		numbers = append(numbers, row)
	}

	operations := re_space.Split(strings.Trim(lines[len(lines)-1], " "), -1)

	return numbers, operations
}

func solve(numbers [][]int, operations []string) int {
	grand_total := 0

	for index, operation := range operations {
		var result int

		if operation == "*" {
			result = 1
			for _, row := range numbers {
				result *= row[index]
			}

		} else {
			result = 0
			for _, row := range numbers {
				result += row[index]
			}
		}
		grand_total += result
	}

	return grand_total
}

func solution(filename string) int {
	numbers, operations := parse(filename)
	return solve(numbers, operations)
}

func main() {
	fmt.Println(solution("./example.txt")) // 4277556
	fmt.Println(solution("./input.txt"))   // 7229350537438
}
