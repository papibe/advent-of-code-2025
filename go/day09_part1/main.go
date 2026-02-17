package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

type Corner struct {
	x int
	y int
}

func parse(filename string) []Corner {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}

	corners := []Corner{}
	lines := strings.Split(strings.Trim(string(data), "\n"), "\n")
	for _, line := range lines {
		str_numbers := strings.Split(line, ",")
		y, _ := strconv.Atoi(str_numbers[0])
		x, _ := strconv.Atoi(str_numbers[1])
		corners = append(corners, Corner{x, y})
	}

	return corners
}

func area(x1, y1, x2, y2 int) float64 {
	d1 := float64(x1 - x2 + 1)
	d2 := float64(y1 - y2 + 1)
	return math.Abs(d1) * math.Abs(d2)
}

func solve(corners []Corner) int {
	max_area := 0.0
	n := len(corners)

	for i, corner1 := range corners {
		for j := i + 1; j < n; j++ {
			corner2 := corners[j]
			max_area = max(max_area, area(corner1.x, corner1.y, corner2.x, corner2.y))
		}
	}
	return int(max_area)
}

func solution(filename string) int {
	corners := parse(filename)
	return solve(corners)
}

func main() {
	fmt.Println(solution("./example.txt")) // 50
	fmt.Println(solution("./input.txt"))   // 4739623064
}
