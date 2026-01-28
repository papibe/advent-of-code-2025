package main

import (
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

func parse(filename string) [][]int {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}

	lines := strings.Split(strings.Trim(string(data), "\n"), "\n")
	banks := [][]int{}
	for _, line := range lines {
		battery := []int{}
		for _, char := range line {
			value, _ := strconv.Atoi(string(char))
			battery = append(battery, value)
		}
		banks = append(banks, battery)
	}

	return banks
}

func solve(banks [][]int) int {
	total_sum := 0

	for _, bank := range banks {
		var second_battery int
		first_battery := slices.Max(bank[:len(bank)-1])
		for position, battery := range bank {
			if battery == first_battery {
				second_battery = slices.Max(bank[position+1:])
				break
			}
		}
		total_sum += first_battery*10 + second_battery
	}
	return total_sum
}

func solution(filename string) int {
	banks := parse(filename)
	return solve(banks)
}

func main() {
	fmt.Println(solution("./example.txt")) // 357
	fmt.Println(solution("./input.txt"))   // 17376
}
