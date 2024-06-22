package main

func binarySearch(low, high int) int {
	var mid int

	for low <= high {
		mid = (low + high) / 2

		switch {
		case isCorrect(mid) > 0:
			high = mid - 1
		case isCorrect(mid) < 0:
			low = mid + 1
		default:
			return mid
		}
	}
	return -1
}

func isCorrect(n int) int {
	switch {
	case n > 10:
		return 1
	case n < 10:
		return -1
	default:
		return 0
	}
}
