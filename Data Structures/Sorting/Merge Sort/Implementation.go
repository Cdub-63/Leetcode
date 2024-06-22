package main

func mergeSort(arr []int, l int, r int) []int {
	if l < r {
		m := (l + r) / 2

		mergeSort(arr, l, m)
		mergeSort(arr, m+1, r)
		merge(arr, l, m, r)
	}
	return arr
}

func merge(arr []int, l int, m int, r int) {
	length1 := m - l + 1
	length2 := r - m

	L := make([]int, length1)
	R := make([]int, length2)

	for i := 0; i < length1; i++ {
		L[i] = arr[l+i]
	}

	for j := 0; j < length2; j++ {
		R[j] = arr[m+1+j]
	}

	i := 0
	j := 0
	k := l

	for i < length1 && j < length2 {
		if L[i] <= R[j] {
			arr[k] = L[i]
			i++
		} else {
			arr[k] = R[j]
			j++
		}
		k++
	}

	for i < length1 {
		arr[k] = L[i]
		i++
		k++
	}

	for j < length2 {
		arr[k] = R[j]
		j++
		k++
	}
}
