package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

type Corner struct {
	row int
	col int
}

func abs(a int) int {
	if a > 0 {
		return a
	}
	return -a
}

func (c Corner) area(c2 Corner) int {
	return (abs(c.row-c2.row) + 1) * (abs(c.col-c2.col) + 1)
}

type Segment struct {
	c1 Corner
	c2 Corner
}

type MovieTheater struct {
	points      []Corner
	green_lines []Segment
}

var memo = map[Corner]bool{}

func (mt *MovieTheater) is_inside(p Corner) bool {

	_, seen := memo[p]
	if seen {
		return memo[p]
	}

	inside := false

	for _, segment := range mt.green_lines {
		g1 := segment.c1
		g2 := segment.c2

		if p.col == g1.col &&
			p.col == g2.col &&
			min(g1.row, g2.row) <= p.row &&
			p.row <= max(g1.row, g2.row) {
			memo[p] = true
			return true
		}
		if p.row == g1.row &&
			p.row == g2.row &&
			min(g1.col, g2.col) <= p.col &&
			p.col <= max(g1.col, g2.col) {
			memo[p] = true
			return true
		}
		if (g1.row > p.row) != (g2.row > p.row) &&
			p.col < ((g2.col-g1.col)*(p.row-g1.row)/(g2.row-g1.row)+g1.col) {
			inside = !inside
		}
	}
	memo[p] = inside
	return inside
}

func (mt *MovieTheater) valid_square(c1, c2 Corner) bool {
	p1 := Corner{min(c1.row, c2.row), min(c1.col, c2.col)}
	p3 := Corner{max(c1.row, c2.row), max(c1.col, c2.col)}
	p2 := Corner{p1.row, p3.col}
	p4 := Corner{p3.row, p1.col}

	for _, p := range []Corner{p1, p2, p3, p4} {
		if !mt.is_inside(p) {
			return false
		}
	}

	for _, segment := range mt.green_lines {
		if mt.intersect(p1, p3, segment) {
			return false
		}
	}
	return true
}

func (mt *MovieTheater) intersect(p1, p2 Corner, segment Segment) bool {
	edge_row1 := min(segment.c1.row, segment.c2.row)
	edge_col1 := min(segment.c1.col, segment.c2.col)
	edge_row2 := max(segment.c1.row, segment.c2.row)
	edge_col2 := max(segment.c1.col, segment.c2.col)

	// pre calculated bool expressions
	left_of_rectangle := (p2.col <= edge_col1)
	right_of_rectangle := (p1.col >= edge_col2)
	above_of_rectangle := (p2.row <= edge_row1)
	below_of_rectangle := (p1.row >= edge_row2)

	return !(left_of_rectangle || right_of_rectangle || above_of_rectangle || below_of_rectangle)
}

func NewMovieTheater(points []Corner) *MovieTheater {
	n := len(points)
	green_lines := []Segment{}

	for index := range n {
		c1 := points[index]
		c2 := points[(index+1)%n]
		green_lines = append(green_lines, Segment{c1, c2})
	}
	return &MovieTheater{points, green_lines}
}

func parse(filename string) *MovieTheater {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}

	corners := []Corner{}
	lines := strings.Split(strings.Trim(string(data), "\n"), "\n")
	for _, line := range lines {
		str_numbers := strings.Split(line, ",")
		col, _ := strconv.Atoi(str_numbers[0])
		row, _ := strconv.Atoi(str_numbers[1])
		corners = append(corners, Corner{row, col})
	}

	return NewMovieTheater(corners)
}

func area(x1, y1, x2, y2 int) float64 {
	d1 := float64(x1 - x2 + 1)
	d2 := float64(y1 - y2 + 1)
	return math.Abs(d1) * math.Abs(d2)
}

func solve(movie_theater *MovieTheater) int {
	n := len(movie_theater.points)
	max_area := 0

	for i, corner1 := range movie_theater.points {
		for j := i + 1; j < n; j++ {
			corner2 := movie_theater.points[j]
			area := corner1.area(corner2)

			if area > max_area && movie_theater.valid_square(corner1, corner2) {
				max_area = area
			}
		}
	}
	return int(max_area)
}

func solution(filename string) int {
	movie_theater := parse(filename)
	// fmt.Println(*movie_theater)
	return solve(movie_theater)
}

func main() {
	fmt.Println(solution("./example.txt")) // 24
	fmt.Println(solution("./input.txt"))   // 1654141440
}
