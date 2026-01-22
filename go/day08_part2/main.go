package main

import (
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
	"strings"
)

type JunctionBox struct {
	x int
	y int
	z int
}

func (j JunctionBox) distance(k JunctionBox) float64 {
	return math.Sqrt(
		math.Pow(float64(j.x-k.x), 2) + math.Pow(float64(j.y-k.y), 2) + math.Pow(float64(j.z-k.z), 2),
	)
}

type UnionFind struct {
	size    int
	parents []int
}

func (uf *UnionFind) find(i int) int {
	root := uf.parents[i]

	if uf.parents[root] != root {
		uf.parents[i] = uf.find(root)
		return uf.parents[i]
	}
	return root
}

func (uf *UnionFind) union(i, j int) {
	i_root := uf.find(i)
	j_root := uf.find(j)
	uf.parents[i_root] = j_root
}

func NewUnionFind(n int) *UnionFind {
	parents := make([]int, n)
	for i := range n {
		parents[i] = i
	}
	return &UnionFind{n, parents}
}

type JBDistance struct {
	distance float64
	jb1      int
	jb2      int
}

func parse(filename string) []JunctionBox {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}

	junction_boxes := []JunctionBox{}
	lines := strings.Split(strings.Trim(string(data), "\n"), "\n")
	for _, line := range lines {
		str_numbers := strings.Split(line, ",")
		x, _ := strconv.Atoi(str_numbers[0])
		y, _ := strconv.Atoi(str_numbers[1])
		z, _ := strconv.Atoi(str_numbers[2])
		junction_boxes = append(junction_boxes, JunctionBox{x, y, z})
	}

	return junction_boxes
}

func solve(junction_boxes []JunctionBox, connections int) int {
	n := len(junction_boxes)
	distances := []JBDistance{}

	for i, jb1 := range junction_boxes {
		for j := i + 1; j < n; j++ {
			jb2 := junction_boxes[j]
			distances = append(distances, JBDistance{jb1.distance(jb2), i, j})
		}
	}

	sort.Slice(distances, func(i, j int) bool {
		return distances[i].distance < distances[j].distance
	})

	union_find := NewUnionFind(n)
	for _, jbd := range distances {
		union_find.union(jbd.jb1, jbd.jb2)

		circuit_sizes := NewSet[int]()
		for k := range n {
			circuit_sizes.add(union_find.find(k))
			if circuit_sizes.len() > 1 {
				break
			}
		}

		if circuit_sizes.len() == 1 {
			return junction_boxes[jbd.jb1].x * junction_boxes[jbd.jb2].x
		}

	}
	return -1
}

func solution(filename string, connections int) int {
	junction_boxes := parse(filename)
	return solve(junction_boxes, connections)
}

func main() {
	fmt.Println(solution("./example.txt", 10))  // 25272
	fmt.Println(solution("./input.txt", 1_000)) // 44543856
}
