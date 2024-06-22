package main

func bucketSort(arr []int) []int {
	// Assuming arr only contains 0, 1 or 2
	counts := [3]int{0, 0, 0}

	// Count the quantity of each val in arr
	for _, num := range arr {
		counts[num]++
	}

	// Fill each bucket in the original array
	i := 0
	for n, count := range counts {
		for j := 0; j < count; j++ {
			arr[i] = n
			i++
		}
	}
	return arr
}
