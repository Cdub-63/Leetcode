package main

func binarySearch(arr []int, target int) int {
	L, R := 0, len(arr)-1
	var mid int

	for L <= R {
		mid = (L + R) / 2
		if target > arr[mid] {
			L = mid + 1
		} else if target < arr[mid] {
			R = mid - 1
		} else {
			return mid
		}
	}
	return -1
}
