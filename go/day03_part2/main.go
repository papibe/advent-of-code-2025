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
		selection := []string{}

		var number int
		for digit := 11; digit >= 0; digit-- {
			if digit > 0 {
				number = slices.Max(bank[:len(bank)-digit])
			} else {
				number = slices.Max(bank)
			}
			for position, battery := range bank {
				if battery == number {
					bank = bank[position+1:]
					selection = append(selection, strconv.Itoa(number))
					break
				}
			}
		}
		value, _ := strconv.Atoi(strings.Join(selection, ""))
		total_sum += value
	}
	return total_sum
}

func solution(filename string) int {
	banks := parse(filename)
	return solve(banks)
}

func main() {
	fmt.Println(solution("./example.txt")) // 3121910778619
	fmt.Println(solution("./input.txt"))   // 172119830406258
}
