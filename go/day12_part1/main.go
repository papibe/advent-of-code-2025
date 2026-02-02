package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

type Area struct {
	rows       int
	cols       int
	quantities [6]int
}

type Shape struct {
	rows int
	cols int
	grid [][]rune
	used int
}

func parse(filename string) ([]Shape, []Area) {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}
	lines := strings.Split(strings.Trim(string(data), "\n"), "\n")

	re_shape := regexp.MustCompile(`^\d:$`)
	re_area := regexp.MustCompile(`(\d+)x(\d+): (\d+) (\d+) (\d+) (\d+) (\d+) (\d+)`)

	shapes := []Shape{}
	areas := []Area{}

	index := 0
	for index < len(lines) {
		// parse shape
		shape_match := re_shape.MatchString(lines[index])
		if shape_match {
			shape := [][]rune{}
			index++
			// for lines[index] != "" {
			for range 3 {
				shape_row := []rune{}
				for _, char := range lines[index] {
					shape_row = append(shape_row, char)
				}
				shape = append(shape, shape_row)
				index++
			}

			used := 0
			for _, row := range shape {
				for _, cell := range row {
					if cell == '#' {
						used++
					}
				}
			}
			shapes = append(shapes, Shape{len(shape), len(shape[0]), shape, used})
		}

		// parse area
		area_match := re_area.FindStringSubmatch(lines[index])
		if len(area_match) > 0 {
			rows, _ := strconv.Atoi(area_match[1])
			cols, _ := strconv.Atoi(area_match[2])
			q1, _ := strconv.Atoi(area_match[3])
			q2, _ := strconv.Atoi(area_match[4])
			q3, _ := strconv.Atoi(area_match[5])
			q4, _ := strconv.Atoi(area_match[6])
			q5, _ := strconv.Atoi(area_match[7])
			q6, _ := strconv.Atoi(area_match[8])

			areas = append(areas, Area{rows, cols, [6]int{q1, q2, q3, q4, q5, q6}})
		}

		index++
	}

	return shapes, areas
}

func fit_area(area Area, shapes []Shape) bool {
	area_size := area.rows * area.cols

	size_by_side_area_required := 0
	for shape_number, required_amount := range area.quantities {
		shape := shapes[shape_number]
		size_by_side_area_required += shape.rows * shape.cols * required_amount
	}
	if size_by_side_area_required <= area_size {
		return true
	}

	min_used_required := 0
	for shape_number, required_amount := range area.quantities {
		shape := shapes[shape_number]
		min_used_required += shape.used * required_amount
	}
	if min_used_required > area_size {
		return false
	}

	panic("precise size fitting not implemented")
}

func solve(shapes []Shape, areas []Area) int {
	total_sum := 0

	for _, area := range areas {
		if fit_area(area, shapes) {
			total_sum++
		}
	}
	return total_sum
}

func solution(filename string) int {
	shapes, areas := parse(filename)
	return solve(shapes, areas)
}

func main() {
	fmt.Println(solution("./input.txt")) // 575
}
