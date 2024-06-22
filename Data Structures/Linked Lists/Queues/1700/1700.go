package main

func countStudents(students []int, sandwiches []int) int {
	var count int
	for len(students) > 0 {
		if students[0] == sandwiches[0] {
			// The student can eat the sandwich
			students = students[1:]     // Remove the student from the queue
			sandwiches = sandwiches[1:] // Remove the sandwich from the stack
			count = 0                   // Reset count since a student ate a sandwich
		} else {
			// The student goes to the end of the queue
			students = append(students[1:], students[0])
			count++ // Increment count since no student ate a sandwich
		}
		// If all students have been moved to the end of the queue without eating
		if count == len(students) {
			break
		}
	}
	return len(students) // The number of students unable to eat
}
