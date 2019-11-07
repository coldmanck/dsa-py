def binary_search(arr, n):
	return _binary_search(sorted(arr), n, 0, len(arr) - 1)

def _binary_search(arr, n, start, end):
	if start > end:
		return 0

	mid = int((start + end) / 2)
	if n == arr[mid]:
		return 1
	elif n < arr[mid]:
		return _binary_search(arr, n, start, mid - 1)
	else:
		return _binary_search(arr, n, mid + 1, end)
