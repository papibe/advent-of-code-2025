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

// equivalent function to % in python
func mod(a, b int) int {
	return (a%b + b) % b
}

func solve(rotations []Rotation) int {
	dial_pointer := 50
	zeros := 0

	for _, rot := range rotations {
		if rot.direction == RIGHT {
			dial_pointer = mod(dial_pointer+rot.amount, 100)
		} else {
			dial_pointer = mod(dial_pointer-rot.amount, 100)
		}

		if dial_pointer == 0 {
			zeros++
		}
	}
	return zeros
}

func solution(filename string) int {
	rotations := parse(filename)
	return solve(rotations)
}

func main() {
	fmt.Println(solution("./example.txt")) // 3
	fmt.Println(solution("./input.txt"))   // 1182
}
