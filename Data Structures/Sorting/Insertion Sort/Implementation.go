package main

func insertionSort(arr []int) []int {
	for i := 1; i < len(arr); i++ {
		j := i - 1
		for j >= 0 && arr[j+1] < arr[j] {
			tmp := arr[j+1]
			arr[j+1] = arr[j]
			arr[j] = tmp
			j--
		}
	}
	return arr
}
