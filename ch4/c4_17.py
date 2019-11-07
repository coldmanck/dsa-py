def is_palindrome(arr):
	return _is_palindrome(arr, 0, len(arr) - 1)

def _is_palindrome(arr, start, end):
	if start >= end:
		return True
	else:
		if arr[start] != arr[end]:
			return False
		return _is_palindrome(arr, start + 1, end - 1)
