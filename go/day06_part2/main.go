package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type CephNumber struct {
	operation rune
	start     int
	end       int
}

func parse(filename string) ([]string, []CephNumber) {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}

	data_str := strings.Trim(string(data), "\n")
	all_rows := strings.Split(data_str, "\n")
	numbers := all_rows[:len(all_rows)-1]
	operations_row := all_rows[len(all_rows)-1]

	operations := []CephNumber{}
	n := len(operations_row)
	index := 0
	for index < n {
		operation := rune(operations_row[index])
		start_index := index

		index++
		for index < n && operations_row[index] == ' ' {
			index++
		}
		if index >= n {
			index++
		}
		operations = append(operations, CephNumber{operation, start_index, index - 1})
	}

	return numbers, operations
}

func solve(numbers []string, operations []CephNumber) int {
	grand_total := 0

	for _, op := range operations {
		var result int
		if op.operation == '*' {
			result = 1
		} else {
			result = 0
		}

		for col := op.start; col < op.end; col++ {
			digits := []string{}
			for row := range len(numbers) {
				digits = append(digits, string(numbers[row][col]))
			}
			number, _ := strconv.Atoi(strings.Trim(strings.Join(digits, ""), " "))

			if op.operation == '*' {
				result *= number

			} else {
				result += number
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
	fmt.Println(solution("./example.txt")) // 3263827
	fmt.Println(solution("./input.txt"))   // 11479269003550
}
