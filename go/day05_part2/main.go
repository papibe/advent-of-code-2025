package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

type IngredientRanges struct {
	start int
	end   int
}

func parse(filename string) []IngredientRanges {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}
	blocks := strings.Split(string(data), "\n\n")
	// available_ingredients := []int{}
	// for _, str_number := range strings.Split(strings.Trim(blocks[1], "\n"), "\n") {
	// 	value, _ := strconv.Atoi(str_number)
	// 	available_ingredients = append(available_ingredients, value)
	// }

	ingredient_ranges := []IngredientRanges{}
	lines := strings.Split(strings.Trim(string(blocks[0]), "\n"), "\n")
	for _, line := range lines {
		split_line := strings.Split(line, "-")
		start, _ := strconv.Atoi(split_line[0])
		end, _ := strconv.Atoi(split_line[1])
		ingredient_ranges = append(ingredient_ranges, IngredientRanges{start, end})
	}

	return ingredient_ranges
}

func solve(ranges []IngredientRanges) int {
	sort.Slice(ranges, func(i, j int) bool {
		if ranges[i].start != ranges[j].start {
			return ranges[i].start < ranges[j].start
		}
		return ranges[i].end < ranges[j].end
	})

	new_ranges := []IngredientRanges{ranges[0]}

	for _, i_range := range ranges {
		n := len(new_ranges)
		last_start := new_ranges[n-1].start
		last_end := new_ranges[n-1].end

		if i_range.start > last_end {
			new_ranges = append(
				new_ranges, IngredientRanges{i_range.start, i_range.end},
			)
		} else {
			new_ranges[n-1] = IngredientRanges{last_start, max(last_end, i_range.end)}
		}
	}

	total_fresh_ingredients := 0
	for _, i_range := range new_ranges {
		total_fresh_ingredients += i_range.end - i_range.start + 1
	}
	return total_fresh_ingredients
}

func solution(filename string) int {
	ranges := parse(filename)
	return solve(ranges)
}

func main() {
	fmt.Println(solution("./example.txt")) // 14
	fmt.Println(solution("./input.txt"))   // 345821388687084
}
