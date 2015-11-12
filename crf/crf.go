package main

import (
	"encoding/csv"
	"fmt"
	"io"
	//"github.com/gonum/lapack"
	"math"
	"os"
	"strconv"
)

func learniteration(fmat [][]int, theta [][]float64, rowc int) {
	exp := make([][4]float64, rowc)

	for row, _ := range fmat {
		for col := 0; col < 4; col++ {
			var sum float64
			for k, _ := range fmat[row] {
				sum += math.Exp(float64(fmat[row][k]) * theta[k][col])
			}
			exp[row][col] = sum
		}
	}

	for _, v := range exp {
		fmt.Fprintf(os.Stdout, "%v\n", v)
	}
}

func main() {
	f, err := os.Open(os.Args[1])
	if err != nil {
		fmt.Fprintf(os.Stderr, "Couldn't open fiiiile\n")
		os.Exit(1)
	}

	var l int
	var rownr int

	fr := csv.NewReader(f)

	X := make([][]int, 8)

	for {
		row, err := fr.Read()
		if err != nil {
			if err != io.EOF {
				fmt.Fprintf(os.Stderr, "Error when reading row\n")
			}
			break
		}
		if l == 0 {
			l = len(row)
		}

		fmt.Fprintf(os.Stdout, "%q\n", row)
		for _, sf := range row {
			ii, err := strconv.Atoi(sf)
			if err != nil {
				fmt.Fprintf(os.Stderr, "Error when being sad\n")
				os.Exit(1)
			}
			X[rownr] = append(X[rownr], ii)
		}
		rownr++
	}

	theta := make([][]float64, l)

	for i, _ := range theta {
		//theta[i] = make([]float64, 4)
		theta[i] = []float64{2, 3, 5.2, 4}
	}
	learniteration(X, theta, l)
}
