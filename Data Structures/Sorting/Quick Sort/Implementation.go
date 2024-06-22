package main

func QuickSort(arr []int, s int, e int) []int {
	if e-s+1 <= 1 {
		return arr
	}

	pivot := arr[e]
	left := s

	for i := s; i < e; i++ {
		if arr[i] < pivot {
			tmp := arr[left]
			arr[left] = arr[i]
			arr[i] = tmp
			left++
		}
	}

	arr[e] = arr[left]
	arr[left] = pivot

	QuickSort(arr, s, left-1)
	QuickSort(arr, left+1, e)

	return arr
}
