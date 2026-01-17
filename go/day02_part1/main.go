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

func solve(ranges []Range) int {
	sum_of_invalid_ids := 0

	for _, id_range := range ranges {
		for product_id := id_range.start_id; product_id <= id_range.end_id; product_id++ {
			str_id := strconv.Itoa(product_id)
			n := len(str_id)

			if n%2 == 0 {
				half := str_id[:n/2]
				if str_id == half+half {
					sum_of_invalid_ids += product_id
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
	fmt.Println(solution("./example.txt")) // 1227775554
	fmt.Println(solution("./input.txt"))   // 29940924880
}
