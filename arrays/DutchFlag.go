package main

import (
	"fmt"
	"os"
	"strconv"
	"math/rand"
	"time"
)


// Ordered Integers inplace by less-than-pivot, 
// equal-to-pivot, and greater-than pivot
func GroupIntegersInplace(numbers[] int, pidx int) {
	pivot := numbers[pidx]
	low := 0

	for i := 0; i < len(numbers); i++ {
		if numbers[i] < pivot {
			swap(numbers, i, low)
			low++
		}
	}

	high := len(numbers) - 1
	for i := high; i >= 0; i-- {
		if numbers[i] > pivot {
			swap(numbers, i, high)
			high--
		}
	}
}


// Swaps integers inplace in array at indexes i and j
func swap(array []int, i int, j int) {
	temp := array[i]
	array[i] = array[j]
	array[j] = temp
}


// Groups integers by less-than-pivot, equal-to-pivot,
// greater-than-pivot into slices, combines them, and returns
// the result
func GroupIntegers(numbers []int, pivot int) []int {
	var ordered, lt, eq, gt []int
	for i := 0; i < len(numbers); i++ {
		if numbers[i] < pivot {
			lt = append(lt, numbers[i])
		} else if numbers[i] == pivot {
			eq = append(eq, numbers[i])
		} else {
			gt = append(gt, numbers[i])
		}
	}

	// combine slices
	ordered = append(ordered, lt...)
	ordered = append(ordered, eq...)
	ordered = append(ordered, gt...)
	return ordered
}


func GetLowHighPivotIndexes(numbers []int, pivot int) (int, int) {
	var init bool
	var lo, hi int
	for i := 0; i < len(numbers); i++ {
		if numbers[i] == pivot {
			if !init {
				init = true
				lo, hi = i, i
			} else {
				hi++
			}
		}
	}
	return lo, hi
}


func AllPivotValuesContiguous(numbers []int, pivot int) bool {
	lo, hi := GetLowHighPivotIndexes(numbers, pivot)
	for i := lo; i <= hi; i++ {
		if numbers[i] != pivot {
			return false
		}
	}
	return true
}


func AllNumbersGroupedAroundPivot(numbers []int, pivot int) bool {
	lo, hi := GetLowHighPivotIndexes(numbers, pivot)
	for i := 0; i < lo; i++ {
		if numbers[i] >= pivot {
			return false
		}
	}

	for i := hi+1; i < len(numbers); i++ {
		if numbers[i] <= pivot {
			return false
		}
	}
	return true
}


func main() {
	var n int
	var err error
	nstr := os.Args[1]
	if n, err = strconv.Atoi(nstr); err != nil {
		panic(err)
	}
	
	seed := rand.NewSource(time.Now().UnixNano())
	r := rand.New(seed)
	limit := 25
	numbers := make([]int, n)
	for i := 0; i < n; i++ {
		numbers[i] = r.Intn(limit)
	}

	// get random index for pivot
	pidx := r.Intn(n)
	pivot := numbers[pidx]

	fmt.Println("Original List:")
	fmt.Println(numbers)
	fmt.Println("Pivot:")
	fmt.Println(pivot)
	fmt.Println()

	fmt.Println("Ordered List:")
	ordered := GroupIntegers(numbers, pivot)
	fmt.Println(ordered)
	fmt.Println()

	// check that the program works correctly
	check := AllPivotValuesContiguous(ordered, pivot) && AllNumbersGroupedAroundPivot(ordered, pivot)
	if check {
		fmt.Println("All Tests Pass")
	} else {
		fmt.Println("Tests Failed")
	}


	fmt.Println("Original List:")
	fmt.Println(numbers)
	GroupIntegersInplace(numbers, pidx)
	fmt.Println()
	fmt.Println("Ordered List:")
	fmt.Println(numbers)
	fmt.Println()

	// check that the program works correctly
	check = AllPivotValuesContiguous(numbers, pivot) && AllNumbersGroupedAroundPivot(numbers, pivot)
	if check {
		fmt.Println("All Tests Pass")
	} else {
		fmt.Println("Tests Failed")
	}
}