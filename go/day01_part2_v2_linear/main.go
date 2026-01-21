package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

const RIGHT = 'R'

type Rotation struct {
	direction rune
	amount    int
}

func parse(filename string) []Rotation {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}

	rotations := []Rotation{}
	lines := strings.Split(strings.Trim(string(data), "\n"), "\n")
	for _, line := range lines {
		direction := rune(line[0])
		amount, _ := strconv.Atoi(line[1:])
		rotations = append(rotations, Rotation{direction, amount})
	}

	return rotations
}

func mod(a, b int) int {
	// equivalent function to % in python
	return (a%b + b) % b
}

func solve(rotations []Rotation) int {
	dial_pointer := 50
	zero_clicks := 0
	var spin int

	for _, rot := range rotations {
		// amount = 100k + r
		k := rot.amount / 100
		r := mod(rot.amount, 100)
		zero_clicks += k

		if rot.direction == RIGHT {
			if dial_pointer+r >= 100 {
				zero_clicks++
			}
			spin = 1

		} else {
			if dial_pointer > 0 && (dial_pointer-r) <= 0 {
				zero_clicks++
			}
			spin = -1
		}

		dial_pointer = mod(dial_pointer+spin*rot.amount, 100)
	}
	return zero_clicks
}

func solution(filename string) int {
	rotations := parse(filename)
	return solve(rotations)
}

func main() {
	fmt.Println(solution("./example.txt")) // 6
	fmt.Println(solution("./input.txt"))   // 6907
}
