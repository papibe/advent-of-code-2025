package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

const ON = '#'

type Machine struct {
	goal    int
	lights  int
	buttons []int
}

func (m *Machine) reset_lights() {
	m.lights = 0
}

func (m *Machine) is_on() bool {
	return m.lights == m.goal
}

func (m *Machine) press(button_value int) {
	m.lights ^= button_value
}

func NewMachine(lights string, str_buttons []string) *Machine {
	goal := 0

	for i, char := range lights[1 : len(lights)-1] {
		if char == ON {
			goal |= 1 << i
		}
	}
	buttons := []int{}
	for _, button := range str_buttons {
		button_value := 0
		for _, char := range strings.Split(button[1:len(button)-1], ",") {
			value, _ := strconv.Atoi(char)
			button_value |= 1 << value
		}
		buttons = append(buttons, button_value)
	}
	return &Machine{goal, 0, buttons}
}

func parse(filename string) []Machine {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}

	machines := []Machine{}
	lines := strings.Split(strings.Trim(string(data), "\n"), "\n")
	for _, line := range lines {
		spit_line := strings.Split(line, " ")
		n := len(spit_line)
		lights := spit_line[0]
		buttons := spit_line[1 : n-1]
		// joltage := spit_line[n-1]
		machines = append(machines, *NewMachine(lights, buttons))
	}

	return machines
}

func get_min_presses(machine Machine) int {
	n := len(machine.buttons)

	for size := 1; size <= n; size++ {
		for _, perms := range combinations(machine.buttons, size) {
			_ = perms
			machine.reset_lights()
			for _, button_value := range perms {
				machine.press(button_value)
			}
			if machine.is_on() {
				return size
			}
		}
	}
	return -1
}

func solve(machines []Machine) int {
	sum_of_presses := 0
	for _, machine := range machines {
		sum_of_presses += get_min_presses(machine)
	}
	return sum_of_presses
}

func solution(filename string) int {
	machines := parse(filename)
	return solve(machines)
}

func main() {
	fmt.Println(solution("./example.txt")) // 7
	fmt.Println(solution("./input.txt"))   // 491
}
