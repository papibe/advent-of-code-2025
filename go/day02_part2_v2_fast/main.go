package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Range struct {
	start_id int
	end_id   int
}

func parse(filename string) []Range {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}

	ranges := []Range{}
	lines := strings.Split(strings.Trim(string(data), "\n"), ",")
	for _, id_range := range lines {
		ids := strings.Split(id_range, "-")
		start_id, _ := strconv.Atoi(ids[0])
		end_id, _ := strconv.Atoi(ids[1])
		ranges = append(ranges, Range{start_id, end_id})
	}

	return ranges
}

func check_symmetry(n, pattern_len int, str_id string) bool {
	for i := 0; i < pattern_len; i++ {
		for j := 1; j < n/pattern_len; j++ {
			if str_id[i] != str_id[i+j*pattern_len] {
				return false
			}
		}
	}
	return true
}

func solve(ranges []Range) int {
	sum_of_invalid_ids := 0

	for _, id_range := range ranges {
		for product_id := id_range.start_id; product_id <= id_range.end_id; product_id++ {
			str_id := strconv.Itoa(product_id)
			n := len(str_id)

			for pattern_len := 1; pattern_len <= n/2; pattern_len++ {
				if n%pattern_len != 0 {
					continue
				}

				if check_symmetry(n, pattern_len, str_id) {
					sum_of_invalid_ids += product_id
					break
				}
			}
		}
	}
	return sum_of_invalid_ids
}

func solution(filename string) int {
	rotations := parse(filename)
	return solve(rotations)
}

func main() {
	// it takes <200ms
	fmt.Println(solution("./example.txt")) // 4174379265
	fmt.Println(solution("./input.txt"))   // 48631958998
}
