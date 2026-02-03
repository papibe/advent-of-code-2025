package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type IngredientRanges struct {
	start int
	end   int
}

func parse(filename string) ([]IngredientRanges, []int) {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}
	blocks := strings.Split(string(data), "\n\n")
	available_ingredients := []int{}
	for _, str_number := range strings.Split(strings.Trim(blocks[1], "\n"), "\n") {
		value, _ := strconv.Atoi(str_number)
		available_ingredients = append(available_ingredients, value)
	}

	ingredient_ranges := []IngredientRanges{}
	lines := strings.Split(strings.Trim(string(blocks[0]), "\n"), "\n")
	for _, line := range lines {
		split_line := strings.Split(line, "-")
		start, _ := strconv.Atoi(split_line[0])
		end, _ := strconv.Atoi(split_line[1])
		ingredient_ranges = append(ingredient_ranges, IngredientRanges{start, end})
	}

	return ingredient_ranges, available_ingredients
}

func solve(ranges []IngredientRanges, ingredients []int) int {
	available_fresh_ingredients := 0

	for _, ingredient := range ingredients {
		for _, i_range := range ranges {
			if i_range.start <= ingredient && ingredient <= i_range.end {
				available_fresh_ingredients++
				break
			}
		}
	}

	return available_fresh_ingredients
}

func solution(filename string) int {
	ranges, ingredients := parse(filename)
	return solve(ranges, ingredients)
}

func main() {
	fmt.Println(solution("./example.txt")) // 3
	fmt.Println(solution("./input.txt"))   // 733
}
