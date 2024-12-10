package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

var nextSteps [][]int = [][]int{
	{1, 0},
	{0, 1},
	{-1, 0},
	{0, -1}}

func inMap(r, c, lr, lc int) bool {
	return (r >= 0) && (c >= 0) && (r < lr) && (c < lc)
}

func removeDuplicates(input [][]int) [][]int {
	seen := make(map[int]bool)
	result := [][]int{}

	for _, elem := range input {
		if !seen[elem[0]*10000+elem[1]] {
			result = append(result, elem)
			seen[elem[0]*10000+elem[1]] = true
		}
	}

	return result
}

func runTrail(mapa [][]int, start []int) [][]int {
	lr := len(mapa)
	lc := len(mapa[0])
	startValue := mapa[start[0]][start[1]]
	if startValue == 9 {

		return [][]int{start}
	}

	validPath := [][]int{}
	for _, d := range nextSteps {
		newPos := []int{start[0] + d[0], start[1] + d[1]}
		if inMap(newPos[0], newPos[1], lr, lc) {
			if mapa[newPos[0]][newPos[1]] == startValue+1 {
				valids := runTrail(mapa, newPos)
				validPath = append(validPath, valids...)
			}
		}
	}
	return validPath
}

func main() {
	start := time.Now()
	var data, _ = os.ReadFile("myinput")
	var lines = strings.Split(string(data), "\n")

	var mapa [][]int
	for _, l := range lines {

		row := []int{}
		for _, c := range l {
			num, _ := strconv.Atoi(string(c))
			row = append(row, num)
		}

		mapa = append(mapa, row)
	}

	scores := 0
	scoresA := 0
	for r, l := range mapa {
		for c, val := range l {
			if val == 0 {
				options := runTrail(mapa, []int{r, c})
				scores += len(options)
				scoresA += len(removeDuplicates(options))
			}
		}
	}
	fmt.Printf("ResultadoA : %d\n", scoresA)
	fmt.Printf("ResultadoB : %d\n", scores)
	fmt.Printf("Time: %s\n", time.Since(start))

}
