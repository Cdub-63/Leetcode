package main

func factorial(n int) int {
	// Base case: n = 0 or 1
	if n <= 1 {
		return 1
	}
	// Recursive case: n! = n * (n - 1)!
	return n * factorial(n-1)
}
