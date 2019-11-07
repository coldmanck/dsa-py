def insertion_sort(arr):
	for i in range(1, len(arr)):
		j = i
		while arr[j] < arr[j-1] and j >= 1:
			arr[j], arr[j - 1] = arr[j - 1], arr[j]
			j -= 1
	return arr

def selection_sort(arr):
	for i in range(len(arr) - 1):
		for j in range(i + 1, len(arr)):
			if arr[i] > arr[j]:
				arr[i], arr[j] = arr[j], arr[i]
	return arr

def bubble_sort(arr):
	for i in range(len(arr), 0, -1):
		for j in range(i - 1):
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
	return arr
