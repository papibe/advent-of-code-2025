package main

import (
	"fmt"
	"math"
	"os"
	"slices"
	"strconv"
	"strings"
)

const ON = '#'
const INFINITE = 1_000_000 // big number outside results domain

type Machine struct {
	goal    int
	lights  int
	buttons []int
	joltage []int
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

func (m *Machine) is_jolted_balanced() bool {
	for _, joltage := range m.joltage {
		if joltage != 0 {
			return false
		}
	}
	return true
}

func (m *Machine) is_overloaded() bool {
	for _, joltage := range m.joltage {
		if joltage < 0 {
			return true
		}
	}
	return false
}

func (m *Machine) set_lights_parity_goal() {
	goal := 0
	for i, joltage := range m.joltage {
		if joltage%2 == 1 {
			goal |= 1 << i
		}
	}
	m.goal = goal
}

func (m *Machine) half_joltage() {
	for i := range len(m.joltage) {
		m.joltage[i] /= 2
	}
}

func (m *Machine) update_joltage(vector []int) {
	for i := range len(m.joltage) {
		m.joltage[i] -= vector[i]
	}
}

func (m *Machine) hash_key() string {
	key_digits := []string{}
	for _, digit := range m.joltage {
		key_digits = append(key_digits, strconv.Itoa(digit))
	}
	return strings.Join(key_digits, "")
}

func NewMachine(lights string, str_buttons []string, joltage string) *Machine {
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
	jolt := []int{}
	for _, char := range strings.Split(joltage[1:len(joltage)-1], ",") {
		jolt_value, _ := strconv.Atoi(char)
		jolt = append(jolt, jolt_value)
	}
	return &Machine{goal, 0, buttons, jolt}
}

type ButtonCombo struct {
	len    int
	vector []int
}

func parse(filename string) []*Machine {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}

	machines := []*Machine{}
	lines := strings.Split(strings.Trim(string(data), "\n"), "\n")
	for _, line := range lines {
		spit_line := strings.Split(line, " ")
		n := len(spit_line)
		lights := spit_line[0]
		buttons := spit_line[1 : n-1]
		joltage := spit_line[n-1]
		machines = append(machines, NewMachine(lights, buttons, joltage))
	}

	return machines
}

func get_diff_vector(combo []int, size int) []int {
	vector := make([]int, size)
	for _, n := range combo {
		for i := range size {
			if n&(1<<i) != 0 {
				vector[i] += 1
			}
		}
	}
	return vector
}

func get_all_button_combos(buttons []int, machine *Machine) map[int][]ButtonCombo {
	combos := make(map[int][]ButtonCombo)
	for size := range len(buttons) + 1 {
		for _, combo := range combinations(buttons, size) {
			parity := 0
			for _, button := range combo {
				parity ^= button
			}
			_, seen := combos[parity]
			if !seen {
				combos[parity] = []ButtonCombo{}
			}
			combos[parity] = append(
				combos[parity],
				ButtonCombo{
					len(combo), get_diff_vector(combo, len(machine.joltage)),
				},
			)
		}
	}
	return combos
}

func copy_machine(machine *Machine) *Machine {
	n := len(machine.buttons)
	new_buttons := make([]int, n)
	for i := range n {
		new_buttons[i] = machine.buttons[i]
	}

	n = len(machine.joltage)
	new_joltage := make([]int, n)
	for i := range n {
		new_joltage[i] = machine.joltage[i]
	}

	return &Machine{machine.goal, machine.lights, new_buttons, new_joltage}
}

func get_min_presses(machine *Machine) int {
	buttons_combos := get_all_button_combos(machine.buttons, machine)
	memo := make(map[string]int)

	var _get_min_presses func(machine *Machine) int

	_get_min_presses = func(machine *Machine) int {
		if machine.is_jolted_balanced() {
			return 0
		}
		if machine.is_overloaded() {
			return math.MaxInt
		}

		key := machine.hash_key()
		cached_value, in_memo := memo[key]
		if in_memo {
			return cached_value
		}

		machine.set_lights_parity_goal()
		presses, in_combos := buttons_combos[machine.goal]
		if !in_combos {
			return INFINITE
		}
		results := []int{INFINITE}
		for _, button_combo := range presses {
			press := button_combo.len
			vector := button_combo.vector

			new_machine := copy_machine(machine)
			new_machine.update_joltage(vector)

			if new_machine.is_overloaded() {
				continue
			}

			new_machine.half_joltage()
			results = append(results, 2*_get_min_presses(new_machine)+press)
		}
		memo[key] = slices.Min(results)
		return memo[key]
	}

	return _get_min_presses(machine)
}

func solve(machines []*Machine) int {
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
	fmt.Println(solution("./example.txt")) // 33
	fmt.Println(solution("./input.txt"))   // 20617
}
