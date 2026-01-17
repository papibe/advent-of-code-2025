package main

import (
	"fmt"
	"os"
	"regexp"
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

			for pattern_len := 1; pattern_len <= n/2; pattern_len++ {
				if n%pattern_len != 0 {
					continue
				}
				re_pattern := regexp.MustCompile(`^(` + str_id[:pattern_len] + `)` + `{2,}$`)
				matches := re_pattern.FindStringSubmatch(str_id)
				if len(matches) > 0 {
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
	// it takes ~26secs
	fmt.Println(solution("./example.txt")) // 4174379265
	fmt.Println(solution("./input.txt"))   // 48631958998
}
