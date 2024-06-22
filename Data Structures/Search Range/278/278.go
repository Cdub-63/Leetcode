package main

func firstBadVersion(n int) int {
	left, right := 1, n
	for left < right {
		mid := left + (right-left)/2
		if isBadVersion(mid) {
			right = mid // The first bad version is at mid or before mid
		} else {
			left = mid + 1 // The first bad version is after mid
		}
	}
	return left // left and right converge to the first bad version
}
